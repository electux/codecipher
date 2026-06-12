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
    Creates class encoder with cipher B64 logic.
'''

from dataclasses import dataclass, field
from typing import List, Optional
from codecipher.abstracts.iencoder import IEncoder
from codecipher.abstracts.ialgorithm import IAlgorithm
from codecipher.abstracts.iconfig import IConfig
from codecipher.b64.config import B64Config
from codecipher.b64.encode.encode_algorithm import EncodeAlgorithm

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class Encoder(IEncoder):
    '''
        Defines class Encoder with attribute(s) and method(s).

        It defines:

            :attributes:
                | _config - Configuration parameters for cipher B64 logic.
                | _strategy - Strategy for cipher B64 logic.
                | _encoded_data - Container for encoded data.
            :methods:
                | encoded_data - Property method for getting encoded data.
                | encode - Encode data by cipher B64 logic.
    '''

    _config: IConfig = field(default_factory=B64Config)
    _strategy: IAlgorithm[IConfig] = field(default_factory=EncodeAlgorithm)
    _encoded_data: Optional[str] = field(default=None, init=False)

    @property
    def encoded_data(self) -> Optional[str]:
        '''
            Property method for getting encoded data.

            :return: Encoded data in string format | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._encoded_data

    def encode(self, data: Optional[str] = None) -> bool:
        '''
            Encode data by cipher B64 logic.

            :param data: Data in string format which should to be encoded | None
            :type data: <Optional[str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not data:
            return False

        # Execute cipher B64 logic with configuration parameters
        self._encoded_data = self._strategy.execute(data, self._config)

        if not self._encoded_data:
            return False

        return True
