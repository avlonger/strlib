CC=cc
CFLAGS=-Wall -O3
LDFLAGS=
BIN_PATH=bin
SRC_PATH=src
VPATH=src
SOURCES=$(wildcard $(SRC_PATH)/*.c)
EXECUTABLES=$(SOURCES:$(SRC_PATH)/%.c=%)


all: dirs $(EXECUTABLES)

dirs:
	mkdir -p $(BIN_PATH)

%: %.c
	$(CC) $(CFLAGS) $< -o $(BIN_PATH)/$@

clean:
	rm -rf $(BIN_PATH)
