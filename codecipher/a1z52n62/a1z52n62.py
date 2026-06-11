# -*- coding: UTF-8 -*-

'''
Module
    a1z52n62.py
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
    Defines class A1z52N62 with attribute(s) and method(s).
'''

from typing import List, Optional
from codecipher.abstracts import IValidationEngine, IA1Z52N62Config, IEncoder, IDecoder
from codecipher.a1z52n62.default import (
    DefaultA1z52N62Config,
    DefaultA1Z52N62ValidationEngine,
    DefaultA1z52N62Encoder,
    DefaultA1z52N62Decoder
)
from .ia1z52n62 import IA1z52N62

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class A1z52N62(IA1z52N62):
    '''
        Defines class A1z52N62 with attribute(s) and method(s).

        It defines:

            :attributes:
                | __config - Configuration for A1Z52N62 algorithm.
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for A1Z52N62 algorithm.
                | __decoder - Decoder for A1Z52N62 algorithm.
            :methods:
                | __init__ - Initializes A1z52N62 constructor.
                | encode - Encoding data to A1z52N62 format.
                | encode_data - Property method for getting encoded data.
                | decode - Decoding data from A1z52N62 format.
                | decode_data - Property method for getting decoded data.
    '''

    def __init__(
        self,
        config: Optional[IA1Z52N62Config] = None,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IEncoder] = None,
        decoder: Optional[IDecoder] = None,
    ) -> None:
        '''
            Initializes A1z52N62 constructor.

            :param config: Configuration for A1Z52N62 algorithm | None
            :type config: <Optional[IA1Z52N62Config]>
            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IDecoder]>
            :exceptions: None
        '''
        # Dependecy injection or use default implementation
        self.__config: IA1Z52N62Config = config or DefaultA1z52N62Config()
        self.__validation_engine: IValidationEngine = validation_engine or DefaultA1Z52N62ValidationEngine(
            allow_space=self.__config.allow_space
        )
        self.__encoder: IEncoder = encoder or DefaultA1z52N62Encoder(_config=self.__config)
        self.__decoder: IDecoder = decoder or DefaultA1z52N62Decoder(_config=self.__config)

    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to A1z52N62 format.

            :param data: Data which should to be encoded | None
            :type data: <Optional[str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        # Checking and validation data for encoding
        if not data or not self.__validation_engine.is_valid(data):
            return False

        # Checking encoding data
        return self.__encoder.encode(data)

    @property
    def encoded_data(self) -> Optional[str]:
        '''
            Property method for getting encoded data.

            :return: Encoded data | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__encoder.encoded_data

    def decode(self, data: Optional[str]) -> bool:
        '''
            Decoding data from A1z52N62 format.

            :param data: Data which should to be decoded | None
            :type data: <Optional[str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        # Checking and decoding data
        if not data or not self.__decoder.decode(data):
            return False

        # Checking and validation decoding data
        return self.__validation_engine.is_valid(self.decoded_data)

    @property
    def decoded_data(self) -> Optional[str]:
        '''
            Property method for getting decoded data.

            :return: Decoded data | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__decoder.decoded_data
