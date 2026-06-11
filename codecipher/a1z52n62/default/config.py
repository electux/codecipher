# -*- coding: UTF-8 -*-

'''
Module
    default_config.py
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
    Defines configuration for algorithm A1z52N62.
'''

from typing import List
from dataclasses import dataclass
from codecipher.abstracts import IA1Z52N62Config

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(frozen=True)
class DefaultA1z52N62Config(IA1Z52N62Config):
    '''
        Defines class DefaultA1z52N62Config with attribute(s).

        It defines:

            :attributes:
                | allow_space - Allow space in A1Z52N62 (default True).
                | upper_case_offset - Offset for uppercase letters (default 64).
                | lower_case_offset - Offset for lowercase letters (default 96).
                | lower_case_base - Base index for lowercase letters (default 27).
                | numeric_base - Base index for numeric characters (default 53).
                | alphabet_size - Size of alphabet (default 26).
                | code_splitter - Code splitter (default ' - ').
            :methods: None
    '''

    allow_space: bool = True
    upper_case_offset: int = 64
    lower_case_offset: int = 96
    lower_case_base: int = 27
    numeric_base: int = 53
    alphabet_size: int = 26
    code_splitter: str = ' - '
