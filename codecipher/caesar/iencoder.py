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
    Defines interface IEncoder with attribute(s) and method(s).
    Interface for Caesar Encoder.
'''

from abc import ABC, abstractmethod
from typing import Optional

class IEncoder(ABC):
    '''
        Defines interface IEncoder with attribute(s) and method(s).
        Interface for Caesar Encoder.

        It defines:
            :attributes:
                | None.
            :methods:
                | encode_data - Property method for getting encoded data.
                | encode - Encode data using Caesar cipher.
    '''

    @property
    @abstractmethod
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encoded data.

            :return: Encoded data | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encode_data() is not implemented')

    @abstractmethod
    def encode(self, data: Optional[str], shift_counter: Optional[int]) -> bool:
        '''
            Encode data using Caesar cipher.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :param shift_counter: Defining the shift count | None
            :type shift_counter: <Optional[int]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encode() is not implemented')
