# -*- coding: UTF-8 -*-

'''
Module
    iconfig.py
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
    Defines abstract class IConfig for cipher configuration.
'''

from typing import List, Optional, Set
from abc import ABC

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IConfig(ABC):
    '''
        Defines interface IConfig with attribute(s).

        It defines:

            :attributes:
                | key - Controls transformation during encoding and decoding.
                | shift - Controls transformation during encoding and decoding.
                | upper_case_offset - Offset for uppercase letters in cipher set.
                | lower_case_offset - Offset for lowercase letters in cipher set.
                | lower_case_base - Base index for lowercase letters in cipher set.
                | numeric_base - Base index for numeric characters in cipher set.
                | alphabet_size - Size of alphabet in cipher set.
                | code_splitter - Code splitter in cipher set.
                | altchars - Defines replacements for '+' and '/' in cipher set.
                | padding - Adds to end '=' in cipher set.
                | allowed_chars - Strict set of allowed characters in cipher set.
            :methods: None
    '''

    key: Optional[str]
    shift: int
    upper_case_offset: int
    lower_case_offset: int
    lower_case_base: int
    numeric_base: int
    alphabet_size: int
    code_splitter: str
    altchars: Optional[bytes]
    padding: bool
    allowed_chars: Optional[Set[str]]
