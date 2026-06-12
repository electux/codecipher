# -*- coding: UTF-8 -*-

'''
Module
    caesar_test.py
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
    Defines class CaesarTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Caesar.
Execute
    python3 -m unittest -v caesar_test
'''

import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.abstracts.ivalidation_engine import IValidationEngine
from codecipher.abstracts.iencoder import IEncoder
from codecipher.abstracts.idecoder import IDecoder
from codecipher.caesar.engine import Caesar

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CaesarTestCase(unittest.TestCase):
    '''
        Defines class CaesarTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Caesar.

        It defines:

            :attributes:
                | RAW_DATA - Raw text data for encoding.
                | ENC_SEQ - Expected encoded sequence.
                | raw_data - Object container data for encoding.
                | enc_sequence - Object container for encoded sequence.
                | enc_data - Encoded data.
                | dec_data - Decoded data.
                | cipher - Cipher object.
                | mock_validation_engine - Mocked validation engine.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_caesar_encoding - Test for base encoding caesar.
                | test_caesar_decoding - Test for base decoding caesar.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'Pruh Kxpdq Wkdq Kxpdq01 Lv Rxu Prwwr'
    EMPTY_DATA: str = ''
    EMPTY_ENC_SEQ: str = ''
    UNICODE_DATA: str = 'Привет, мир! 👋'
    UNICODE_ENC_SEQ: str = 'Привет, мир! 👋' # Caesar cipher implementation ignores non-ASCII letters

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = CaesarTestCase.RAW_DATA
        self.enc_sequence: Optional[str] = CaesarTestCase.ENC_SEQ
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None

        # Mock validation engine to be used by default or for specific tests
        self.mock_validation_engine = MagicMock(spec=IValidationEngine)
        self.mock_validation_engine.is_valid.return_value = True

        # Initialize Caesar with mocked validation engine to avoid strict checks in tests
        self.cipher: Caesar = Caesar(validation_engine=self.mock_validation_engine)

        # Mocks for specific mock interaction tests
        self.mock_encoder = MagicMock(spec=IEncoder)
        self.mock_decoder = MagicMock(spec=IDecoder)
        self.mock_cipher_with_deps: Caesar = Caesar(
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
        self.mock_encoder = None  # type: ignore
        self.mock_decoder = None  # type: ignore
        self.mock_cipher_with_deps = None  # type: ignore
        self.mock_validation_engine = None  # type: ignore

    def test_caesar_encoding(self) -> None:
        '''Test base encoding.'''
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(self.raw_data)
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_caesar_decoding(self) -> None:
        '''Test base decoding.'''
        if bool(self.cipher):
            encoded = self.cipher.encode(self.raw_data)
            self.dec_data = self.cipher.decode(encoded)
            self.assertEqual(self.raw_data, self.dec_data)

    def test_caesar_encoding_empty_string(self) -> None:
        '''Test encoding an empty string.'''
        if bool(self.cipher):
            result = self.cipher.encode(self.EMPTY_DATA)
            self.assertFalse(result)

    def test_caesar_decoding_empty_string(self) -> None:
        '''Test decoding an empty string.'''
        if bool(self.cipher):
            result = self.cipher.decode(self.EMPTY_ENC_SEQ)
            self.assertFalse(result)

    def test_caesar_with_none_data(self) -> None:
        '''Test encoding and decoding with None data.'''
        if bool(self.cipher):
            self.assertFalse(self.cipher.encode(None))
            self.assertFalse(self.cipher.decode(None))

    def test_caesar_encoding_with_spaces(self) -> None:
        '''Test encoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = '   ' # Spaces are ignored by Caesar cipher
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(data_with_spaces)
            self.assertEqual(expected_encoded, self.enc_data)

    def test_caesar_decoding_with_spaces(self) -> None:
        '''Test decoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = '   '
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(expected_encoded)
            self.assertEqual(data_with_spaces, self.dec_data)

    def test_caesar_encoding_with_numbers_and_symbols(self) -> None:
        '''Test encoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        expected_encoded = '123!@#defDEF' # Numbers and symbols are ignored, letters shifted by 3
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(data)
            self.assertEqual(expected_encoded, self.enc_data)

    def test_caesar_decoding_with_numbers_and_symbols(self) -> None:
        '''Test decoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        encoded_data = '123!@#defDEF'
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(encoded_data)
            self.assertEqual(data, self.dec_data)

    def test_caesar_encoding_unicode(self) -> None:
        '''Test encoding a Unicode string.'''
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(self.UNICODE_DATA)
            self.assertEqual(self.UNICODE_ENC_SEQ, self.enc_data)

    def test_caesar_decoding_unicode(self) -> None:
        '''Test decoding a Unicode string.'''
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(self.UNICODE_ENC_SEQ)
            self.assertEqual(self.UNICODE_DATA, self.dec_data)

    def test_caesar_mock_interactions(self) -> None:
        '''Test interactions with mocked encoder and decoder.'''
        test_data = "Mock Data"
        mock_encoded = "Pbfn Gdwb"
        mock_decoded = "Mock Data"

        # Configure mock encoder
        self.mock_encoder.encode.return_value = True  # type: ignore
        type(self.mock_encoder).encoded_data = PropertyMock(return_value=mock_encoded)  # type: ignore

        # Configure mock decoder
        self.mock_decoder.decode.return_value = True  # type: ignore
        type(self.mock_decoder).decoded_data = PropertyMock(return_value=mock_decoded)  # type: ignore

        # Test encode interaction
        result_enc = self.mock_cipher_with_deps.encode(test_data)
        self.assertEqual(mock_encoded, result_enc)
        self.mock_encoder.encode.assert_called_once_with(test_data)  # type: ignore

        # Test decode interaction
        result_dec = self.mock_cipher_with_deps.decode(mock_encoded)
        self.assertEqual(mock_decoded, result_dec)
        self.mock_decoder.decode.assert_called_once_with(mock_encoded)  # type: ignore


if __name__ == '__main__':
    unittest.main()
