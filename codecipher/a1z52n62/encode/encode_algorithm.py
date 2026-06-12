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
    Defines class EncodeAlgorithm with default cipher A1z52N62 implementation.
'''

from typing import List, Optional
from codecipher.abstracts.ialgorithm import IAlgorithm
from codecipher.abstracts.iconfig import IConfig
from codecipher.a1z52n62.config import A1z52N62Config

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
                | _config - Configuration parameters for cipher A1z52N62.
            :methods:
                | __init__ - Initializes EncodeAlgorithm constructor.
                | encoded_data - Property method for getting encoded data.
                | encode - Execute cipher A1z52N62 logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes EncodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher A1z52N62 logic.

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

        self.__config = config or A1z52N62Config()

        if not self.__config:
            return None

        splitter = getattr(self.__config, 'code_splitter', ' - ') or ' - '

        encode_list: List[str] = []

        for element in data:
            if element.isalpha():
                if element.isupper():
                    # 'A' -> 65 - 64 = 1.
                    encode_list.append(str(ord(element) - self.__config.upper_case_offset))
                else:
                    # lower_case_base = 27, a ord('a') - 96 = 1, 'a' -> (1 + 26 = 27).
                    encode_list.append(
                        str(ord(element) - self.__config.lower_case_offset + (self.__config.lower_case_base - 1))
                    )
            elif element.isnumeric():
                # '0' -> 0 + 53 = 53, '9' -> 9 + 53 = 62.
                encode_list.append(str(int(element) + self.__config.numeric_base))
            else:
                # All other characters (spaces, punctuation) remain unchanged.
                encode_list.append(element)

        # Join encoded list with splitters
        return splitter.join(encode_list)
