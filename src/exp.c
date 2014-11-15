#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>
#include "algo/duval.h"

#define LENGTH 1000
#define EXPERIMENTS 100000
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

void save_random_strings_results_for_alphabets() {
    freopen("/Users/alonger/HSE/stringology/strlib/result_alphabets.txt", "wt", stdout);
    int * buffer = calloc(LENGTH + 1, sizeof(int));
    char * text = calloc(LENGTH + 1, sizeof(char));

    int alphabet_sizes[13] = {2,3,5,10,20,30,40,50,60,70,80,90,100};
    for (int i = 0; i < 13; ++i) {
        int alphabet_size = alphabet_sizes[i];
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


void save_random_strings_results_for_lengths() {
    freopen("/Users/alonger/HSE/stringology/strlib/result_lengths.txt", "wt", stdout);
    int * buffer = calloc(LENGTH + 1, sizeof(int));
    char * text = calloc(LENGTH + 1, sizeof(char));
    int lengths[11] = {10,100,200,300,400,500,600,700,800,900,1000};

    for (int alphabet_size = 2; alphabet_size < ALPHABET_SIZE; ++alphabet_size) {
        for (int i = 0; i < 11; ++i) {
            int length = lengths[i];
            printf("%d %d\n", alphabet_size, length);
            for (int exp = 0; exp < EXPERIMENTS; ++exp) {
                printf("%d ", duval(rand_string(text, length, alphabet_size), buffer));
            }
            printf("\n");
        }
    }
    free(buffer);
}

void save_ecoli_results() {
    freopen("/Users/alonger/HSE/stringology/strlib/ecoli.txt", "wt", stdout);
    freopen("/Users/alonger/HSE/stringology/strlib/ecoli.fasta", "rt", stdin);
    int * buffer = calloc(LENGTH + 1, sizeof(int));
    char * text = calloc(2 * LENGTH + 1, sizeof(char));
    char * text_part = calloc(LENGTH + 1, sizeof(char));
    char * read_buffer = calloc(LENGTH + 1, sizeof(char));
    for (int exp = 0; exp < EXPERIMENTS; ++exp) {
        int text_len = 0;
        memset(text, 0, (2 * LENGTH + 1) * sizeof(char));
        memset(text_part, 0, (LENGTH + 1) * sizeof(char));
        while (text_len < LENGTH) {
            scanf("%s\n", read_buffer);
            strcat(text, read_buffer);
            text_len += strlen(read_buffer);
        }
        text_part[0] = text[0];
        for (int i = 1; i < LENGTH; ++i) {
            text_part[i] = text[i];
            printf("%d %d\n", i + 1, duval(text_part, buffer));
        }
    }
    free(buffer);
}

int main(int argc, char** argv) {
    save_random_strings_results_for_lengths();
    return 0;
}
