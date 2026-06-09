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
    Defines interface IATBSDecoder for ATBSDecode class.
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


class IATBSDecoder(ABC):
    '''
        Defines interface IATBSDecoder with methods.

        It defines:

            :attributes: None
            :methods:
                | decode_data - Property method for getting decode data.
                | decode - Decoding data from ATBS format.
    '''

    @property
    @abstractmethod
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decoded data | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Property decode_data must be implemented.')

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
