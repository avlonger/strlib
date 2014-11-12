#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>
#include "duval.h"

#define LENGTH 1000
#define EXPERIMENTS 1000

char *rand_string(char *str, size_t n) {
    for (size_t i = 0; i < n; ++i) {
        str[i] = (char) (rand() % 127 + 1);
    }
    str[n] = '\0';
    return str;
}

void test_duval_and_naive_results_equality() {
    char * text = calloc(LENGTH + 1, sizeof(char));
    int * output1 = calloc(LENGTH + 1, sizeof(int));
    int * output2 = calloc(LENGTH + 1, sizeof(int));

    for (int i = 0; i < EXPERIMENTS; ++i) {
        rand_string(text, LENGTH);
        int word_count2 = naive_lyndon_decomposition(text, output2);
        int word_count1 = duval(text, output1);
        assert(word_count1 == word_count2);
        assert(memcmp(output1, output2, word_count1) == 0);
    }

    free(text);
}

int main(int argc, char** argv) {
    printf("Testing Duval and naive algorithm results... ");
    test_duval_and_naive_results_equality();
    printf("OK\n");

    return 0;
}
