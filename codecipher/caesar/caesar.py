# -*- coding: UTF-8 -*-

'''
Module
    caesar.py
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
    Defines class Caesar with attribute(s) and method(s).
    Creates container class with aggregate backend API.
'''

from typing import Optional, List
from codecipher.abstracts import IValidationEngine
from .iencoder import IEncoder
from .icaesar import ICaesar
from .idecoder import IDecoder
from .encoder import CaesarEncoder
from .decoder import CaesarDecoder
from .default_validation_engine import DefaultCaesarValidationEngine

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Caesar(ICaesar):
    '''
        Defines class Caesar with attribute(s) and method(s).
        Creates container class with aggregate backend API.

        It defines:
            :attributes:
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for Caesar algorithm.
                | __decoder - Decoder for Caesar algorithm.
            :methods:
                | __init__ - Initializes Caesar constructor.
                | encode - Encoding data to Caesar format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from Caesar format.
                | decode_data - Property method for getting decode data.
    '''

    def __init__(
        self,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IEncoder] = None,
        decoder: Optional[IDecoder] = None,
    ) -> None:
        '''
            Initializes Caesar constructor.

            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IDecoder]>
            :exceptions: None
        '''
        self.__validation_engine: IValidationEngine = validation_engine or DefaultCaesarValidationEngine()
        self.__encoder: IEncoder = encoder or CaesarEncoder()
        self.__decoder: IDecoder = decoder or CaesarDecoder()

    def encode(self, data: Optional[str], shift_counter: Optional[int]) -> bool:
        '''
            Encoding data to Caesar format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :param shift_counter: Shift value | None
            :type shift_counter: <Optional[int]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if shift_counter is None or not self.__validation_engine.is_valid(data):
            return False
        return self.__encoder.encode(data, shift_counter)

    @property
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.

            :return: Encoded data | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__encoder.encode_data

    def decode(self, data: Optional[str], shift_counter: Optional[int]) -> bool:
        '''
            Decoding data from Caesar format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :param shift_counter: Shift value | None
            :type shift_counter: <Optional[int]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if shift_counter is None or not self.__validation_engine.is_valid(data):
            return False
        return self.__decoder.decode(data, shift_counter)

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.

            :return: Decoded data | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__decoder.decode_data
