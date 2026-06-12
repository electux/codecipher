# -*- coding: UTF-8 -*-

'''
Module
    ialgorithm.py
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
    Defines class IAlgorithm for cipher algorithms.
'''

from typing import List, Optional, TypeVar, Generic
from abc import ABC, abstractmethod
from codecipher.abstracts.iconfig import IConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Generic type for algorithm configuration
ConfigT = TypeVar('ConfigT', bound=IConfig)


class IAlgorithm(ABC, Generic[ConfigT]):
    '''
        Defines interface IAlgorithm with abstract method.

        It defines:

            :attributes: None
            :methods:
                | execute - Execute chipher logic for processing data.
    '''

    @abstractmethod
    def execute(self, data: Optional[str] = None, config: Optional[ConfigT] = None) -> Optional[str]:
        '''
            Execute cipher logic for processing data.

            :param data: Data in string format which should to be processed | None
            :type data: <Optional[str]>
            :param config: Configuration parameters for cipher | None
            :type config: <Optional[IConfig]>
            :return: Processed data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        raise NotImplementedError('Method execute() must be implemented.')
