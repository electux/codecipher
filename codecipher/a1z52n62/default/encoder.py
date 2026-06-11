# -*- coding: UTF-8 -*-

'''
Module
    encoder.py
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
    Defines class DefaultA1z52N62Encoder with attribute(s) and method(s).
    Creates encoder with A1z52N62 algorithm.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from codecipher.abstracts import IEncoder, IAlgorithm, IA1Z52N62Config
from .config import DefaultA1z52N62Config
from .encode_algorithm import DefaultA1z52N62EncodeAlgorithm

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class DefaultA1z52N62Encoder(IEncoder):
    '''
        Defines class DefaultA1z52N62Encoder with attribute(s) and method(s).
        Creates encoder with A1z52N62 algorithm.

        It defines:

            :attributes:
                | _config - Configuration parameters for A1z52N62 algorithm.
                | _strategy - Strategy for A1z52N62 algorithm.
                | _encoded_data - Container for encoded data.
            :methods:
                | encoded_data - Property method for getting encoded data.
                | encode - Encode data by using A1z52N62 algorithm.
    '''

    _config: IA1Z52N62Config = field(default_factory=DefaultA1z52N62Config)
    _strategy: IAlgorithm[IA1Z52N62Config] = field(default_factory=DefaultA1z52N62EncodeAlgorithm)
    _encoded_data: Optional[str] = field(default=None, init=False)

    @property
    def encoded_data(self) -> Optional[str]:
        '''
            Property method for getting encoded data.

            :return: Encoded data in str format | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._encoded_data

    def encode(
        self,
        data: Optional[str] = None,
        key: Optional[str] = None,
        shift_counter: Optional[int] = None
    ) -> bool:
        '''
            Encode data by using A1z52N62 algorithm.

            :param data: Data which should to be encoded | None
            :type data: <Optional[str]>
            :param key: Key for encoding | None (ignored for A1z52N62)
            :type key: <Optional[str]>
            :param shift_counter: Shift count for encoding | None (ignored for A1z52N62)
            :type shift_counter: <Optional[int]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not data:
            return False

        self._encoded_data = self._strategy.execute(data, self._config)

        if not self._encoded_data:
            return False

        return True
