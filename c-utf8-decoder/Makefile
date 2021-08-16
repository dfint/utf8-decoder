.PHONY: compile bin clean
all: bin

CC=gcc
CFLAGS=-O3
NAME=utf8_decoder

$(NAME).o: $(NAME).c
	$(CC) $(CFLAGS) -c $(NAME).c

compile: $(NAME).o

$(NAME).bin: $(NAME).o
	objcopy -O binary -j .text $(NAME).o $(NAME).bin

bin: $(NAME).bin

clean:
	rm *.o *.bin
