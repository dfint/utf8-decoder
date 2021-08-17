import os

from ctypes import *
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def decode_utf8():
    lib = cdll.LoadLibrary("libutf8_decoder.so")
    lib.decode_utf8.restype = c_void_p
    return lib.decode_utf8


@pytest.mark.parametrize("text", [
    "abcd",
    "Hello!",
    "Привет!",
    "你好",
    "🏠",
])
def test_utf8_decoder(decode_utf8, text):
    array_size = len(text.encode('utf-16-le')) // 2
    buffer = (c_uint32 * array_size)()

    result = decode_utf8(buffer, text.encode('utf-8'))

    result_size = (result - addressof(buffer)) // sizeof(c_uint32)
    assert result_size == array_size
    
    utf16_le_bytes = b''.join(map(lambda x: x.to_bytes(2, byteorder='little'), buffer))
    assert utf16_le_bytes == text.encode('utf-16-le')
