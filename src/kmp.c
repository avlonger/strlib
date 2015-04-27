#include <stdlib.h>
#include <string.h>
#include <assert.h>
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


/**
 * Test KMP implementation on random data
 */
void test_kmp() {
    int tests = 1000;
    int text_length = 100000;
    int pattern_length = 10;
    int alphabet_size = 2;
    char * text = calloc(text_length + 1, sizeof(char));
    char * pattern = calloc(pattern_length + 1, sizeof(char));
    int * output = calloc(text_length + 1, sizeof(int));
    for (int i = 0; i < tests; ++i) {
        printf("Test %d...\n", i + 1);

        // fill text with random letters
        for (int c = 0; c < text_length; ++c) {
            text[c] = (char) (rand() % alphabet_size + 1);
        }
        text[text_length] = 0;

        // fill pattern with random letters
        for (int c = 0; c < pattern_length; ++c) {
            pattern[c] = (char) (rand() % alphabet_size + 1);
        }
        pattern[pattern_length] = 0;

        // test kmp output
        int occ_count = kmp(pattern, text, output);
        int occ_number = 0;
        unsigned long position = 0;
        char * strstr_result = strstr(text, pattern);
        while (strstr_result != NULL) {
            assert(occ_number < occ_count);
            position = strstr_result - text;
            assert(position == output[occ_number++]);
            strstr_result = strstr(strstr_result + 1, pattern);
        }
        assert(occ_number == occ_count);
        printf("OK (occ: %d)\n", occ_count);
    }
    printf("----------\n");
    printf("Tests passed: %d\n", tests);
    free(pattern);
    free(text);
    free(output);
}


int main(int argc, char** argv) {
    if (argc == 2 && strcmp(argv[1], "-t") == 0) {
        test_kmp();
        return 0;
    }

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
