# -*- coding: UTF-8 -*-

'''
 Module
     vernam_test.py
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
     Defined class VernamTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of Vernam.
 Execute
     python3 -m unittest -v vernam_test
'''

import sys
import unittest

try:
    from codecipher.vernam import Vernam
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/codecipher'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__ = '1.2.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class VernamTestCase(unittest.TestCase):
    '''
        Defined class VernamTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of Vernam.
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
                | test_vernam_encoding - test for base encoding vernam.
                | test_vernam_decoding - test for base decoding vernam.
    '''

    RAW_DATA = "More Human Than Human01 Is Our Motto"
    ENC_SEQ = "Doeh Tlmnq Fyaa Vgdaa01 Zs Rid Mbwha"

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.raw_data = VernamTestCase.RAW_DATA
        self.enc_sequence = VernamTestCase.ENC_SEQ
        self.enc_data = None
        self.dec_data = None
        self.cipher = Vernam()

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None

    def test_vernam_encoding(self) -> None:
        '''Test base encoding.'''
        self.cipher.encode(
            self.raw_data, "randomrandomrandom"
        )  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.assertEqual(self.enc_sequence, self.enc_data)

    def test_vernam_decoding(self) -> None:
        '''Test base decoding.'''
        self.cipher.encode(
            self.raw_data, "randomrandomrandom"
        )  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.cipher.decode(
            self.enc_data, "randomrandomrandom"
        )  # decoding data
        self.dec_data = self.cipher.decode_data  # decoded data
        self.assertEqual(self.raw_data, self.dec_data)


if __name__ == '__main__':
    unittest.main()
