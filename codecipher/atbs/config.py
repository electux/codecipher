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
    Defines configuration for cipher ATBS logic.
'''

from typing import Dict, List, Optional, Set
from string import ascii_lowercase, ascii_uppercase, digits, whitespace
from dataclasses import dataclass, field
from codecipher.abstracts import IConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(frozen=True)
class ATBSConfig(IConfig):
    '''
        Defines class ATBSConfig with attribute(s).

        It defines:

            :attributes:
                | key - Controls transformation during encoding and decoding (default None).
                | shift - Controls transformation during encoding and decoding (default 0).
                | upper_case_offset - Offset for uppercase letters (default 0).
                | lower_case_offset - Offset for lowercase letters (default 0).
                | lower_case_base - Base index for lowercase letters (default 0).
                | numeric_base - Base index for numeric characters (default 0).
                | alphabet_size - Size of alphabet (default 0).
                | code_splitter - Code splitter (default None).
                | altchars - Defines replacements for '+' and '/' (default None).
                | padding - Adds to end '=' (default False).
                | allowed_chars - Strict set of allowed characters (default ascii_lowercase + ascii_uppercase + digits + whitespace).
                | lookup_table - Lookup table for cipher set.
            :methods: None
    '''

    key: Optional[str] = None
    shift: int = 0
    upper_case_offset: int = 0
    lower_case_offset: int = 0
    lower_case_base: int = 0
    numeric_base: int = 0
    alphabet_size: int = 0
    code_splitter: Optional[str] = None
    altchars: Optional[bytes] = None
    padding: bool = False
    allowed_chars: Optional[Set[str]] = field(
        default_factory=lambda: set(ascii_lowercase + ascii_uppercase + digits + whitespace)
    )
    lookup_table: Optional[Dict[str, str]] = field(
        default_factory=lambda: {
            'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
            'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
            'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
            'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
            'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
            'Z': 'A', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w',
            'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r',
            'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm',
            'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h',
            't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
            'y': 'b', 'z': 'a', ' ': ' ', '\n': '\n', '0': '9',
            '1': '8', '2': '7', '3': '6', '4': '5', '5': '4',
            '6': '3', '7': '2', '8': '1', '9': '0'
        }
    )
