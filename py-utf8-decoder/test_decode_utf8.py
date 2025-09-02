from decode_utf8 import decode_utf8
from hypothesis import example, given
from hypothesis import strategies as st


@given(st.text())
@example("Hello!")
@example("Привет!")
@example("你好")
@example("🏠")
def test(text):
    encoded_utf8 = text.encode("utf-8")
    utf16_byte_pairs = decode_utf8(encoded_utf8)
    utf16_le_bytes = b"".join(map(lambda x: x.to_bytes(2, byteorder="little"), utf16_byte_pairs))
    assert utf16_le_bytes == text.encode("utf-16-le")
