# -*- coding: UTF-8 -*-

'''
Module
    iencoder.py
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
    Defines interface IA1z52N62Encoder for A1z52N62Encoder class.
'''

from abc import ABC, abstractmethod
from typing import List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IA1z52N62Encoder(ABC):
    '''
        Defines interface IA1z52N62Encoder with property and method.

        It defines:

            :methods:
                | encode_data - Property methods for encode data.
                | encode - Encode data to A1z52N62 format.
    '''

    @property
    @abstractmethod
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.

            :return: Encoded data
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        raise NotImplementedError('Method encode_data must be implemented.')

    @encode_data.setter
    @abstractmethod
    def encode_data(self, encode_data: Optional[str]) -> None:
        '''
            Property method for setting encode data.

            :param encode_data: Encode data | None
            :type encode_data: <Optional[str]>
            :return: None
            :exceptions: None
        '''
        raise NotImplementedError('Method encode_data must be implemented.')

    @abstractmethod
    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to A1z52N62 format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        raise NotImplementedError('Method encode must be implemented.')
