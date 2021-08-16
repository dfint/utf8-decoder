import pytest

from decode_utf8 import decode_utf8


@pytest.mark.parametrize("text",
[
    "Привет!",
    "你好"
])
def test(text):
    encoded_utf8 = text.encode('utf-8')
    utf16_byte_pairs = decode_utf8(encoded_utf8)
    utf16_le_bytes = b''.join(map(lambda x: x.to_bytes(2, byteorder='little'), utf16_byte_pairs))
    assert utf16_le_bytes == text.encode('utf-16-le')
