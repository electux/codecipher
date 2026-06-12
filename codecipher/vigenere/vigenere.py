# -*- coding: UTF-8 -*-

'''
Module
    vigenere.py
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
    Defines class Vigenere with attribute(s) and method(s).
'''

from typing import List, Optional
from codecipher.abstracts import (
    ICipherEngine, IConfig, IValidationEngine, IEncoder, IDecoder
)
from codecipher.validation import ValidationEngine
from codecipher.vigenere.encoder import Encoder
from codecipher.vigenere.decoder import Decoder
from .config import VigenereConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Vigenere(ICipherEngine):
    '''
        Defines class Vigenere with attribute(s) and method(s).

        It defines:

            :attributes:
                | __config - Configuration for cipher VIGENERE.
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for cipher VIGENERE.
                | __decoder - Decoder for cipher VIGENERE.
            :methods:
                | __init__ - Initializes Vigenere constructor.
                | encode - Encoding data to VIGENERE format.
                | decode - Decoding data from VIGENERE format.
    '''

    def __init__(
        self,
        config: Optional[IConfig] = None,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IEncoder] = None,
        decoder: Optional[IDecoder] = None,
    ) -> None:
        '''
            Initializes Vigenere constructor.

            :param config: Configuration for cipher VIGENERE | None
            :type config: <Optional[IConfig]>
            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for cipher  | None
            :type encoder: <Optional[IEncoder]>
            :param decoder: Decoder for cipher  | None
            :type decoder: <Optional[IDecoder]>
            :exceptions: None
        '''
        # Dependency injection or use default implementations
        self.__config: IConfig = config or VigenereConfig()
        self.__validation_engine: IValidationEngine = validation_engine or ValidationEngine(
            allowed_chars=self.__config.allowed_chars
        )
        self.__encoder: IEncoder = encoder or Encoder(_config=self.__config)
        self.__decoder: IDecoder = decoder or Decoder(_config=self.__config)

    def encode(self, data: Optional[str]) -> Optional[str]:
        '''
            Encoding data to VIGENERE format.

            :param data: Data in string format which should to be encoded | None
            :type data: <Optional[str]>
            :return: Encoded data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        # Checking and validation data for process of encoding
        if not data or not self.__validation_engine.is_valid(data):
            return None

        # Checking process of encoding data
        if not self.__encoder.encode(data):
            return None

        return self.__encoder.encoded_data

    def decode(self, data: Optional[str]) -> Optional[str]:
        '''
            Decoding data from VIGENERE format.

            :param data: Data in string format which should to be decoded | None
            :type data: <Optional[str]>
            :return: Decoded data in string format (success) | None (fail)
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        # Checking data and process of decoding data
        if not data or not self.__decoder.decode(data):
            return None

        # Checking and validation decoded data
        if not self.__validation_engine.is_valid(self.__decoder.decoded_data):
            return None

        return self.__decoder.decoded_data
