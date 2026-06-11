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
    Defines class DefaultATBSValidationEngine for managing multiple data validators.
'''

from typing import List, Optional
from codecipher.abstracts import IValidationEngine, IDataValidator
from .data_validator import DefaultATBSDataValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DefaultATBSValidationEngine(IValidationEngine):
    '''
        Defines class DefaultATBSValidationEngine with attribute(s) and method(s).
        Creates validation engine class for ATBS.

        It defines:

            :attributes:
                | __validators - List of registered data validators.
            :methods:
                | __init__ - Initializes DefaultATBSValidationEngine constructor.
                | add_validator - Adds a new data validator to the engine.
                | is_valid - Validates data using all registered validators.
    '''

    def __init__(self, validators: Optional[List[IDataValidator]] = None) -> None:
        '''
            Initializes DefaultATBSValidationEngine constructor.

            :param validators: Initial list of validators | None
            :type validators: <Optional[List[IDataValidator]]>
            :exceptions: None
        '''
        self.__validators: List[IDataValidator] = validators or [DefaultATBSDataValidator()]

    def add_validator(self, validator: IDataValidator) -> None:
        '''
            Adding a new data validator to the engine.

            :param validator: Validator instance to add.
            :type validator: <IDataValidator>
            :return: None
            :exceptions: None
        '''
        if validator and validator not in self.__validators:
            self.__validators.append(validator)

    def is_valid(self, data: Optional[str]) -> bool:
        '''
            Validating data using all registered validators.

            :param data: Data which should be validated | None
            :type data: <Optional[str]>
            :return: True (if all valid) | False (if any invalid)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data):
            return False

        if not self.__validators:
            return False

        return all(validator.is_valid(data) for validator in self.__validators)
