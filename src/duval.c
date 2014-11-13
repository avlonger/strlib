#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "algo/duval.h"


int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: %s TEXT\n", argv[0]);
        return 1;
    }
    char * text = argv[1];

    int * output = calloc(strlen(text), sizeof(int));

    int word_count = naive_lyndon_decomposition(text, output);

    printf("WORD COUNT: %d\n", word_count);

    for (int i = 0; i < word_count; ++i) {
        printf("%d ", output[i]);
    }
    printf("\n");

    return 0;
}
