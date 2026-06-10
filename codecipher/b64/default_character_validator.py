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
    Defines class DefaultB64CharacterValidator for strict B64 character validation.
'''

from typing import Optional, Set, List
from string import ascii_uppercase, ascii_lowercase, digits
from codecipher.abstracts import ICharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultB64CharacterValidator(ICharacterValidator):
    '''
        Defines class DefaultB64CharacterValidator with attribute(s) and method(s).
        Creates character validator class for B64.

        It defines:

            :attributes:
                | __allowed_chars - Strict ASCII alphanumeric character B64 set.
            :methods:
                | __init__ - Initializes DefaultB64CharacterValidator constructor.
                | is_valid_char - Validates if a single character belongs to B64.
    '''

    def __init__(self) -> None:
        '''
            Initializes DefaultB64CharacterValidator constructor.
        '''
        self.__allowed_chars: Set[str] = set(ascii_uppercase + ascii_lowercase + digits + '+/=' )

    def is_valid_char(self, char: Optional[str]) -> bool:
        '''
            Validating if a character belongs strictly to B64 set.

            :param char: Single character to validate | None
            :type char: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
        '''
        if not bool(char) or len(char) != 1:
            return False

        return char in self.__allowed_chars
