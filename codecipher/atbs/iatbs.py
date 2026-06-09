# -*- coding: UTF-8 -*-

'''
Module
    iatbs.py
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
    Defines interface IATBS for ATBS class.
'''

from abc import ABC, abstractmethod
from typing import Optional

class IATBS(ABC):
    '''
        Defines interface IATBS with methods.

        It defines:

            :attributes: None
            :methods:
                | encode - Encoding data to ATBS format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from ATBS format.
                | decode_data - Property method for getting decode data.
    '''

    @abstractmethod
    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to ATBS format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encode must be implemented.')

    @property
    @abstractmethod
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.

            :return: Encoded data
            :rtype: <Optional[str]>
        '''
        raise NotImplementedError('Property encode_data must be implemented.')

    @abstractmethod
    def decode(self, data: Optional[str]) -> bool:
        '''
            Decoding data from ATBS format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method decode must be implemented.')

    @property
    @abstractmethod
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decoded data
            :rtype: <Optional[str]>
        '''
        raise NotImplementedError('Property decode_data must be implemented.')
