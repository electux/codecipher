# -*- coding: UTF-8 -*-

'''
Module
    atbs_test.py
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
    Defines class ATBSTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATBS.
Execute
    python3 -m unittest -v atbs_test
'''

import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.abstracts.ivalidation_engine import IValidationEngine
from codecipher.abstracts.iencoder import IEncoder
from codecipher.abstracts.idecoder import IDecoder
from codecipher.atbs.engine import ATBS

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATBSTestCase(unittest.TestCase):
    '''
        Defines class ATBSTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATBS.

        It defines:

            :attributes:
                | RAW_DATA - Raw text data for encoding.
                | ENC_SEQ - Expected encoded sequence.
                | raw_data - Object container data for encoding.
                | enc_sequence - Object container for encoded sequence.
                | enc_data - Encoded data.
                | dec_data - Decoded data.
                | cipher - Cipher object with mocked dependencies.
                | real_cipher - Real cipher object for integration testing.
                | mock_encoder - Mocked encoder.
                | mock_decoder - Mocked decoder.
                | mock_validation_engine - Mocked validation engine.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_atbs_encoding - Test for base encoding atbs.
                | test_atbs_decoding - Test for base decoding atbs.
                | test_encode_with_none_data - Test for encoding with None data.
                | test_encode_with_validation_failure - Test for encoding with validation failure.
                | test_encode_delegation - Test for encoding delegation to encoder.
                | test_decode_with_none_data - Test for decoding with None data.
                | test_decode_with_decoder_failure - Test for decoding with decoder failure.
                | test_decode_with_validation_failure - Test for decoding with validation failure.
                | test_decode_delegation - Test for decoding delegation to decoder.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'Nliv Sfnzm Gszm Sfnzm98 Rh Lfi Nlggl'

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = ATBSTestCase.RAW_DATA
        self.enc_sequence: Optional[str] = ATBSTestCase.ENC_SEQ
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None

        # Mock dependencies for the base tests
        self.mock_encoder = MagicMock(spec=IEncoder)
        self.mock_encoder.encode.return_value = True
        type(self.mock_encoder).encoded_data = PropertyMock(return_value=self.enc_sequence)

        self.mock_decoder = MagicMock(spec=IDecoder)
        self.mock_decoder.decode.return_value = True
        type(self.mock_decoder).decoded_data = PropertyMock(return_value=self.raw_data)

        self.mock_validation_engine = MagicMock(spec=IValidationEngine)
        self.mock_validation_engine.is_valid.return_value = True

        self.cipher: ATBS = ATBS(
            validation_engine=self.mock_validation_engine,
            encoder=self.mock_encoder,
            decoder=self.mock_decoder
        )

        # Real cipher for integration testing
        self.real_cipher: ATBS = ATBS()

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

    def test_atbs_encoding(self) -> None:
        '''Test base encoding with real cipher.'''
        if bool(self.real_cipher):
            self.enc_data = self.real_cipher.encode(self.raw_data)
            self.assertTrue(bool(self.enc_data))
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_atbs_decoding(self) -> None:
        '''Test base decoding with real cipher.'''
        if bool(self.real_cipher):
            encoded = self.real_cipher.encode(self.raw_data)
            self.assertTrue(bool(encoded))
            self.dec_data = self.real_cipher.decode(encoded)
            self.assertTrue(bool(self.dec_data))
            self.assertEqual(self.raw_data, self.dec_data)

    def test_atbs_with_none_data(self) -> None:
        '''Testing encode with None or empty data.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(None))
            self.assertFalse(self.real_cipher.decode(None))

    def test_atbs_empty_string(self) -> None:
        '''Test encoding and decoding with empty strings.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(''))
            self.assertFalse(self.real_cipher.decode(''))

    def test_atbs_encoding_with_numbers(self) -> None:
        '''Test Atbash transformation of numbers.'''
        # 0 -> 9, 1 -> 8, etc.
        data = "0123456789"
        expected = "9876543210"
        if bool(self.real_cipher):
            result = self.real_cipher.encode(data)
            self.assertEqual(expected, result)

    def test_atbs_encoding_with_spaces(self) -> None:
        '''Test Atbash with spaces (should remain unchanged).'''
        data = "A B C"
        expected = "Z Y X"
        if bool(self.real_cipher):
            result = self.real_cipher.encode(data)
            self.assertEqual(expected, result)

    def test_encode_with_validation_failure(self) -> None:
        '''Testing encode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False # type: ignore
        self.assertFalse(self.cipher.encode(self.raw_data))
        self.mock_validation_engine.is_valid.assert_called_once_with(self.raw_data) # type: ignore
        self.mock_encoder.encode.assert_not_called() # type: ignore

    def test_encode_delegation(self) -> None:
        '''Testing encode delegation to internal encoder.'''
        result = self.cipher.encode(self.raw_data)
        self.assertTrue(result)
        self.mock_validation_engine.is_valid.assert_called_once_with(self.raw_data) # type: ignore
        self.mock_encoder.encode.assert_called_once_with(self.raw_data) # type: ignore
        self.assertEqual(self.enc_sequence, result)

    def test_decode_with_decoder_failure(self) -> None:
        '''Testing decode when internal decoder fails.'''
        self.mock_decoder.decode.return_value = False # type: ignore
        self.assertFalse(self.cipher.decode(self.enc_sequence))
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence) # type: ignore

    def test_decode_with_validation_failure(self) -> None:
        '''Testing decode when validation of decoded data fails.'''
        # Decoder succeeds, but validation engine says NO
        self.mock_decoder.decode.return_value = True # type: ignore
        type(self.mock_decoder).decoded_data = PropertyMock(return_value="invalid_result") # type: ignore
        self.mock_validation_engine.is_valid.return_value = False # type: ignore

        self.assertFalse(self.cipher.decode(self.enc_sequence))
        self.mock_validation_engine.is_valid.assert_called_once_with("invalid_result") # type: ignore

    def test_decode_delegation(self) -> None:
        '''Testing decode delegation to internal decoder and engine.'''
        result = self.cipher.decode(self.enc_sequence)
        self.assertTrue(result)
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence) # type: ignore
        self.mock_validation_engine.is_valid.assert_called_once_with(self.raw_data) # type: ignore
        self.assertEqual(self.raw_data, result)


if __name__ == '__main__':
    unittest.main()
