# -*- coding: UTF-8 -*-

'''
Module
    decode.py
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
    Defines class ATBSDecoder with attribute(s) and method(s).
    Creates decode class with backend API.
'''

from typing import List, Optional
from codecipher.abstracts import IDecoder
from .lookup_table import LOOKUP_TABLE

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATBSDecoder(IDecoder):
    '''
        Defines class ATBSDecoder with attribute(s) and method(s).
        Creates decode class with backend API.

        It defines:

            :attributes:
                | __decoded_data - Data decode container.
            :methods:
                | __init__ - Initializes ATBSDecoder constructor.
                | decode_data - Property methods for decode data.
                | decode - Decode data from ATBS format.
    '''

    def __init__(self) -> None:
        '''
            Initializes ATBSDecoder constructor.

            :exceptions: None
        '''
        self.__decoded_data: Optional[str] = None

    @property
    def decoded_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decode data in str format | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__decoded_data

    def decode(
        self,
        data: Optional[str] = None,
        key: Optional[str] = None,
        shift_counter: Optional[int] = None
    ) -> bool:
        '''
            Decoding data from ATBS format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :return: None
            :exceptions: None
        '''
        if bool(data):
            decode_list: List[str] = []
            for element in data:
                decode_list.append(LOOKUP_TABLE[element])
            self.__decoded_data = ''.join(decode_list)
            return True
        return False
