# -*- coding: UTF-8 -*-

'''
Module
    decode_algorithm.py
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
    Defines class DecodeAlgorithm with default cipher B64 implementation.
'''

from typing import List, Optional
from base64 import b64decode
from binascii import Error
from codecipher.abstracts import IAlgorithm, IConfig
from codecipher.b64.config import B64Config

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class DecodeAlgorithm(IAlgorithm[IConfig]):
    '''
        Defines class DecodeAlgorithm with attribute(s) and method(s).

        It defines:

            :attributes:
                | _config - Configuration parameters for cipher B64.
            :methods:
                | __init__ - Initializes DecodeAlgorithm constructor.
                | encoded_data - Property method for getting decoded data.
                | encode - Execute cipher B64 logic.
    '''

    def __init__(self) -> None:
        '''
            Initializes DecodeAlgorithm constructor.

            :exceptions: None
        '''
        self.__config: Optional[IConfig] = None

    def execute(self, data: Optional[str] = None, config: Optional[IConfig] = None) -> Optional[str]:
        '''
            Execute cipher B64 logic.

            :param data: Data in string format which should to be decoded | None
            :type data: <Optional[str]>
            :param config: Configuration for cipher | None
            :type config: <Optional[IConfig]>
            :return: Decoded data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        if not data:
            return None

        self.__config = config or B64Config()

        if not self.__config:
            return None

        if not self.__config.padding:
            missing_padding: int = len(data) % 4

            if missing_padding:
                data += '=' * (4 - missing_padding)

        try:
            decoded_bytes: bytes = b64decode(data.encode('utf-8'), altchars=self.__config.altchars)

            return decoded_bytes.decode('utf-8')
        except (Error, UnicodeDecodeError, ValueError):
            # binascii->Error: invalid base64 input
            # UnicodeDecodeError: decoded bytes are not valid UTF-8
            # ValueError: defensive catch for other decode-related errors
            return None
