#include <stdint.h>

#define SHIFT_1(s, w) (w << 6 | *(s)++ & 0x3F)

uint32_t shift(unsigned char ** pbuffer, uint32_t w, int n);


uint32_t * decode_utf8(uint32_t *out_buffer, unsigned char *in_buffer)
{
    unsigned char c;
    while (c = *in_buffer++) {
        uint32_t w;
        if (c < 0b11000000) {
            w = (uint32_t)c;
        } else if (c < 0b11100000) {
            w = c & 0b00011111;
            w = SHIFT_1(in_buffer, w);
            // w = shift(&in_buffer, w, 1);
        } else if (c < 0b11110000) {
            w = c & 0b00001111;
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            // w = shift(&in_buffer, w, 2);
        } else if (c < 0b11111000) {
            w = c & 0b00000111;
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
        } else if (c < 0b11111100) {
            w = c & 0b00000011;
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
        } else {  // c < 0b11111110
            w = c & 0b00000001;
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
            w = SHIFT_1(in_buffer, w);
        }

        if (w < 0x10000) {
            *out_buffer++ = w;
        } else {
            // Convert full 32-bit code into utf-16
            w -= 0x10000;
            *out_buffer++ = 0xD800 | (w >> 10);  // higher 10 bits
            *out_buffer++ = 0xDC00 | (w & 0x3FF);  // lower 10 bits
        }
    }

    return out_buffer;
}


uint32_t shift(unsigned char ** pbuffer, uint32_t w, int n) {
    unsigned char * buffer = *pbuffer;
    for (int i; i < n; i++) {
        w = SHIFT_1(buffer, w);
    }
    return w;
}