# -*- coding: UTF-8 -*-

'''
Module
    data_validator.py
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
    Defines class CharacterValidator for strict chipher data validation.
'''

from typing import List, Optional, Set
from codecipher.abstracts import IDataValidator, ICharacterValidator
from .character_validator import CharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DataValidator(IDataValidator):
    '''
        Defines class DataValidator with attribute(s) and method(s).
        Creates data validator with cipher character validator.

        It defines:

            :attributes:
                | __char_validator - Validator for individual characters.
            :methods:
                | __init__ - Initializes DataValidator constructor.
                | is_valid - Validates if data belongs to cipher data set.
    '''

    def __init__(
        self,
        char_validator: Optional[ICharacterValidator] = None,
        allowed_chars: Optional[Set[str]] = None
    ) -> None:
        '''
            Initializes DataValidator constructor.

            :param char_validator: Character validator instance | None
            :type char_validator: <Optional[ICharacterValidator]>
            :param allowed_chars: Strict cipher character set | None
            :type allowed_chars: <Optional[Set[str]]>
            :exceptions: None
        '''
        self.__char_validator: ICharacterValidator = char_validator or CharacterValidator(
            allowed_chars
        )

    def is_valid(self, data: Optional[str]) -> bool:
        '''
            Validates if data belongs to cipher data set.

            :param data: Data which should to be validated | None
            :type data: <Optional[str]>
            :return: True (valid) | False (invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not data:
            return False

        return all(self.__char_validator.is_valid_char(element) for element in data)
