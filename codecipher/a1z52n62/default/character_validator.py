# -*- coding: UTF-8 -*-

'''
Module
    default_character_validator.py
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
    Defines class DefaultA1Z52N62CharacterValidator for strict A1z52N62 character validation.
'''

from typing import List, Optional, Set
from string import ascii_lowercase, ascii_uppercase, digits
from codecipher.abstracts import ICharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultA1Z52N62CharacterValidator(ICharacterValidator):
    '''
        Defines class DefaultA1Z52N62CharacterValidator with attribute(s) and method(s).
        Creates character validator for A1z52N62.

        It defines:

            :attributes:
                | __allowed_chars - Strict ASCII alphanumeric character set (optional space).
            :methods:
                | __init__ - Initializes DefaultA1Z52N62CharacterValidator constructor.
                | is_valid_char - Validates if a single character belongs to A1z52N62.
    '''

    def __init__(self, allow_space: bool = False) -> None:
        '''
            Initializes DefaultA1Z52N62CharacterValidator constructor.

            :param allow_space: Whether to allow space character | False
            :type allow_space: <bool>
            :exceptions: None
        '''
        self.__allowed_chars: Set[str] = set(ascii_lowercase + ascii_uppercase + digits) 

        if allow_space:
            self.__allowed_chars.add(' ')

    def is_valid_char(self, char: Optional[str]) -> bool:
        '''
            Validates if a single character belongs to A1z52N62.

            :param char: Single character to validate | None
            :type char: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not char or len(char) != 1:
            return False

        return char in self.__allowed_chars
