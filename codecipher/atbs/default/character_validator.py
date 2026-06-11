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
    Defines class DefaultATBSCharacterValidator for strict ATBS character validation.
'''

from typing import Optional, Set
from codecipher.abstracts import ICharacterValidator
from .lookup_table import LOOKUP_TABLE


class DefaultATBSCharacterValidator(ICharacterValidator):
    '''
        Defines class DefaultATBSCharacterValidator with attribute(s) and method(s).
        Creates character validator class for ATBS.

        It defines:

            :attributes:
                | __allowed_chars - Strict ASCII alphanumeric character set (ATBS lookup table).
            :methods:
                | __init__ - Initializes DefaultATBSCharacterValidator constructor.
                | is_valid_char - Validates if a single character belongs to ATBS.
    '''

    def __init__(self) -> None:
        '''
            Initializes DefaultATBSCharacterValidator constructor.
        '''
        self.__allowed_chars: Set[str] = set(LOOKUP_TABLE.keys())

    def is_valid_char(self, char: Optional[str]) -> bool:
        '''
            Validates if a single character belongs to ATBS.

            :param char: Single character to validate | None
            :type char: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
        '''
        if not bool(char) or len(char) != 1:
            return False

        return char in self.__allowed_chars
