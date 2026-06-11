# -*- coding: UTF-8 -*-

'''
Module
    icharacter_validator.py
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
    Defines interface ICharacterValidator for character validators.
'''

from typing import List, Optional
from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ICharacterValidator(ABC):
    '''
        Defines interface ICharacterValidator with abstract method.

        It defines:

            :attributes: None
            :methods:
                | is_valid_char - Validates if a single character belongs to cipher charcter set.
    '''

    @abstractmethod
    def is_valid_char(self, character: Optional[str]) -> bool:
        '''
            Validates if a single character belongs to cipher charcter set.

            :param character: Single character in string format to be validated
            :type character: <Optional[str]>
            :return: True (valid) | False (invalid)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_valid_char() must be implemented.")
