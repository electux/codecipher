# -*- coding: UTF-8 -*-

'''
Module
    vigenere_test.py
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
    Defines class VigenereTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Vigenere.
Execute
    python3 -m unittest -v vigenere_test
'''

import unittest
from unittest.mock import MagicMock, PropertyMock
from typing import List, Optional
from codecipher.abstracts import IValidationEngine
from codecipher.vigenere import Vigenere, IEncoder, IDecoder, IKeyGenerator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class VigenereTestCase(unittest.TestCase):
    '''
        Defines class VigenereTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Vigenere.

        It defines:

            :attributes:
                | RAW_DATA - Raw text data for encoding.
                | ENC_SEQ - Expected encoded sequence.
                | raw_data - Object container data for encoding.
                | enc_sequence - Object container for encoded sequence.
                | enc_data - Encoded data.
                | dec_data - Decoded data.
                | key - Key for encoding/decoding.
                | cipher - Cipher object with mocked dependencies.
                | real_cipher - Real cipher object for integration testing.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_vigenere_encoding - Test for base encoding vigenere.
                | test_vigenere_decoding - Test for base decoding vigenere.
                | test_vigenere_with_none_data - Test for encoding/decoding with None data.
                | test_vigenere_with_none_key - Test for encoding/decoding with None key.
                | test_vigenere_empty_string - Test for encoding/decoding with empty strings.
                | test_encode_with_validation_failure - Test for encoding with validation failure.
                | test_decode_with_validation_failure - Test for decoding with validation failure.
                | test_encode_delegation - Test for encoding delegation to components.
                | test_decode_delegation - Test for decoding delegation to components.
                | test_encode_with_encoder_failure - Test for encoding with encoder failure.
                | test_decode_with_decoder_failure - Test for decoding with decoder failure.
                | test_encode_with_key_gen_failure - Test for encoding with key generation failure.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'bbaWG7h6SUzG1SUzud4HNNKReSXxbYzz8a0O'
    KEY: str = 'AYUSH'

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = VigenereTestCase.RAW_DATA
        self.enc_sequence: Optional[str] = VigenereTestCase.ENC_SEQ
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None
        self.key: str = VigenereTestCase.KEY

        # Mock dependencies for the unit tests
        self.mock_encoder = MagicMock(spec=IEncoder)
        self.mock_decoder = MagicMock(spec=IDecoder)
        self.mock_key_generator = MagicMock(spec=IKeyGenerator)
        self.mock_validation_engine = MagicMock(spec=IValidationEngine)

        # Configure default mock behavior
        self.mock_encoder.encode.return_value = True
        type(self.mock_encoder).encode_data = PropertyMock(return_value=self.enc_sequence)

        self.mock_decoder.decode.return_value = True
        type(self.mock_decoder).decode_data = PropertyMock(return_value=self.raw_data)

        self.mock_key_generator.generate_key.return_value = True
        type(self.mock_key_generator).key = PropertyMock(return_value=self.key)

        self.mock_validation_engine.is_valid.return_value = True

        # Initialize Vigenere with mocked dependencies
        self.cipher: Vigenere = Vigenere(
            validation_engine=self.mock_validation_engine,
            encoder=self.mock_encoder,
            decoder=self.mock_decoder,
            key_generator=self.mock_key_generator
        )

        # Real cipher for integration testing
        self.real_cipher: Vigenere = Vigenere()

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None  # type: ignore
        self.real_cipher = None  # type: ignore
        self.mock_encoder = None  # type: ignore
        self.mock_decoder = None  # type: ignore
        self.mock_key_generator = None  # type: ignore
        self.mock_validation_engine = None  # type: ignore

    def test_vigenere_encoding(self) -> None:
        '''Test base encoding with real cipher.'''
        if bool(self.real_cipher):
            result = self.real_cipher.encode(self.raw_data, self.key)
            self.assertTrue(result)
            self.enc_data = self.real_cipher.encode_data
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_vigenere_decoding(self) -> None:
        '''Test base decoding with real cipher.'''
        if bool(self.real_cipher):
            self.real_cipher.encode(self.raw_data, self.key)
            self.enc_data = self.real_cipher.encode_data
            result = self.real_cipher.decode(self.enc_data, self.key)
            self.assertTrue(result)
            self.dec_data = self.real_cipher.decode_data
            self.assertEqual(self.raw_data, self.dec_data)

    def test_vigenere_with_none_data(self) -> None:
        '''Test encoding and decoding with None data.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(None, self.key))
            self.assertFalse(self.real_cipher.decode(None, self.key))

    def test_vigenere_with_none_key(self) -> None:
        '''Test encoding and decoding with None key.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode(self.raw_data, None))
            self.assertFalse(self.real_cipher.decode(self.enc_sequence, None))

    def test_vigenere_empty_string(self) -> None:
        '''Test encoding and decoding with empty strings.'''
        if bool(self.real_cipher):
            self.assertFalse(self.real_cipher.encode('', self.key))
            self.assertFalse(self.real_cipher.decode('', self.key))

    def test_encode_with_validation_failure(self) -> None:
        '''Testing encode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False  #type: ignore
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertFalse(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.raw_data)  #type: ignore
        self.mock_encoder.encode.assert_not_called()  #type: ignore

    def test_decode_with_validation_failure(self) -> None:
        '''Testing decode when validation engine fails.'''
        self.mock_validation_engine.is_valid.return_value = False  #type: ignore
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertFalse(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.enc_sequence)  #type: ignore
        self.mock_decoder.decode.assert_not_called()  #type: ignore

    def test_encode_delegation(self) -> None:
        '''Testing encode delegation to internal components.'''
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertTrue(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.raw_data)  #type: ignore
        self.mock_key_generator.generate_key.assert_called_once_with(len(self.raw_data))  #type: ignore
        self.mock_encoder.encode.assert_called_once_with(self.raw_data, self.key)  #type: ignore
        self.assertEqual(self.enc_sequence, self.cipher.encode_data)

    def test_decode_delegation(self) -> None:
        '''Testing decode delegation to internal components.'''
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertTrue(result)
        self.mock_validation_engine.is_valid.assert_any_call(self.enc_sequence)  #type: ignore
        self.mock_key_generator.generate_key.assert_called_once_with(len(self.enc_sequence))  #type: ignore
        self.mock_decoder.decode.assert_called_once_with(self.enc_sequence, self.key)  #type: ignore
        self.assertEqual(self.raw_data, self.cipher.decode_data)

    def test_encode_with_encoder_failure(self) -> None:
        '''Testing encode when internal encoder fails.'''
        self.mock_encoder.encode.return_value = False  #type: ignore
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertFalse(result)
        self.mock_encoder.encode.assert_called_once()  #type: ignore

    def test_decode_with_decoder_failure(self) -> None:
        '''Testing decode when internal decoder fails.'''
        self.mock_decoder.decode.return_value = False  #type: ignore
        result = self.cipher.decode(self.enc_sequence, self.key)
        self.assertFalse(result)
        self.mock_decoder.decode.assert_called_once()  #type: ignore

    def test_encode_with_key_gen_failure(self) -> None:
        '''Testing encode when key generator fails.'''
        self.mock_key_generator.generate_key.return_value = False  #type: ignore
        result = self.cipher.encode(self.raw_data, self.key)
        self.assertFalse(result)
        self.mock_key_generator.generate_key.assert_called_once()  #type: ignore
        self.mock_encoder.encode.assert_not_called()  #type: ignore


if __name__ == '__main__':
    unittest.main()
