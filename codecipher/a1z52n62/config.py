# -*- coding: UTF-8 -*-

'''
Module
    config.py
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
    Defines configuration for cipher A1z52N62 logic.
'''

from typing import Dict, List, Optional, Set
from string import ascii_lowercase, ascii_uppercase, digits, whitespace
from dataclasses import dataclass, field
from codecipher.abstracts.iconfig import IConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(frozen=True)
class A1z52N62Config(IConfig):
    '''
        Defines class A1z52N62Config with attribute(s).

        It defines:

            :attributes:
                | key - Controls transformation during encoding and decoding (default None).
                | shift - Controls transformation during encoding and decoding (default 0).
                | upper_case_offset - Offset for uppercase letters (default 64).
                | lower_case_offset - Offset for lowercase letters (default 96).
                | lower_case_base - Base index for lowercase letters (default 27).
                | numeric_base - Base index for numeric characters (default 53).
                | alphabet_size - Size of alphabet (default 26).
                | code_splitter - Code splitter (default ' - ').
                | altchars - Defines replacements for '+' and '/' (default None).
                | padding - Adds to end '=' (default False).
                | allowed_chars - Strict set of allowed characters (default ascii_lowercase + ascii_uppercase + digits + whitespace).
                | lookup_table - Lookup table for cipher set (default None).
            :methods: None
    '''

    key: Optional[str] = None
    shift: int = 0
    upper_case_offset: int = 64
    lower_case_offset: int = 96
    lower_case_base: int = 27
    numeric_base: int = 53
    alphabet_size: int = 26
    code_splitter: Optional[str] = ' - '
    altchars: Optional[bytes] = None
    padding: bool = False
    allowed_chars: Optional[Set[str]] = field(
        default_factory=lambda: set(ascii_lowercase + ascii_uppercase + digits + whitespace)
    )
    lookup_table: Optional[Dict[str, str]] = None
