# -*- coding: UTF-8 -*-

'''
Module
    b64.py
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

from typing import List, Optional
from codecipher.abstracts import IValidationEngine
from .ib64 import IB64
from .iencoder import IEncoder
from .idecoder import IDecoder
from .b64encoder import B64Encoder
from .b64decoder import B64Decoder
from .default_validation_engine import DefaultB64ValidationEngine

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class B64(IB64):
    '''
        Defines class B64 with attribute(s) and method(s).
        Creates container class with aggregate backend API.

        It defines:

            :attributes:
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for algorithm.
                | __decoder - Decoder for algorithm.
            :methods:
                | __init__ - Initializes B64 constructor.
                | encode - Encoding data to B64 format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from B64 format.
                | decode_data - Property method for getting decode data.
    '''

    def __init__(
        self,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IEncoder] = None,
        decoder: Optional[IDecoder] = None,
    ) -> None:
        '''
            Initializes B64 constructor.

            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IDecoder]>
            :exceptions: None
        '''
        self.__validation_engine: IValidationEngine = validation_engine or DefaultB64ValidationEngine()
        self.__encoder: IEncoder = encoder or B64Encoder()
        self.__decoder: IDecoder = decoder or B64Decoder()

    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to B64 format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        # For encoding, we don't strictly need to validate the input characters
        # as b64encode can handle any byte string.
        if not bool(data):
            return False
        return self.__encoder.encode(data)

    @property
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.
        '''
        return self.__encoder.encode_data

    def decode(self, data: Optional[str]) -> bool:
        '''
            Decoding data from B64 format.
        '''
        if not bool(data) or not self.__validation_engine.is_valid(data):
            return False
        return self.__decoder.decode(data)

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.
        '''
        return self.__decoder.decode_data
