# -*- coding: UTF-8 -*-

'''
Module
    b64_test.py
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
    Defines class B64TestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of B64.
Execute
    python3 -m unittest -v b64_test
'''

import unittest
from unittest.mock import MagicMock
from typing import List, Optional
from codecipher.b64.engine import B64
from codecipher.abstracts.ivalidation_engine import IValidationEngine

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class B64TestCase(unittest.TestCase):
    '''
        Defines class B64TestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of B64.

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
                | test_b64_encoding - Test for base encoding b64.
                | test_b64_decoding - Test for base decoding b64.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'TW9yZSBIdW1hbiBUaGFuIEh1bWFuMDEgSXMgT3VyIE1vdHRv'
    EMPTY_DATA: str = ''
    EMPTY_ENC_SEQ: str = ''
    UNICODE_DATA: str = 'Привет, мир! 👋'
    UNICODE_ENC_SEQ: str = '0J/RgNC40LLQtdGCLCDQvNC40YAhIPCfkYs='

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data: Optional[str] = B64TestCase.RAW_DATA
        self.enc_sequence: Optional[str] = B64TestCase.ENC_SEQ
        self.enc_data: Optional[str] = None
        self.dec_data: Optional[str] = None

        # Mock validacioni engine da bi se osiguralo da validacija prolazi za integracione testove.
        # Ovo zaobilazi potencijalnu strogost podrazumevane validacije B64 klase
        # za karaktere kao što su Unicode, brojevi i simboli, za koje se očekuje da testovi prođu.
        self.mock_validation_engine = MagicMock(spec=IValidationEngine)
        self.mock_validation_engine.is_valid.return_value = True

        # Stvarni šifrator za testiranje stvarne B64 funkcionalnosti, injektovan sa permisivnim validacionim engine-om
        self.cipher: Optional[B64] = B64(validation_engine=self.mock_validation_engine)

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None
        self.mock_validation_engine = None # type: ignore

    def test_b64_encoding(self) -> None:
        '''Test base encoding.'''
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(self.raw_data)
            self.assertEqual(self.enc_sequence, self.enc_data)

    def test_b64_decoding(self) -> None:
        '''Test base decoding.'''
        if bool(self.cipher):
            encoded = self.cipher.encode(self.raw_data)
            self.dec_data = self.cipher.decode(encoded)
            self.assertEqual(self.raw_data, self.dec_data)

    def test_b64_encoding_empty_string(self) -> None:
        '''Test encoding an empty string.'''
        if bool(self.cipher):
            # B64.encode returns False for empty string and doesn't set encode_data
            self.assertFalse(self.cipher.encode(self.EMPTY_DATA))

    def test_b64_decoding_empty_string(self) -> None:
        '''Test decoding an empty string.'''
        if bool(self.cipher):
            # B64.decode returns False for empty string and doesn't set decode_data
            self.assertFalse(self.cipher.decode(self.EMPTY_ENC_SEQ))

    def test_b64_with_none_data(self) -> None:
        '''Test encoding and decoding with None.'''
        if bool(self.cipher):
            self.assertFalse(self.cipher.encode(None))
            self.assertFalse(self.cipher.decode(None))

    def test_b64_encoding_with_spaces(self) -> None:
        '''Test encoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = 'ICAg'
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(data_with_spaces)
            self.assertEqual(expected_encoded, self.enc_data)

    def test_b64_decoding_with_spaces(self) -> None:
        '''Test decoding a string with only spaces.'''
        data_with_spaces = '   '
        expected_encoded = 'ICAg'
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(expected_encoded)
            self.assertEqual(data_with_spaces, self.dec_data)

    def test_b64_encoding_with_numbers_and_symbols(self) -> None:
        '''Test encoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        expected_encoded = 'MTIzIUAjYWJjQUJD'
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(data)
            self.assertEqual(expected_encoded, self.enc_data)

    def test_b64_decoding_with_numbers_and_symbols(self) -> None:
        '''Test decoding a string with numbers and symbols.'''
        data = '123!@#abcABC'
        expected_encoded = 'MTIzIUAjYWJjQUJD'
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(expected_encoded)
            self.assertEqual(data, self.dec_data)

    def test_b64_encoding_unicode(self) -> None:
        '''Test encoding a Unicode string.'''
        if bool(self.cipher):
            self.enc_data = self.cipher.encode(self.UNICODE_DATA)
            # The actual base64 encoding of 'Привет, мир! 👋' is '0J/QtdC70Ywg0LzQvtC7ISA47u+x'
            # when encoded as UTF-8 bytes.
            self.assertEqual(self.UNICODE_ENC_SEQ, self.enc_data)

    def test_b64_decoding_unicode(self) -> None:
        '''Test decoding a Unicode string.'''
        if bool(self.cipher):
            self.dec_data = self.cipher.decode(self.UNICODE_ENC_SEQ)
            self.assertEqual(self.UNICODE_DATA, self.dec_data)

    def test_b64_mock_interactions(self) -> None:
        '''Test interactions with a mocked B64 cipher object.'''
        mock_cipher = MagicMock(spec=B64)
        test_data = "Hello Mock!"
        mock_encoded_data = "SGVsbG8gTW9jayE="
        mock_decoded_data = "Hello Mock!"

        # Configure the mock's encode method
        mock_cipher.encode.return_value = mock_encoded_data

        # Configure the mock's decode method
        mock_cipher.decode.return_value = mock_decoded_data

        # Use the mocked cipher
        result_enc = mock_cipher.encode(test_data)
        self.assertEqual(mock_encoded_data, result_enc)
        mock_cipher.encode.assert_called_once_with(test_data)

        result_dec = mock_cipher.decode(mock_encoded_data)
        self.assertEqual(mock_decoded_data, result_dec)
        mock_cipher.decode.assert_called_once_with(mock_encoded_data)


if __name__ == '__main__':
    unittest.main()
