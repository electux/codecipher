# -*- coding: UTF-8 -*-

'''
Module
    idecoder.py
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
    Defines interface IDecoder for algorithm decoders.
'''

from abc import ABC, abstractmethod
from typing import Optional

class IDecoder(ABC):
    '''
        Defines interface IDecoder with method(s).

        It defines:
            :attributes: None.
            :methods:
                | decoded_data - Property method for getting decoded data.
                | decode - Decode data using decoder cipher.
    '''

    @property
    @abstractmethod
    def decoded_data(self) -> Optional[str]:
        '''
            Property method for getting decoded data.

            :return: Decoded data in string format | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method decoded_data() must be implemented.')

    @abstractmethod
    def decode(
        self,
        data: Optional[str] = None,
        key: Optional[str] = None,
        shift_counter: Optional[int] = None
    ) -> bool:
        '''
            Decode data using decoder cipher.

            :param data: Data in string format which should to be decoded | None
            :type data: <Optional[str]>
            :param key: Key in string format for process of decoding | None
            :type key: <Optional[str]>
            :param shift_counter: Shift count in integer format for process of decoding | None
            :type shift_counter: <Optional[int]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method decode() must be implemented.')
