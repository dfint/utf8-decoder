def shift_1(s, w):
    c = s.pop(0)
    return w << 6 | (c & 0x3F)


def decode_utf8(s: bytes):
    s = list(s)
    while s:
        c = s.pop(0)
        if c < 0xC0:
            w = c
        elif c < 0xE0:
            w = c & 0x1F
            w = shift_1(s, w)
        elif c < 0xF0:
            w = c & 0x0F
            w = shift_1(s, w)
            w = shift_1(s, w)
        elif c < 0xF8:
            w = c & 0x07
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
        elif c < 0xFC:
            w = c & 0x03
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
        else:  # < 0xFE
            w = c & 0x01
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
            w = shift_1(s, w)
        
        if w < 0x10000:
            yield w
        else:
            # Convert full 32-bit code into utf-16
            w -= 0x10000
            yield 0xD800 | (w >> 10)  # higher 10 bits
            yield 0xDC00 | (w & 0x3FF)  # lower 10 bits
