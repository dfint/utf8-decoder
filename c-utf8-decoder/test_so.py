from ctypes import cdll, c_void_p, c_uint32, addressof, sizeof

from hypothesis import given, example, strategies as st

import pytest


@pytest.fixture(scope="module")
def decode_utf8():
    lib = cdll.LoadLibrary("./libutf8_decoder.so")
    lib.decode_utf8.restype = c_void_p
    return lib.decode_utf8


@given(st.text(st.characters(blacklist_characters="\x00")))
@example("Hello!")
@example("Привет!")
@example("你好")
@example("🏠")
@pytest.mark.xfail(raises=UnicodeEncodeError)
def test_utf8_decoder(decode_utf8, text):
    array_size = len(text.encode('utf-16-le')) // 2
    buffer = (c_uint32 * array_size)()

    result = decode_utf8(buffer, text.encode('utf-8'))

    result_size = (result - addressof(buffer)) // sizeof(c_uint32)
    assert result_size == array_size
    
    utf16_le_bytes = b''.join(map(lambda x: x.to_bytes(2, byteorder='little'), buffer))
    assert utf16_le_bytes == text.encode('utf-16-le')
