import os

from ctypes import *
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def libutf8_decoder():
    return cdll.LoadLibrary("libutf8_decoder.so")


@pytest.mark.parametrize("text", [
    "abcd"
])
def test_utf8_decoder(libutf8_decoder, text):
    lib = libutf8_decoder
    array_size = len(text.encode('utf-16-le')) // 2
    buffer = (c_ulong * array_size)()
    result = lib.decode_utf8(buffer, text)
    print(list(buffer))
    assert False
