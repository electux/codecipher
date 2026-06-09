# -*- coding: UTF-8 -*-

'''
Module
    aleph_taw_bet_shin.py
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
    Defines class AlephTawBetShin with attribute(s) and method(s).
    Creates container class with aggregate backend API.
'''

from typing import Optional, List
from .iatbs import IATBS
from .iencoder import IATBSEncoder
from .encoder import ATBSEncoder
from .idecoder import IATBSDecoder
from .decoder import ATBSDecoder
from .ivalidation_engine import IValidationEngine
from .validation_engine import ValidationEngine
from .data_validator import DataValidator
from .character_validator import CharacterValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/codecipher'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/codecipher/blob/main/LICENSE'
__version__: str = '1.5.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATBS(IATBS):
    '''
        Defines class ATBS with attribute(s) and method(s).
        Creates container class with aggregate backend API.

        It defines:

            :attributes:
                | __config - Configuration for algorithm.
                | __validation_engine - Engine for data validation.
                | __encoder - Encoder for algorithm.
                | __decoder - Decoder for algorithm.
            :methods:
                | __init__ - Initializes ATBS constructor.
                | encode - Encoding data to ATBS format.
                | encode_data - Property method for getting encode data.
                | decode - Decoding data from ATBS format.
                | decode_data - Property method for getting decode data.
    '''

    def __init__(
        self,
        validation_engine: Optional[IValidationEngine] = None,
        encoder: Optional[IATBSEncoder] = None,
        decoder: Optional[IATBSDecoder] = None,
    ) -> None:
        '''
            Initializes ATBS constructor.

            :param config: Configuration for algorithm | None
            :type config: <Optional[ATBSConfig]>
            :param validation_engine: Engine for data validation | None
            :type validation_engine: <Optional[IValidationEngine]>
            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[IATBSEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[IATBSDecoder]>
            :exceptions: None
        '''
        self.__validation_engine: IValidationEngine = validation_engine or ValidationEngine(
            [DataValidator(CharacterValidator())]
        )
        self.__encoder: IATBSEncoder = encoder or ATBSEncoder()
        self.__decoder: IATBSDecoder = decoder or ATBSDecoder()

    def encode(self, data: Optional[str]) -> bool:
        '''
            Encoding data to ATBS format.
        '''
        if not bool(data) or not self.__validation_engine.is_valid(data):
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
            Decoding data from ATBS format.
        '''
        if not bool(data) or not self.__decoder.decode(data):
            return False

        return self.__validation_engine.is_valid(self.decode_data)

    @property
    def decode_data(self) -> Optional[str]:
        '''
            Property method for getting decode data.
        '''
        return self.__decoder.decode_data
