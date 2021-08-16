def shift_1(s, w):
    c = s.pop(0)
    return w << 6 | (c & 0x3F)


def shift_2(s, w):
    w = shift_1(s, w)
    return shift_1(s, w)


def shift_3(s, w):
    w = shift_1(s, w)
    return shift_2(s, w)


def shift_4(s, w):
    w = shift_1(s, w)
    return shift_3(s, w)


def shift_5(s, w):
    w = shift_1(s, w)
    return shift_4(s, w)



def decode_utf8(s: bytes):
    s = list(s)
    while s:
        c = s.pop(0)
        if c < 0b11_000000:
            w = c
        elif c < 0b111_00000:
            w = c & 0b000_11111
            w = shift_1(s, w)
        elif c < 0b1111_0000:
            w = c & 0b0000_1111
            w = shift_2(s, w)
        elif c < 0b11111_000:
            w = c & 0b00000_111
            w = shift_3(s, w)
        elif c < 0b111111_00: 
            w = c & 0b000000_11
            w = shift_4(s, w)
        else:  # < 0b1111111_0
            w = c & 0b0000000_1
            w = shift_5(s, w)
        
        if w < 0x10000:
            yield w
        else:
            # Convert full 32-bit code into utf-16
            w -= 0x10000
            yield 0xD800 | (w >> 10)  # higher 10 bits
            yield 0xDC00 | (w & 0x3FF)  # lower 10 bits
