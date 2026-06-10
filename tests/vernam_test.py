# -*- coding: UTF-8 -*-

'''
Module
    vernam_test.py
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
    Defines class VernamTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Vernam.
Execute
    python3 -m unittest -v vernam_test
'''

import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.abstracts import IValidationEngine
from codecipher.vernam import Vernam, IEncoder, IDecoder

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class VernamTestCase(unittest.TestCase):
    '''
        Defines class VernamTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Vernam.

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
                | test_vernam_encoding - Test for base encoding vernam.
                | test_vernam_decoding - Test for base decoding vernam.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'Doeh Tlmnq Fyaa Vgdaa01 Zs Rid Mbwha' # Example with key 'randomrandomrandom'
    EMPTY_DATA: str = ''
    EMPTY_ENC_SEQ: str = ''
    UNICODE_DATA: str = 'Привет, мир! 👋'
    UNICODE_ENC_SEQ: str = 'Привет, мир! 👋' # Vernam passes non-alpha chars through, but validation will fail
    KEY: str = 'randomrandomrandom'

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = VernamTestCase.RAW_DATA
        self.enc_sequence: Optional[str] = VernamTestCase.ENC_SEQ
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None
        self.key: str = VernamTestCase.KEY

        # Mock dependencies for the base tests
        self.mock_encoder = MagicMock(spec=IEncoder)
        self.mock_decoder = MagicMock(spec=IDecoder)
        self.mock_validation_engine = MagicMock(spec=IValidationEngine)

        # Configure default mock behavior
        self.mock_encoder.encode.return_value = True
        type(self.mock_encoder).encode_data = PropertyMock(return_value=self.enc_sequence)

        self.mock_decoder.decode.return_value = True
        type(self.mock_decoder).decode_data = PropertyMock(return_value=self.raw_data)

        self.mock_validation_engine.is_valid.return_value = True # Default to valid

        # Initialize Vernam with mocked dependencies
        self.cipher: Vernam = Vernam(
            validation_engine=self.mock_validation_engine,
            encoder=self.mock_encoder,
            decoder=self.mock_decoder
        )

        # Real cipher for direct testing without mocks
        self.real_cipher: Vernam = Vernam(validation_engine=self.mock_validation_engine)

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None # type: ignore
        self.real_cipher = None # type: ignore
        self.mock_encoder = None # type: ignore
        self.mock_decoder = None # type: ignore
        self.mock_validation_engine = None # type: ignore

    def test_vernam_encoding(self) -> None:
        '''Test base encoding with real cipher.'''
        if bool(self.real_cipher):
            result = self.real_cipher.encode(self.raw_data, self.key)
            self.assertTrue(result)
            self.enc_data = self.real_cipher.encode_data
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_vernam_decoding(self) -> None:
        '''Test base decoding with real cipher.'''
        if bool(self.real_cipher):
            # First encode to get the encoded data
            self.real_cipher.encode(self.raw_data, self.key)
            self.enc_data = self.real_cipher.encode_data

            # Then decode
            result = self.real_cipher.decode(self.enc_data, self.key)
            self.assertTrue(result)
            self.dec_data = self.real_cipher.decode_data
            self.assertEqual(self.raw_data, self.dec_data)

    def test_vernam_encoding_empty_string(self) -> None:
        '''Test encoding an empty string.'''
        if bool(self.real_cipher):
            result = self.real_cipher.encode(self.EMPTY_DATA, self.key)
            self.assertFalse(result)
            self.enc_data = self.real_cipher.encode_data
            self.assertIsNone(self.enc_data)

    def test_vernam_decoding_empty_string(self) -> None:
        '''Test decoding an empty string.'''
        if bool(self.real_cipher):
            result = self.real_cipher.decode(self.EMPTY_ENC_SEQ, self.key)
            self.assertFalse(result)
            self.dec_data = self.real_cipher.decode_data
            self.assertIsNone(self.dec_data)

    def test_vernam_with_none_data(self) -> None:
        '''Test encoding and decoding with None data.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(None, self.key))
            self.assertFalse(self.real_cipher.decode(None, self.key))

    def test_vernam_with_none_key(self) -> None:
        '''Test encoding and decoding with None key.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(self.raw_data, None))
            self.assertFalse(self.real_cipher.decode(self.enc_sequence, None))

    def test_vernam_encoding_with_spaces(self) -> None:
        '''Test encoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = '   ' # Vernam passes non-alpha chars through
        if bool(self.real_cipher):
            result = self.real_cipher.encode(data_with_spaces, self.key)
            self.assertTrue(result)
            self.enc_data = self.real_cipher.encode_data
            self.assertEqual(expected_encoded, self.enc_data)

    def test_vernam_decoding_with_spaces(self) -> None:
        '''Test decoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = '   '
        if bool(self.real_cipher):
            result = self.real_cipher.decode(expected_encoded, self.key)
            self.assertTrue(result)
            self.dec_data = self.real_cipher.decode_data
            self.assertEqual(data_with_spaces, self.dec_data)

    def test_vernam_encoding_with_numbers_and_symbols(self) -> None:
        '''Test encoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        # Key 'randomrandomrandom'
        # Indices 0-5 are symbols, key is still consumed.
        # Index 6: 'a' + 'r' (key[6]), Index 7: 'b' + 'a' (key[7]), etc.
        expected_encoded = '123!@#rbpDPO'
        if bool(self.real_cipher):
            result = self.real_cipher.encode(data, self.key)
            self.assertTrue(result)
            self.enc_data = self.real_cipher.encode_data
            self.assertEqual(expected_encoded, self.enc_data)

    def test_vernam_decoding_with_numbers_and_symbols(self) -> None:
        '''Test decoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        encoded_data = '123!@#rbpDPO'
        if bool(self.real_cipher):
            result = self.real_cipher.decode(encoded_data, self.key)
            self.assertTrue(result)
            self.dec_data = self.real_cipher.decode_data
            self.assertEqual(data, self.dec_data)

    def test_vernam_encoding_unicode_fails_validation(self) -> None:
        '''Test encoding a Unicode string (should fail validation).'''
        cipher = Vernam()
        if bool(cipher):
            # Default CharacterValidator checks for ASCII, so Unicode should fail
            result = cipher.encode(self.UNICODE_DATA, self.key)
            self.assertFalse(result)
            self.assertIsNone(cipher.encode_data)

    def test_vernam_decoding_unicode_fails_validation(self) -> None:
        '''Test decoding a Unicode string (should fail validation).'''
        cipher = Vernam()
        if bool(cipher):
            # Default CharacterValidator checks for ASCII, so Unicode should fail
            result = cipher.decode(self.UNICODE_ENC_SEQ, self.key)
            self.assertFalse(result)
            self.assertIsNone(cipher.decode_data)

    def test_encode_with_validation_failure(self) -> None:
        '''Testing encode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False  # type: ignore
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertFalse(result)
        # is_valid should be called for data and then for key
        self.mock_validation_engine.is_valid.assert_any_call(self.raw_data)  # type: ignore
        self.mock_encoder.encode.assert_not_called()  # type: ignore

    def test_decode_with_validation_failure(self) -> None:
        '''Testing decode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False  # type: ignore
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertFalse(result)
        # is_valid should be called for data and then for key
        self.mock_validation_engine.is_valid.assert_any_call(self.enc_sequence)  # type: ignore
        self.mock_decoder.decode.assert_not_called()  # type: ignore

    def test_encode_delegation(self) -> None:
        '''Testing encode delegation to internal encoder.'''
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertTrue(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.raw_data)  # type: ignore
        self.mock_validation_engine.is_valid.assert_called_with(self.key)  # type: ignore
        self.mock_encoder.encode.assert_called_once_with(self.raw_data, self.key)  # type: ignore
        self.assertEqual(self.enc_sequence, self.cipher.encode_data)

    def test_decode_delegation(self) -> None:
        '''Testing decode delegation to internal decoder.'''
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertTrue(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.enc_sequence)  # type: ignore
        self.mock_validation_engine.is_valid.assert_called_with(self.key)  # type: ignore
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence, self.key)  # type: ignore
        self.assertEqual(self.raw_data, self.cipher.decode_data)

    def test_encode_with_encoder_failure(self) -> None:
        '''Testing encode when internal encoder fails.'''
        self.mock_encoder.encode.return_value = False  # type: ignore
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertFalse(result)
        self.mock_encoder.encode.assert_called_once_with(self.raw_data, self.key)  # type: ignore

    def test_decode_with_decoder_failure(self) -> None:
        '''Testing decode when internal decoder fails.'''
        self.mock_decoder.decode.return_value = False  # type: ignore
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertFalse(result)
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence, self.key)  # type: ignore


if __name__ == '__main__':
    unittest.main()
