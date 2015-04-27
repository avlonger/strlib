#include <stdlib.h>
#include <string.h>
#include <stdio.h>


/**
* Build border array for text
*/
void border(const char * text, int * border) {
    size_t n = strlen(text);
    border[0] = 0;
    int j = 0;
    for (int i = 1; i < n; ++i) {
        j = border[i - 1];
        while (j > 0 && text[i] != text[j]) {
            j = border[j - 1];
        }
        if (text[i] == text[j])
            j++;
        border[i] = j;
    }
}


/**
* Implementation of the Knuth Morris Pratt algorithm
*/
int kmp(const char * pattern, const char * text, int * output){
    size_t m = strlen(pattern), n = strlen(text);
    int * pattern_border = calloc(m, sizeof(int));
    border(pattern, pattern_border);
    int i = 0, k = 0;
    for (int j = 0; j < n; ++j) {
        while (i > 0 && pattern[i] != text[j])
            i = pattern_border[i - 1];
        if (pattern[i] == text[j])
            i++;
        if (i >= m) {
            output[k++] = j - i + 1;
            i = pattern_border[i - 1];
        }
    }
    free(pattern_border);
    return k;
}


int main(int argc, char** argv) {
    if (argc < 3) {
        printf("Usage: %s PATTERN TEXT\n", argv[0]);
        return 1;
    }
    char * pattern = argv[1];
    char * text = argv[2];

    int * output = calloc(strlen(text), sizeof(int));

    int occ = kmp(pattern, text, output);

    printf("OCCURENCES: %d\n", occ);

    for (int i = 0; i < occ; ++i) {
        printf("%d ", output[i]);
    }

    printf("\n");

    return 0;
}
