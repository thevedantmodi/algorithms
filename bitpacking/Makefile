CC = gcc

INCLUDES = $(shell echo *.h)

all: bitpack-exec

%.o: %.c $(INCLUDES)
	$(CC) $< -c

bitpack-exec: main.o bitpack.o
	$(CC) $^ -o $@

clean:
	rm *.o bitpack-exec