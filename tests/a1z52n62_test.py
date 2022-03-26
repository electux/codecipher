# -*- coding: UTF-8 -*-

'''
 Module
     a1z52n62_test.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class A1z52N62TestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of A1z52N62.
 Execute
     python3 -m unittest -v a1z52n62_test
'''

import sys
import unittest

try:
    from codecipher.a1z52n62 import A1z52N62
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/codecipher'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__ = '1.1.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class A1z52N62TestCase(unittest.TestCase):
    '''
        Defined class A1z52N62TestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of A1z52N62.
        It defines:

            :attributes:
                | RAW_DATA - raw text data for encoding.
                | ENC_SEQ - expected encoded sequence. 
                | raw_data - object container data for encoding.
                | enc_sequence - object container for encoded sequence.
                | enc_data - encoded data.
                | dec_data - decoded data.
                | cipher - cipher object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_a1z52n62_encoding - test for base encoding a1z52n62.
                | test_a1z52n62_decoding - test for base decoding a1z52n62.
    '''

    RAW_DATA = "More Human Than Human01 Is Our Motto"
    ENC_SEQ = [
        '13', '42', '45', '32', ' ', '8', '48', '40', '28', '41', ' ',
        '20', '35', '28', '41', ' ', '8', '48', '40', '28', '41', '53',
        '54', ' ', '9', '46', ' ', '15', '48', '45', ' ', '13', '42',
        '47', '47', '42'
    ]

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data = A1z52N62TestCase.RAW_DATA
        self.enc_sequence = " - ".join(A1z52N62TestCase.ENC_SEQ)
        self.enc_data = None
        self.dec_data = None
        self.cipher = A1z52N62()

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None

    def test_a1z52n62_encoding(self) -> None:
        '''Test base encoding.'''
        self.cipher.encode(self.raw_data)  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.assertEqual(self.enc_sequence, self.enc_data)

    def test_a1z52n62_decoding(self) -> None:
        '''Test base decoding.'''
        self.cipher.encode(self.raw_data)  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.cipher.decode(self.enc_data)  # decoding data
        self.dec_data = self.cipher.decode_data  # decoded data
        self.assertEqual(self.raw_data, self.dec_data)


if __name__ == '__main__':
    unittest.main()
