CC=cc
CFLAGS=-Wall -O3 -std=gnu99
LDFLAGS=-lm
BIN_PATH=bin
SRC_PATH=src

all: dirs duval kmp

dirs:
	mkdir -p $(BIN_PATH)

duval:
	$(CC) $(CFLAGS) $(SRC_PATH)/duval.c $(LDFLAGS) -o $(BIN_PATH)/duval

kmp:
	$(CC) $(CFLAGS) $(SRC_PATH)/kmp.c $(LDFLAGS) -o $(BIN_PATH)/kmp

clean:
	rm -rf $(BIN_PATH)
