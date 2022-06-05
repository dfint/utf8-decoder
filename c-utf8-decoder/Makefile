.PHONY: compile bin clean so test pytest

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
	rm *.o *.bin *.so *.out || true

lib$(NAME).so: $(NAME).c
	rm *.o || true
	$(CC) -shared -o lib$(NAME).so -fPIC $(NAME).c

so: lib$(NAME).so

pytest: so
	pytest

test:
	$(CC) $(CFLAGS) test.c $(NAME).c
	./a.out
