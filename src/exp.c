#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>
#include "duval.h"

#define LENGTH 1000
#define EXPERIMENTS 100
#define ALPHABET_SIZE 127

char *rand_string(char *str, int n, int alphabet_size) {
    for (int i = 0; i < n; ++i) {
        str[i] = (char) (rand() % alphabet_size + 1);
    }
    str[n] = '\0';
    return str;
}

void test_duval_and_naive_results_equality() {
    char * text = calloc(LENGTH + 1, sizeof(char));
    int * output1 = calloc(LENGTH + 1, sizeof(int));
    int * output2 = calloc(LENGTH + 1, sizeof(int));

    for (int i = 0; i < EXPERIMENTS; ++i) {
        rand_string(text, LENGTH, 100);
        int word_count2 = naive_lyndon_decomposition(text, output2);
        int word_count1 = duval(text, output1);
        assert(word_count1 == word_count2);
        assert(memcmp(output1, output2, word_count1) == 0);
    }

    free(text);
}

void save_random_strings_results() {
    freopen("/Users/alonger/HSE/stringology/strlib/result.txt", "wt", stdout);
    int * buffer = calloc(LENGTH + 1, sizeof(int));
    char * text = calloc(LENGTH + 1, sizeof(char));
    for (int alphabet_size = 2; alphabet_size <= ALPHABET_SIZE; ++alphabet_size) {
        for (int length = 2; length < LENGTH; ++length) {
            printf("%d %d\n", alphabet_size, length);
            for (int exp = 0; exp < EXPERIMENTS; ++exp) {
                printf("%d ", duval(rand_string(text, length, alphabet_size), buffer));
            }
            printf("\n");
        }
    }
    free(buffer);
}

int main(int argc, char** argv) {

    return 0;
}
