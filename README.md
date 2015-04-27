Implementation of some basic algorithms on strings

# Compilation

```
$ make
```

# KMP

[Source](https://github.com/avlonger/strlib/blob/master/src/kmp.c)

Usage:
```
$ ./bin/kmp aba abaabacaba
OCCURENCES: 3
0 3 7
```

# Duval alogrithm

[Source](https://github.com/avlonger/strlib/blob/master/src/duval.c)

Usage:
```
$ ./bin/duval -h mississippi
FACTOR COUNT: 5
FACTOR POSITIONS:
0 1 4 7 10
m|iss|iss|ipp|i
```

# Tests
To run tests execute:
```
./bin/kmp -t
```
or
```
./bin/duval -t
```