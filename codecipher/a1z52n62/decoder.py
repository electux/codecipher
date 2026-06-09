# -*- coding: UTF-8 -*-

'''
Module
    decoder.py
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
    Defines class A1z52N62Decoder with attribute(s) and method(s).
    Creates decode class with backend API.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from .idecoder import IA1z52N62Decoder
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
class A1z52N62Decoder(IA1z52N62Decoder):
    '''
        Defines class A1z52N62Decoder with attribute(s) and method(s).
        Creates decode class with backend API.

        It defines:

            :attributes:
                | _config - Configuration for offsets and bases.
                | _decode_data - Data decode container.
            :methods:
                | decode_data - Property methods for decode data.
                | decode - Decode data from A1z52N62 format.
    '''

    _config: A1z52N62Config = field(default_factory=A1z52N62Config)
    _decode_data: Optional[str] = field(default=None, init=False)

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decode data in str format | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._decode_data

    @decode_data.setter
    def decode_data(self, decode_data: Optional[str]) -> None:
        '''
            Property method for setting decode data.

            :param decode_data: Decoded data | None
            :type decode_data: <Optional[str]>
            :return: None
            :exceptions: None
        '''
        if bool(decode_data):
            self._decode_data = decode_data

    def decode(self, data: Optional[str]) -> bool:
        '''
            Decoding data from A1z52N62 format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False

        if not bool(data):
            return status

        decode_list: List[str] = []
        for element in data.split(self._config.code_splitter):
            if element.isnumeric():
                val = int(element)
                if val < self._config.numeric_base:
                    if val <= self._config.alphabet_size:
                        decode_list.append(
                            chr(val + self._config.upper_case_offset)
                        )
                    else:
                        decode_list.append(
                            chr(val + self._config.lower_case_offset - self._config.lower_case_base)
                        )
                else:
                    decode_list.append(str(val - self._config.numeric_base))
            else:
                decode_list.append(element)
        self._decode_data = ''.join(decode_list)
        status = True

        return status
