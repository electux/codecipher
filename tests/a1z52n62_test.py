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

import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.a1z52n62 import (
    A1z52N62,
    IValidationEngine,
    IA1z52N62Encoder,
    IA1z52N62Decoder
)

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
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: List[str] = [
        '13', '42', '45', '32', ' ', '8', '48', '40', '28', '41', ' ',
        '20', '35', '28', '41', ' ', '8', '48', '40', '28', '41', '53',
        '54', ' ', '9', '46', ' ', '15', '48', '45', ' ', '13', '42',
        '47', '47', '42'
    ]

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = A1z52N62TestCase.RAW_DATA
        self.enc_sequence: Optional[str] = ' - '.join(A1z52N62TestCase.ENC_SEQ)
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None

        # Mock dependencies for the base tests
        self.mock_encoder = MagicMock(spec=IA1z52N62Encoder)
        self.mock_encoder.encode.return_value = True
        type(self.mock_encoder).encode_data = PropertyMock(return_value=self.enc_sequence)

        self.mock_decoder = MagicMock(spec=IA1z52N62Decoder)
        self.mock_decoder.decode.return_value = True
        type(self.mock_decoder).decode_data = PropertyMock(return_value=self.raw_data)

        self.mock_validation_engine = MagicMock(spec=IValidationEngine)
        self.mock_validation_engine.is_valid.return_value = True

        self.cipher: A1z52N62 = A1z52N62(
            validation_engine=self.mock_validation_engine,
            encoder=self.mock_encoder,
            decoder=self.mock_decoder
        )

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None  # type: ignore

    def test_a1z52n62_encoding(self) -> None:
        '''Testing base encoding.'''
        self.cipher.encode(self.raw_data)
        self.enc_data: Optional[str] = self.cipher.encode_data
        self.assertEqual(self.enc_sequence, self.enc_data)

    def test_a1z52n62_decoding(self) -> None:
        '''Testing base decoding.'''
        self.cipher.encode(self.raw_data)
        self.enc_data = self.cipher.encode_data
        self.cipher.decode(self.enc_data)
        self.dec_data: Optional[str] = self.cipher.decode_data
        self.assertEqual(self.raw_data, self.dec_data)

    def test_encode_with_none_data(self) -> None:
        '''Testing encode with None or empty data.'''
        cipher = A1z52N62()
        self.assertFalse(cipher.encode(None))
        self.assertFalse(cipher.encode(''))

    def test_encode_with_validation_failure(self) -> None:
        '''Testing encode when validation engine fails.'''
        mock_engine = MagicMock(spec=IValidationEngine)
        mock_engine.is_valid.return_value = False
        cipher = A1z52N62(validation_engine=mock_engine)

        self.assertFalse(cipher.encode("test_data"))
        mock_engine.is_valid.assert_called_once_with("test_data")

    def test_encode_delegation(self) -> None:
        '''Testing encode delegation to internal encoder.'''
        mock_engine = MagicMock(spec=IValidationEngine)
        mock_engine.is_valid.return_value = True
        mock_encoder = MagicMock(spec=IA1z52N62Encoder)
        mock_encoder.encode.return_value = True
        cipher = A1z52N62(validation_engine=mock_engine, encoder=mock_encoder)

        self.assertTrue(cipher.encode("valid_data"))
        mock_encoder.encode.assert_called_once_with("valid_data")

    def test_decode_with_none_data(self) -> None:
        '''Testing decode with None or empty data.'''
        cipher = A1z52N62()
        self.assertFalse(cipher.decode(None))
        self.assertFalse(cipher.decode(''))

    def test_decode_with_decoder_failure(self) -> None:
        '''Testing decode when internal decoder fails.'''
        mock_decoder = MagicMock(spec=IA1z52N62Decoder)
        mock_decoder.decode.return_value = False
        cipher = A1z52N62(decoder=mock_decoder)

        self.assertFalse(cipher.decode("encoded_data"))
        mock_decoder.decode.assert_called_once_with("encoded_data")

    def test_decode_with_validation_failure(self) -> None:
        '''Testing decode when validation of decoded data fails.'''
        mock_decoder = MagicMock(spec=IA1z52N62Decoder)
        mock_decoder.decode.return_value = True
        type(mock_decoder).decode_data = PropertyMock(return_value="decoded_invalid")

        mock_engine = MagicMock(spec=IValidationEngine)
        mock_engine.is_valid.return_value = False

        cipher = A1z52N62(validation_engine=mock_engine, decoder=mock_decoder)

        self.assertFalse(cipher.decode("encoded_data"))
        mock_engine.is_valid.assert_called_once_with("decoded_invalid")

    def test_decode_delegation(self) -> None:
        '''Testing decode delegation to internal decoder and engine.'''
        mock_decoder = MagicMock(spec=IA1z52N62Decoder)
        mock_decoder.decode.return_value = True
        type(mock_decoder).decode_data = PropertyMock(return_value="decoded_valid")

        mock_engine = MagicMock(spec=IValidationEngine)
        mock_engine.is_valid.return_value = True

        cipher = A1z52N62(validation_engine=mock_engine, decoder=mock_decoder)

        self.assertTrue(cipher.decode("encoded_data"))
        mock_decoder.decode.assert_called_once_with("encoded_data")
        mock_engine.is_valid.assert_called_once_with("decoded_valid")


if __name__ == '__main__':
    unittest.main()
