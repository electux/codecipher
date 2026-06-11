# -*- coding: UTF-8 -*-

'''
Module
    a1z52n62_test.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    codecipher is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    codecipher is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class A1z52N62TestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of A1z52N62.
Execute
    python3 -m unittest -v a1z52n62_test
'''

import random
import string
import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.abstracts import IA1Z52N62Config, IValidationEngine, IEncoder, IDecoder
from codecipher.a1z52n62 import A1z52N62

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class A1z52N62TestCase(unittest.TestCase):
    '''
        Defines class A1z52N62TestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of A1z52N62.

        It defines:

            :attributes:
                | RAW_DATA - Raw text data for encoding.
                | ENC_SEQ - Expected encoded sequence.
                | raw_data - Object container data for encoding.
                | enc_sequence - Object container for encoded sequence.
                | enc_data - Encoded data.
                | dec_data - Decoded data.
                | cipher - Cipher object.
                | real_cipher - Real cipher object for integration testing.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_a1z52n62_encoding - Test for base encoding a1z52n62.
                | test_a1z52n62_decoding - Test for base decoding a1z52n62.
                | test_encode_with_none_data - Test for encoding with None data.
                | test_encode_with_validation_failure - Test for encoding with validation failure.
                | test_encode_delegation - Test for encoding delegation to encoder.
                | test_decode_with_none_data - Test for decoding with None data.
                | test_decode_with_decoder_failure - Test for decoding with decoder failure.
                | test_decode_with_validation_failure - Test for decoding with validation failure.
                | test_decode_delegation - Test for decoding delegation to decoder.
                | test_encode_with_encoder_failure - Test for encoding with encoder failure.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: List[str] = [
        '13', '41', '44', '31', ' ', '8', '47', '39', '27', '40', ' ',
        '20', '34', '27', '40', ' ', '8', '47', '39', '27', '40', '53',
        '54', ' ', '9', '45', ' ', '15', '47', '44', ' ', '13', '41',
        '46', '46', '41'
    ]

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = A1z52N62TestCase.RAW_DATA
        self.enc_sequence: Optional[str] = ' - '.join(A1z52N62TestCase.ENC_SEQ)
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None

        # Mock dependencies for the base tests
        self.mock_encoder = MagicMock(spec=IEncoder)
        self.mock_encoder.encode.return_value = True # type: ignore
        type(self.mock_encoder).encoded_data = PropertyMock(return_value=self.enc_sequence) # type: ignore

        self.mock_decoder = MagicMock(spec=IDecoder)
        self.mock_decoder.decode.return_value = True # type: ignore
        type(self.mock_decoder).decoded_data = PropertyMock(return_value=self.raw_data) # type: ignore

        self.mock_validation_engine = MagicMock(spec=IValidationEngine)
        self.mock_validation_engine.is_valid.return_value = True # type: ignore

        self.mock_config = MagicMock(spec=IA1Z52N62Config)

        self.cipher: A1z52N62 = A1z52N62(
            config=self.mock_config,
            validation_engine=self.mock_validation_engine,
            encoder=self.mock_encoder,
            decoder=self.mock_decoder
        )

        # Real cipher for integration testing
        self.real_cipher: A1z52N62 = A1z52N62()

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None  # type: ignore
        self.real_cipher = None  # type: ignore
        self.mock_encoder = None  # type: ignore
        self.mock_decoder = None  # type: ignore
        self.mock_validation_engine = None  # type: ignore
        self.mock_config = None  # type: ignore

    def test_a1z52n62_encoding(self) -> None:
        '''Testing base encoding.'''
        if bool(self.real_cipher):
            result = self.real_cipher.encode(self.raw_data)
            self.assertTrue(result)
            self.enc_data: Optional[str] = self.real_cipher.encoded_data
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_a1z52n62_decoding(self) -> None:
        '''Testing base decoding.'''
        if bool(self.real_cipher):
            result = self.real_cipher.encode(self.raw_data)
            self.assertTrue(result)
            self.enc_data = self.real_cipher.encoded_data

            result = self.real_cipher.decode(self.enc_data)
            self.assertTrue(result)
            self.dec_data: Optional[str] = self.real_cipher.decoded_data
            self.assertEqual(self.raw_data, self.dec_data)

    def test_encode_with_none_data(self) -> None:
        '''Testing encode with None or empty data.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(None))
            self.assertFalse(self.real_cipher.encode(''))

    def test_encode_with_validation_failure(self) -> None:
        '''Testing encode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False # type: ignore
        result = self.cipher.encode(self.raw_data)
        self.assertFalse(result)
        self.mock_validation_engine.is_valid.assert_called_once_with(self.raw_data) # type: ignore
        self.mock_encoder.encode.assert_not_called() # type: ignore

    def test_encode_delegation(self) -> None:
        '''Testing encode delegation to internal encoder.'''
        result = self.cipher.encode(self.raw_data)
        self.assertTrue(result)
        self.mock_encoder.encode.assert_called_once_with(self.raw_data) # type: ignore
        self.assertEqual(self.enc_sequence, self.cipher.encoded_data)

    def test_encode_with_encoder_failure(self) -> None:
        '''Testing encode when internal encoder fails.'''
        self.mock_encoder.encode.return_value = False # type: ignore
        result = self.cipher.encode(self.raw_data)
        self.assertFalse(result)
        self.mock_encoder.encode.assert_called_once_with(self.raw_data) # type: ignore

    def test_decode_with_none_data(self) -> None:
        '''Testing decode with None or empty data.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.decode(None))
            self.assertFalse(self.real_cipher.decode(''))

    def test_decode_with_decoder_failure(self) -> None:
        '''Testing decode when internal decoder fails.'''
        self.mock_decoder.decode.return_value = False # type: ignore
        result = self.cipher.decode(self.enc_sequence)
        self.assertFalse(result)
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence) # type: ignore

    def test_decode_with_validation_failure(self) -> None:
        '''Testing decode when validation of decoded data fails.'''
        self.mock_decoder.decode.return_value = True # type: ignore
        type(self.mock_decoder).decoded_data = PropertyMock(return_value="decoded_invalid") # type: ignore
        self.mock_validation_engine.is_valid.return_value = False # type: ignore

        result = self.cipher.decode(self.enc_sequence)
        self.assertFalse(result)
        self.mock_validation_engine.is_valid.assert_called_once_with("decoded_invalid") # type: ignore

    def test_decode_delegation(self) -> None:
        '''Testing decode delegation to internal decoder and engine.'''
        result = self.cipher.decode(self.enc_sequence)
        self.assertTrue(result)
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence) # type: ignore
        self.mock_validation_engine.is_valid.assert_called_once_with(self.raw_data) # type: ignore
        self.assertEqual(self.raw_data, self.cipher.decoded_data)

    def test_a1z52n62_random_data_roundtrip(self) -> None:
        '''Testing roundtrip with random data.'''
        if bool(self.real_cipher):
            # Character set: A-Z, a-z, 0-9, and space
            alphabet = string.ascii_letters + string.digits + ' '
            for _ in range(10):  # Run 10 iterations with different random strings
                length = random.randint(10, 50)
                random_str = ''.join(
                    random.choice(alphabet) for _ in range(length)
                )

                self.assertTrue(self.real_cipher.encode(random_str))
                encoded = self.real_cipher.encoded_data

                self.assertTrue(self.real_cipher.decode(encoded))
                decoded = self.real_cipher.decoded_data

                self.assertEqual(random_str, decoded)


if __name__ == '__main__':
    unittest.main()
