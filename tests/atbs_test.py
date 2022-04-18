# -*- coding: UTF-8 -*-

'''
 Module
     atbs_test.py
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
     Defined class AlephTawBetShinTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of AlephTawBetShin.
 Execute
     python3 -m unittest -v atbs_test
'''

import sys
import unittest

try:
    from codecipher.atbs import AlephTawBetShin
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/codecipher'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/codecipher/blob/dev/LICENSE'
__version__ = '1.3.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class AlephTawBetShinTestCase(unittest.TestCase):
    '''
        Defined class AlephTawBetShinTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of AlephTawBetShin.
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
                | test_atbs_encoding - test for base encoding atbs.
                | test_atbs_decoding - test for base decoding atbs.
    '''

    RAW_DATA = "More Human Than Human01 Is Our Motto"
    ENC_SEQ = "Nliv Sfnzm Gszm Sfnzm98 Rh Lfi Nlggl"

    def setUp(self) -> None:
        '''Call before test case.'''
        self.raw_data = AlephTawBetShinTestCase.RAW_DATA
        self.enc_sequence = AlephTawBetShinTestCase.ENC_SEQ
        self.enc_data = None
        self.dec_data = None
        self.cipher = AlephTawBetShin()

    def tearDown(self) -> None:
        '''Call after test case.'''
        self.raw_data = None
        self.enc_data = None
        self.dec_data = None
        self.cipher = None

    def test_atbs_encoding(self) -> None:
        '''Test base info.'''
        self.cipher.encode(self.raw_data)  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.assertEqual(self.enc_sequence, self.enc_data)

    def test_atbs_decoding(self) -> None:
        '''Test base info.'''
        self.cipher.encode(self.raw_data)  # encoding data
        self.enc_data = self.cipher.encode_data  # encoded data
        self.cipher.decode(self.enc_data)  # decoding data
        self.dec_data = self.cipher.decode_data  # decoded data
        self.assertEqual(self.raw_data, self.dec_data)


if __name__ == '__main__':
    unittest.main()
