# -*- coding: UTF-8 -*-

'''
Module
    character_validator.py
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
    Defines class CharacterValidator for strict chipher character validation.
'''

from typing import List, Optional, Set
from codecipher.abstracts import ICharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CharacterValidator(ICharacterValidator):
    '''
        Defines class CharacterValidator with attribute(s) and method(s).
        Creates character validator with cipher character set.

        It defines:

            :attributes:
                | __allowed_chars - Strict cipher character set.
            :methods:
                | __init__ - Initializes CharacterValidator constructor.
                | is_valid_char - Validates if a single character belongs to cipher charcter set.
    '''

    def __init__(self, allowed_chars: Optional[Set[str]] = None) -> None:
        '''
            Initializes CharacterValidator constructor.

            :param allowed_chars: Strict cipher character set.
            :type allowed_chars: <Optional[Set[str]]>
            :param allow_space: Whether to allow space character | False
            :type allow_space: <bool>
            :exceptions: None
        '''
        self.__allowed_chars: Optional[Set[str]] = allowed_chars

    def is_valid_char(self, character: Optional[str]) -> bool:
        '''
            Validates if a single character belongs to cipher charcter set.

            :param character: Single character in string format to be validated
            :type character: <Optional[str]>
            :return: True (valid) | False (invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not self.__allowed_chars or not character or len(character) != 1:
            return False

        return character in self.__allowed_chars
