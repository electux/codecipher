# -*- coding: UTF-8 -*-

'''
Module
    default_data_validator.py
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
    Defines class DefaultCaesarDataValidator for strict CAESAR data validation.
'''

from typing import List, Optional
from codecipher.abstracts import IDataValidator, ICharacterValidator
from .default_character_validator import DefaultCaesarCharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultCaesarDataValidator(IDataValidator):
    '''
        Defines class DefaultCaesarDataValidator with attribute(s) and method(s).
        Creates data validator for CAESAR.

        It defines:

            :attributes:
                | __char_validator - Validator for individual characters.
            :methods:
                | __init__ - Initializes DefaultCaesarDataValidator constructor.
                | is_valid - Validates if data is in CAESAR format.
    '''

    def __init__(self, char_validator: Optional[ICharacterValidator] = None) -> None:
        '''
            Initializes DefaultCaesarDataValidator constructor.

            :param char_validator: Character validator instance | None
            :type char_validator: <Optional[ICharacterValidator]>
            :exceptions: None
        '''
        self.__char_validator: ICharacterValidator = char_validator or DefaultCaesarCharacterValidator()

    def is_valid(self, data: Optional[str]) -> bool:
        '''
            Validating if data is in CAESAR format.

            :param data: Data which should be validated | None
            :type data: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data):
            return False

        return all(self.__char_validator.is_valid_char(element) for element in data)
