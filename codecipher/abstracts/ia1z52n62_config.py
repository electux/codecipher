# -*- coding: UTF-8 -*-

'''
Module
    ia1z52n62_config.py
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
    Defines class IA1Z52N62Config with expected configuration for A1Z52N62 algorithm.
'''

from typing import List
from abc import ABC
from .iconfig import IConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IA1Z52N62Config(IConfig, ABC):
    '''
        Defines abstract class with expected configuration attribute(s).

        It defines:

            :attributes:
              | allow_space - Allow space in A1Z52N62.
              | upper_case_offset - Upper case in integer format.
              | lower_case_offset - Lower case in integer format.
              | lower_case_base - Lower case base in integer format.
              | numeric_base - Numeric base in integer format.
              | alphabet_size - Alphabet size in integer format.
              | code_splitter - Code splitter in integer format.
            :methods: None
    '''

    allow_space: bool
    upper_case_offset: int
    lower_case_offset: int
    lower_case_base: int
    numeric_base: int
    alphabet_size: int
    code_splitter: str
