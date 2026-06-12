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
    Defines class EncodeAlgorithm with default cipher VIGENERE implementation.
'''

from typing import Dict, List, Optional, Set
from codecipher.abstracts import IAlgorithm, IConfig
from codecipher.vigenere.config import VigenereConfig

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
                | _config - Configuration parameters for cipher VIGENERE.
            :methods:
                | __init__ - Initializes EncodeAlgorithm constructor.
                | _split_data_encode - Splitting data for process of encoding.
                | execute - Execute cipher VIGENERE logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes EncodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def _split_data_encode(self, data_to_encode: Optional[str], key: Optional[str]) -> List[str]:
        '''
            Splitting data for process of encoding.

            :param data_to_encode: Data which should to be encoded | None
            :type data_to_encode: <Optional[str]>
            :param key: Key for process of encoding | None
            :type key: <Optional[str]>
            :return: List with data for process of encoding
            :rtype: <List[str]>
            :exceptions: None
        '''
        elements: List[str] = []

        if data_to_encode and key:
            for i in range(0, len(data_to_encode), len(key)):
                elements.append(data_to_encode[i: i + len(key)])

        return elements

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher VIGENERE logic.

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

        self.__config = config or VigenereConfig()

        if not self.__config:
            return None

        key: str = getattr(self.__config, 'key', 'MyVigenereKey')
        allowed_chars: Optional[Set[str]] = getattr(self.__config, 'allowed_chars')

        if not allowed_chars:
            return None

        alphanum: str = ''.join(allowed_chars)
        letter_to_index: Dict[str, int] = dict(zip(alphanum, range(len(alphanum))))
        index_to_letter: Dict[int, str] = dict(zip(range(len(alphanum)), alphanum))
        encode_list: List[str] = []

        for element in self._split_data_encode(data, key):
            for index, letter in enumerate(element):
                process_index: int = (letter_to_index[letter] + letter_to_index[key[index]]) % len(alphanum)
                encode_list.append(index_to_letter[process_index])

        return ''.join(encode_list)
