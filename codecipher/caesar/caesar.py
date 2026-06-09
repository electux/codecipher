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

from typing import Optional
from .icaesar_encoder import ICaesarEncoder
from .icaesar import ICaesar
from .icaesar_decoder import ICaesarDecoder
from .encoder import CaesarEncoder
from .decoder import CaesarDecoder

class Caesar(ICaesar):
    '''
        Defines class Caesar with attribute(s) and method(s).
        Creates container class with aggregate backend API.

        It defines:
            :attributes:
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
        encoder: Optional[ICaesarEncoder] = None,
        decoder: Optional[ICaesarDecoder] = None,
    ) -> None:
        '''
            Initializes Caesar constructor.

            :param encoder: Encoder for algorithm | None
            :type encoder: <Optional[ICaesarEncoder]>
            :param decoder: Decoder for algorithm | None
            :type decoder: <Optional[ICaesarDecoder]>
            :exceptions: None
        '''
        self.__encoder: ICaesarEncoder = encoder or CaesarEncoder()
        self.__decoder: ICaesarDecoder = decoder or CaesarDecoder()

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
        if not bool(data) or shift_counter is None:
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
        if not bool(data) or shift_counter is None:
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
