# -*- coding: UTF-8 -*-

'''
Module
    encoder.py
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
    Defines class A1z52N62Encoder with attribute(s) and method(s).
    Creates encode class with backend API.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from .iencoder import IA1z52N62Encoder
from .a1z52n62_config import A1z52N62Config

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class A1z52N62Encoder(IA1z52N62Encoder):
    '''
        Defines class A1z52N62Encoder with attribute(s) and method(s).
        Creates encode class with backend API.

        It defines:

            :attributes:
                | _config - Configuration for offsets and bases.
                | _encode_data - Data encode container.
            :methods:
                | encode_data - Property methods for encode data.
                | encode - Encode data to A1z52N62 format.
    '''

    _config: A1z52N62Config = field(default_factory=A1z52N62Config)
    _encode_data: Optional[str] = field(default=None, init=False)

    @property
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.

            :return: Encoded data
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._encode_data

    @encode_data.setter
    def encode_data(self, encode_data: Optional[str]) -> None:
        '''
            Property method for setting encode data.

            :param encode_data: Encode data | None
            :type encode_data: <Optional[str]>
            :return: None
            :exceptions: None
        '''
        if bool(encode_data):
            self._encode_data = encode_data

    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to A1z52N62 format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False

        if not bool(data):
            return status

        encode_list: List[str] = []
        for element in data:
            if element.isalpha():
                if element.isupper():
                    encode_list.append(
                        str(ord(element) - self._config.upper_case_offset)
                    )
                else:
                    encode_list.append(
                        str(
                            ord(element) - self._config.lower_case_offset + self._config.lower_case_base
                        )
                    )
            else:
                if element.isnumeric():
                    encode_list.append(
                        str(int(element) + self._config.numeric_base)
                    )
                else:
                    encode_list.append(element)
        self._encode_data = self._config.code_splitter.join(encode_list)
        status = True

        return status
