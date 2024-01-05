# -*- coding: UTF-8 -*-

'''
Module
    vigenere_test.py
Copyright
    Copyright (C) 2021 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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

import sys
import unittest
from typing import List

try:
    from codecipher.vigenere import Vigenere
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__ = '1.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


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
                | cipher - Cipher object.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_vigenere_encoding - Test for base encoding vigenere.
                | test_vigenere_decoding - Test for base decoding vigenere.
    '''

    RAW_DATA: str = 'More Human Than Human01 Is Our Motto'
    ENC_SEQ: str = 'bbaWG7h6SUzG1SUzud4HNNKReSXxbYzz8a0O'

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data = VigenereTestCase.RAW_DATA
        self.enc_sequence = VigenereTestCase.ENC_SEQ
        self.enc_data = None
        self.dec_data = None
        self.cipher = Vigenere()
        self.cipher.data_len = len(self.raw_data)
        self.cipher.key = 'AYUSH'
        self.cipher.generate_key()

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None

    def test_vigenere_encoding(self) -> None:
        '''Test base encoding.'''
        self.cipher.encode(self.raw_data, self.cipher.key)
        self.enc_data = self.cipher.encode_data
        self.assertEqual(self.enc_sequence, self.enc_data)

    def test_vigenere_decoding(self) -> None:
        '''Test base decoding.'''
        self.cipher.encode(self.raw_data, self.cipher.key)
        self.enc_data = self.cipher.encode_data
        self.cipher.decode(self.enc_data, self.cipher.key)
        self.dec_data = self.cipher.decode_data
        self.assertEqual(self.raw_data, self.dec_data)


if __name__ == '__main__':
    unittest.main()
