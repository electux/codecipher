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
    Creates container class with aggregate backend API.
'''

from typing import List, Optional
from codecipher.abstracts import IValidationEngine
from .ia1z52n62 import IA1z52N62
from .iencoder import IA1z52N62Encoder
from .encoder import A1z52N62Encoder
from .idecoder import IA1z52N62Decoder
from .decoder import A1z52N62Decoder
from .a1z52n62_config import A1z52N62Config
from .default_validation_engine import DefaultA1Z52N62ValidationEngine

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
        Creates container class with aggregate backend API.

        It defines:

            :attributes:
                | __config - Configuration for algorithm.
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for algorithm.
                | __decoder - Decoder for algorithm.
            :methods:
                | __init__ - Initializes A1z52N62 constructor.
                | encode - Encoding data to A1z52N62 format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from A1z52N62 format.
                | decode_data - Property method for getting decode data.
    '''

    def __init__(
        self,
        config: Optional[A1z52N62Config] = None,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IA1z52N62Encoder] = None,
        decoder: Optional[IA1z52N62Decoder] = None,
    ) -> None:
        '''
            Initializes A1z52N62 constructor.

            :param config: Configuration for algorithm | None
            :type config: <Optional[A1z52N62Config]>
            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IA1z52N62Encoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IA1z52N62Decoder]>
            :exceptions: None
        '''
        self.__config = config or A1z52N62Config()
        self.__validation_engine: IValidationEngine = validation_engine or DefaultA1Z52N62ValidationEngine()
        self.__encoder: IA1z52N62Encoder = encoder or A1z52N62Encoder(_config=self.__config)
        self.__decoder: IA1z52N62Decoder = decoder or A1z52N62Decoder(_config=self.__config)

    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to A1z52N62 format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data) or not self.__validation_engine.is_valid(data):
            return False
        return self.__encoder.encode(data)

    @property
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.

            :return: Encoded data
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__encoder.encode_data

    def decode(self, data: Optional[str]) -> bool:
        '''
            Decoding data from A1z52N62 format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data) or not self.__decoder.decode(data):
            return False

        return self.__validation_engine.is_valid(self.decode_data)

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decoded data
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__decoder.decode_data
