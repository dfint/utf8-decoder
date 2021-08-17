#include <stdio.h>

#include "utf8_decoder.h"


int main() {
    unsigned char * message = "abcd";
    uint32_t buffer[4];
    
    decode_utf8(buffer, message);
    printf("%c %c %c %c\n", buffer[0], buffer[1], buffer[2], buffer[3]);
    
    return 0;
}