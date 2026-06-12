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
    Defines interface IEncoder for algorithm encoders.
'''

from abc import ABC, abstractmethod
from typing import Optional

class IEncoder(ABC):
    '''
        Defines interface IEncoder with method(s).

        It defines:
            :attributes: None
            :methods:
                | encoded_data - Property method for getting encoded data.
                | encode - Encode data using encoder cipher.
    '''

    @property
    @abstractmethod
    def encoded_data(self) -> Optional[str]:
        '''
            Property method for getting encoded data.

            :return: Encoded data in str format | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encoded_data() must be implemented.')

    @abstractmethod
    def encode(self, data: Optional[str] = None) -> bool:
        '''
            Encode data using encoder cipher.

            :param data: Data in string format which should to be encoded | None
            :type data: <Optional[str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encode() must be implemented.')
