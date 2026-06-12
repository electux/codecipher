# -*- coding: UTF-8 -*-

'''
Module
    encode_algorithm.py
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
    Defines class EncodeAlgorithm with default cipher ATBS implementation.
'''

from typing import List, Optional
from codecipher.abstracts import IAlgorithm, IConfig
from codecipher.atbs.config import ATBSConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class EncodeAlgorithm(IAlgorithm[IConfig]):
    '''
        Defines class EncodeAlgorithm with attribute(s) and method(s).

        It defines:

            :attributes:
                | _config - Configuration parameters for cipher ATBS.
            :methods:
                | __init__ - Initializes EncodeAlgorithm constructor.
                | encoded_data - Property method for getting encoded data.
                | encode - Execute cipher ATBS logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes EncodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher ATBS logic.

            :param data: Data in string format which should to be encoded | None
            :type data: <Optional[str]>
            :param config: Configuration for cipher | None
            :type config: <Optional[IConfig]>
            :return: Encoded data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        if not data:
            return None

        self.__config = config or ATBSConfig()

        if not self.__config:
            return None

        #def encode(
        #    self,
        #    data: Optional[str] = None,
        #    key: Optional[str] = None,
        #    shift_counter: Optional[int] = None
        #) -> bool:
        #    if bool(data):
        #        encode_list: List[str] = []
        #        for element in data:
        #            encode_list.append(LOOKUP_TABLE[element])
        #        self.__encode_data = ''.join(encode_list)
        #        return True
        #    return False

        return ""
