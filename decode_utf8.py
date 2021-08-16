def decode_utf8(s: bytes):
    s = list(s)
    while s:
        c = s.pop(0)
        w = c
        if c > 0xC0:
            if c < 0xE0:
                w = c & 0x1F
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
            elif c < 0xF0:
                w = c & 0x0F
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
            elif c < 0xF8:
                w = c & 0x07
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
            elif c < 0xFC:
                w = c & 0x03
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
            else:
                w = c & 1
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
                
                c = s.pop(0)
                w = w << 6 | (c & 0x3F)
        
        if w < 0x10000:
            yield w
        else:
            yield 0xD7C0 | (w >> 10)
            yield 0xDC00 | (w & 0x3FF)
