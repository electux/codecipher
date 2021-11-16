# -*- coding: UTF-8 -*-

'''
 Module
     lookup_table.py
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
     Defined class LookUpTable with attribute(s).
     Created lookup table class with support for encoding/decoding.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/codecipher'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__ = '1.0.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class LookUpTable:
    """
        Defined class LookUpTable with attribute(s) and method(s).
        Created lookup table class with support for encoding/decoding.
        It defines:

            :attributes:
                | ALPHA - Define alphabet for encoding/decoding.
                | NUM -  Defined numeric for encoding/decoding.
                | WHITE_SPACE - Defined white space for encoding/decoding.
                | ALPHANUM - Aggregated chars for encoding/decoding.
                | LETTER_TO_INDEX - Indexed letters for encoding/decoding.
                | INDEX_TO_LETTER - Indexed letters for encoding/decoding.
            :methods:
                | None
    """

    ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUM = '0123456789'
    WHITE_SPACE = ' '
    ALPHANUM = "".join([ALPHA, NUM, WHITE_SPACE])
    LETTER_TO_INDEX = dict(zip(ALPHANUM, range(len(ALPHANUM))))
    INDEX_TO_LETTER = dict(zip(range(len(ALPHANUM)), ALPHANUM))