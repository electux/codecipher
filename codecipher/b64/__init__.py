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
from .iencoder import IEncoder
from .idecoder import IDecoder
from .default_validation_engine import DefaultB64ValidationEngine
from .default_data_validator import DefaultB64DataValidator
from .default_character_validator import DefaultB64CharacterValidator

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
    'IEncoder',
    'IDecoder',
    'B64Encoder',
    'B64Decoder',
    'B64',
    'DefaultB64ValidationEngine',
    'DefaultB64DataValidator',
    'DefaultB64CharacterValidator'
]
