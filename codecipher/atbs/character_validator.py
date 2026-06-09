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
    Defines class CharacterValidator for ATBS.
'''

from typing import Optional, Set
from codecipher.atbs.lookup_table import LOOKUP_TABLE
from .icharacter_validator import ICharacterValidator

class CharacterValidator(ICharacterValidator):
    '''
        Defines class CharacterValidator with attribute(s) and method(s).
        Creates character validator class for ATBS.

        It defines:

            :attributes:
                | __allowed_chars - Characters supported by ATBS lookup table.
            :methods:
                | __init__ - Initializes CharacterValidator constructor.
                | is_valid_char - Validates if a single character belongs to ATBS.
    '''

    def __init__(self) -> None:
        '''
            Initializes CharacterValidator constructor.
        '''
        self.__allowed_chars: Set[str] = set(LOOKUP_TABLE.keys())

    def is_valid_char(self, char: Optional[str]) -> bool:
        '''
            Validating if a character belongs strictly to ATBS set.

            :param char: Single character to validate | None
            :type char: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
        '''
        if not bool(char) or len(char) != 1:
            return False

        return char in self.__allowed_chars
