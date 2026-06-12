# -*- coding: UTF-8 -*-

'''
Module
    decode_algorithm.py
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
    Defines class DecodeAlgorithm with default cipher VERNAM implementation.
'''

from typing import List, Optional
from codecipher.abstracts import IAlgorithm, IConfig
from codecipher.vernam.config import VernamConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DecodeAlgorithm(IAlgorithm[IConfig]):
    '''
        Defines class DecodeAlgorithm with attribute(s) and method(s).

        It defines:

            :attributes:
                | _config - Configuration parameters for cipher VERNAM.
            :methods:
                | __init__ - Initializes DecodeAlgorithm constructor.
                | execute - Execute cipher VERNAM logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes DecodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher VERNAM logic.

            :param data: Data in string format which should to be decoded | None
            :type data: <Optional[str]>
            :param config: Configuration for cipher | None
            :type config: <Optional[IConfig]>
            :return: Decoded data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        if not data:
            return None

        self.__config = config or VernamConfig()

        if not self.__config:
            return None

        key: str = getattr(self.__config, 'key', 'MyVerNamKey')
        lower_case_offset: int = getattr(self.__config, 'lower_case_offset', 96)
        alphabet_size: int = getattr(self.__config, 'alphabet_size', 26)
        decode_list: List[str] = []
        key = (key * (len(data) // len(key))) + key[:len(data) % len(key)]

        for i, element in enumerate(data):

            if element.isalpha() and key[i].isalpha():
                key_code: int = ord(key[i].lower()) - lower_case_offset
                code: int = ord(element.lower()) - lower_case_offset
                ans: int = code - key_code + 1

                if ans < 1:
                    ans += alphabet_size
                if element.isupper():
                    decode_list.append(chr(ans + lower_case_offset).upper())
                else:
                    decode_list.append(chr(ans + lower_case_offset))

            else:
                decode_list.append(element)

        return ''.join(decode_list)
