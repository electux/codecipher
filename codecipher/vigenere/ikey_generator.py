# -*- coding: UTF-8 -*-

'''
Module
    ikey_generator.py
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
    Defines interface IKeyGenerator for KeyGenerator class.
'''

from abc import ABC, abstractmethod
from typing import Optional, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IKeyGenerator(ABC):
    '''
        Defines interface IKeyGenerator with methods.

        It defines:

            :attributes: None
            :methods:
                | key - Property method for getting generated key.
                | generate_key - Generating key for algorithm.
    '''

    @property
    @abstractmethod
    def key(self) -> Optional[str]:
        '''
            Property method for getting generated key.

            :return: Generated key | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Property key must be implemented.')

    @key.setter
    @abstractmethod
    def key(self, key: Optional[str]) -> None:
        '''
            Property method for setting key.
        '''
        raise NotImplementedError('Setter key must be implemented.')

    @abstractmethod
    def generate_key(self, data_len: Optional[int]) -> bool:
        '''
            Generating key for algorithm.

            :param data_len: Length of data for which key is generated | None
            :type data_len: <Optional[int]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method generate_key must be implemented.')
