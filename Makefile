CC=cc
CFLAGS=-Wall -O3
LDFLAGS=
BIN_PATH=bin
SRC_PATH=src

all: dirs duval kmp

dirs:
	mkdir -p $(BIN_PATH)

duval:
	$(CC) $(CFLAGS) $(SRC_PATH)/duval.c $(SRC_PATH)/algo/duval.c -o $(BIN_PATH)/duval

kmp:
	$(CC) $(CFLAGS) $(SRC_PATH)/kmp.c $(SRC_PATH)/algo/kmp.c -o $(BIN_PATH)/kmp

clean:
	rm -rf $(BIN_PATH)
