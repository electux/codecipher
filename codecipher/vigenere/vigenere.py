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
    Creates container class with aggregate backend API.
'''

from typing import List, Optional
from codecipher.abstracts import IValidationEngine
from .encoder import VigenereEncoder
from .decoder import VigenereDecoder
from .key_generator import KeyGenerator
from .ivigenere import IVigenere
from .iencoder import IEncoder
from .idecoder import IDecoder
from .ikey_generator import IKeyGenerator
from .default_validation_engine import DefaultVigenereValidationEngine

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Vigenere(IVigenere):
    '''
        Defines class Vigenere with attribute(s) and method(s).
        Creates container class with aggregate backend API.

        It defines:

            :attributes:
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for algorithm.
                | __decoder - Decoder for algorithm.
                | __key_generator - Key generator for algorithm.
            :methods:
                | __init__ - Initializes Vigenere constructor.
                | encode - Encoding data to Vigenere format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from Vigenere format.
                | decode_data - Property method for getting decode data.
    '''

    def __init__(
        self,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IEncoder] = None,
        decoder: Optional[IDecoder] = None,
        key_generator: Optional[IKeyGenerator] = None
    ) -> None:
        '''
            Initializes Vigenere constructor.

            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IDecoder]>
            :param key_generator: Key generator for algorithm | None
            :type key_generator: <Optional[IKeyGenerator]>
            :exceptions: None
        '''
        self.__validation_engine: IValidationEngine = validation_engine or DefaultVigenereValidationEngine()
        self.__encoder: IEncoder = encoder or VigenereEncoder()
        self.__decoder: IDecoder = decoder or VigenereDecoder()
        self.__key_generator: IKeyGenerator = key_generator or KeyGenerator()

    def encode(self, data: Optional[str], key: Optional[str]) -> bool:
        '''
            Encoding data to Vigenere format.

            :param data: Data which should be encoded | None
            :type data: <Optional[str]>
            :param key: Key for encoding | None
            :type key: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data) or not bool(key):
            return False

        if self.__validation_engine.is_valid(data) and \
           self.__validation_engine.is_valid(key):
            self.__key_generator.key = key
            if self.__key_generator.generate_key(len(data)):
                return self.__encoder.encode(data, self.__key_generator.key)
        return False

    @property
    def encode_data(self) -> Optional[str]:
        '''
            Property method for getting encode data.
        '''
        return self.__encoder.encode_data

    def decode(self, data: Optional[str], key: Optional[str]) -> bool:
        '''
            Decoding data from Vigenere format.

            :param data: Data which should be decoded | None
            :type data: <Optional[str]>
            :param key: Key for decoding | None
            :type key: <Optional[str]>
            :return: True (if success) | False (if fail)
            :rtype: <bool>
            :exceptions: None
        '''
        if not bool(data) or not bool(key):
            return False

        if self.__validation_engine.is_valid(data) and \
           self.__validation_engine.is_valid(key):
            self.__key_generator.key = key
            if self.__key_generator.generate_key(len(data)):
                return self.__decoder.decode(data, self.__key_generator.key)
        return False

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.
        '''
        return self.__decoder.decode_data
