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
    Defines class DefaultA1z52N62Decoder with attribute(s) and method(s).
    Creates decoder with A1z52N62 algorithm.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from codecipher.abstracts import IDecoder, IAlgorithm, IA1Z52N62Config
from .config import DefaultA1z52N62Config
from .decode_algorithm import DefaultA1z52N62DecodeAlgorithm

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class DefaultA1z52N62Decoder(IDecoder):
    '''
        Defines class DefaultA1z52N62Decoder with attribute(s) and method(s).
        Creates decoder with A1z52N62 algorithm.

        It defines:

            :attributes:
                | _config - Configuration parameters for A1z52N62 algorithm.
                | _strategy - Strategy for A1z52N62 algorithm.
                | _decoded_data - Container for decoded data.
            :methods:
                | decoded_data - Property method for getting decoded data.
                | decode - Decode data by using A1z52N62 algorithm.
    '''

    _config: IA1Z52N62Config = field(default_factory=DefaultA1z52N62Config)
    _strategy: IAlgorithm[IA1Z52N62Config] = field(default_factory=DefaultA1z52N62DecodeAlgorithm)
    _decoded_data: Optional[str] = field(default=None, init=False)

    @property
    def decoded_data(self) -> Optional[str]:
        '''
            Property method for getting decoded data.

            :return: Decoded data in str format | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._decoded_data

    def decode(
        self,
        data: Optional[str] = None,
        key: Optional[str] = None,
        shift_counter: Optional[int] = None
    ) -> bool:
        '''
            Decode data by using A1z52N62 algorithm.

            :param data: Data which should to be decoded | None
            :type data: <Optional[str]>
            :param key: Key for decoding | None (ignored for A1z52N62)
            :type key: <Optional[str]>
            :param shift_counter: Shift count for decoding | None (ignored for A1z52N62)
            :type shift_counter: <Optional[int]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not data:
            return False

        self._decoded_data = self._strategy.execute(data, self._config)

        if not self._decoded_data:
            return False

        return True
