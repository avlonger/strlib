#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

/**
* This is an implementation of Duval algorithm
* TODO: more comments and docs
*/
int duval(const char * text, int * output){
    return 0;
}

/**
* Naive Lyndon decomposition construction
* TODO: more comments and docs
*/
int naive_lyndon_decomposition(const char * text, int * output) {
    unsigned int n = strlen(text);

    if (n == 1) {
        output[0] = 0;
        return 1;
    }

    int * next_word = calloc(n, sizeof(int));

    // build first (not Lyndon) decomposition of size n
    for (int i = 0; i < n; ++i) {
        next_word[i] = i + 1;
    }

    // concatenate consequent lyndon-words if first is less than the second
    bool progress = true;
    while (progress) {
        progress = false;
        int first_word_start = 0;
        int second_word_start = next_word[first_word_start];
        while (second_word_start < n) {
            int third_word_start = next_word[second_word_start];
            int first_word_index = first_word_start;
            int second_word_index = second_word_start;
            for (; first_word_index < second_word_start && second_word_index < third_word_start && text[first_word_index] == text[second_word_index]; first_word_index++, second_word_index++);
            if (second_word_index < third_word_start && (first_word_index == second_word_start || text[first_word_index] < text[second_word_index])) {
                progress = true;
                next_word[first_word_start] = third_word_start;
            }
            first_word_start = next_word[first_word_start];
            second_word_start = (first_word_start < n) ? next_word[first_word_start] : n;
        }
    }
    int word_count = 0;
    int word_start = 0;
    while (word_start < n) {
        output[word_count++] = word_start;
        word_start = next_word[word_start];
    }
    return word_count;
}

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