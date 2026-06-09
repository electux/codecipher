# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class B64 with attribute(s) and method(s).
    Creates container class with aggregate backend API.
'''

from typing import List
from .b64 import B64
from .ib64 import IB64
from .b64encoder import B64Encoder
from .b64decoder import B64Decoder
from .ib64encoder import IB64Encoder
from .ib64decoder import IB64Decoder
from .validation_engine import ValidationEngine
from .ivalidation_engine import IValidationEngine
from .data_validator import DataValidator
from .idata_validator import IDataValidator
from .character_validator import CharacterValidator
from .icharacter_validator import ICharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

__all__: List[str] = [
    'IB64',
    'IB64Encoder',
    'IB64Decoder',
    'B64Encoder',
    'B64Decoder',
    'B64',
    'IValidationEngine',
    'ValidationEngine',
    'IDataValidator',
    'DataValidator',
    'ICharacterValidator',
    'CharacterValidator'
]
