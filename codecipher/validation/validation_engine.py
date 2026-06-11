# -*- coding: UTF-8 -*-

'''
Module
    validation_engine.py
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
    Defines class ValidationEngine for managing multiple cipher data validators.
'''

from typing import List, Optional, Set
from codecipher.abstracts import IValidationEngine, IDataValidator
from .data_validator import DataValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ValidationEngine(IValidationEngine):
    '''
        Defines class ValidationEngine with attribute(s) and method(s).
        Creates validation engine with options to add multiple data validators.

        It defines:

            :attributes:
                | __validators - List of registered data validators.
            :methods:
                | __init__ - Initializes ValidationEngine constructor.
                | add_validator - Adds a new data validator to the validation engine.
                | is_valid - Validates data using all registered validators.
    '''

    def __init__(
        self,
        validators: Optional[List[IDataValidator]] = None,
        allowed_chars: Optional[Set[str]] = None
    ) -> None:
        '''
            Initializes ValidationEngine constructor.

            :param validators: Initial list of validators | None
            :type validators: <Optional[List[IDataValidator]]>
            :param allowed_chars: Strict cipher character set | None
            :type allowed_chars: <Optional[Set[str]]>
            :exceptions: None
        '''
        self.__validators: List[IDataValidator] = validators or [
            DataValidator(allowed_chars=allowed_chars)
        ]

    def add_validator(self, validator: Optional[IDataValidator]) -> None:
        '''
            Adds a new data validator to the validation engine.

            :param validator: Data validator instance to be added.
            :type validator: <Optional[IDataValidator]>
            :return: None
            :exceptions: None
        '''
        if validator and validator not in self.__validators:
            self.__validators.append(validator)

    def is_valid(self, data: Optional[str]) -> bool:
        '''
            Validates data using all registered validators.

            :param data: Data which should to be validated | None
            :type data: <Optional[str]>
            :return: True (valid) | False (invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not data:
            return False

        if not self.__validators:
            return False

        return all(validator.is_valid(data) for validator in self.__validators)
