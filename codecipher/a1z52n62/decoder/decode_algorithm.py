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
    Defines class DecodeAlgorithm with default cipher A1z52N62 implementation.
'''

from typing import List, Optional
from codecipher.abstracts import IAlgorithm, IConfig
from codecipher.a1z52n62.config import A1z52N62Config

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
                | _config - Configuration parameters for cipher A1z52N62.
            :methods:
                | __init__ - Initializes DecodeAlgorithm constructor.
                | encoded_data - Property method for getting decoded data.
                | encode - Execute cipher A1z52N62 logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes DecodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher A1z52N62 logic.

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

        self.__config = config or A1z52N62Config()

        if not self.__config:
            return None

        if not self.__config.code_splitter:
            return None

        tokens: List[str] = data.split(self.__config.code_splitter)
        decode_list: List[str] = []

        for token in tokens:

            if token.isdigit():
                val = int(token)

                # Range 1 to 26: big letters (A-Z)
                if 1 <= val <= self.__config.alphabet_size:
                    decode_list.append(chr(val + self.__config.upper_case_offset))

                # Range 27 to 52: small letters (a-z)
                elif self.__config.lower_case_base <= val <= (self.__config.lower_case_base + self.__config.alphabet_size - 1):
                    decode_list.append(chr(val - (self.__config.lower_case_base - 1) + self.__config.lower_case_offset))

                # Range 53 to 62: digits (0-9)
                elif val >= self.__config.numeric_base:
                    decode_list.append(str(val - self.__config.numeric_base))

                # Defanse step: any token out of range, append as string
                else:
                    decode_list.append(token)
            else:
                # All others (ex. space ' ', dot '.'), append without changes to decode list
                decode_list.append(token)

        # Join decoded list without splitters and spaces
        return "".join(decode_list)
