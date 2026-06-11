# -*- coding: UTF-8 -*-

'''
Module
    icipher_engine.py
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
    Defines interface ICipherEngine for cipher class with encoders and decoders.
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


class ICipherEngine(ABC):
    '''
        Defines interface ICipherEngine with method(s).

        It defines:

            :attributes: None
            :methods:
                | encode - Encoding data to CIPHER format.
                | decode - Decoding data from CIPHER format.
    '''

    @abstractmethod
    def encode(self, data: Optional[str]) -> Optional[str]:
        '''
            Encoding data to CIPHER format.

            :param data: Data which should to be encoded | None
            :type data: <Optional[str]>
            :return: Encoded data (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method encode() must be implemented.')

    @abstractmethod
    def decode(self, data: Optional[str]) -> Optional[str]:
        '''
            Decoding data from CIPHER format.

            :param data: Data which should to be decoded | None
            :type data: <Optional[str]>
            :return: Decoded data (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError('Method decode() must be implemented.')
