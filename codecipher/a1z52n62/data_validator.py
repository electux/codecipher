# -*- coding: UTF-8 -*-

'''
Module
    idata_validator.py
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
    Defines interface IDataValidator for DataValidator class.
'''

from typing import List, Optional
from .idata_validator import IDataValidator
from .icharacter_validator import ICharacterValidator
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
    '''

    def __init__(self, char_validator: Optional[ICharacterValidator] = None) -> None:
        '''
            Initials DataValidator constructor.

            :exceptions: None
        '''
        self.__char_validator: ICharacterValidator = char_validator or CharacterValidator()

    def is_valid(self, data: Optional[str]) -> bool:
        '''
            Validates if data is in A1z52N62 format.

            :param data: Data which should be validated | None
            :type data: <Optional[str]>
            :return: True (if valid) | False (if invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data):
            return False

        for element in data:
            if not self.__char_validator.is_valid_char(element):
                return False
        return True
