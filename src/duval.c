#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>
#include <stdbool.h>
#include <unistd.h>

/**
* This is an implementation of the Duval algorithm
*/
int duval(const char * text, int * output){
    size_t n = strlen(text);
    int h = 0;
    int words_count = 0;
    while (h < n) {
        int i = h;
        int j = h + 1;
        while (text[j] >= text[i]) {
            if (text[j] > text[i])
                i = h;
            else
                i++;
            j++;
        }
        while (h <= i) {
            output[words_count++] = h;
            h += j - i;
        }
    }
    return words_count;
}

/**
* Build Lyndon decomposition naively
*/
int naive_lyndon_decomposition(const char * text, int * output) {
    size_t n = strlen(text);

    if (n == 1) {
        output[0] = 0;
        return 1;
    }

    int * next_word = calloc(n, sizeof(int));

    // build first (not Lyndon) decomposition of size n
    for (int i = 0; i < n; ++i) {
        next_word[i] = i + 1;
    }

    // concatenate consequent factors if first is less than the second
    bool progress = true;
    while (progress) {
        progress = false;
        int first_word_start = 0;
        int second_word_start = next_word[first_word_start];
        while (second_word_start < n) {
            int third_word_start = next_word[second_word_start];

            int first_word_index = first_word_start;
            int second_word_index = second_word_start;
            while (first_word_index < second_word_start && second_word_index < third_word_start && text[first_word_index] == text[second_word_index]) {
                first_word_index++;
                second_word_index++;
            }

            if (second_word_index < third_word_start && (first_word_index == second_word_start || text[first_word_index] < text[second_word_index])) {
                progress = true;
                next_word[first_word_start] = third_word_start;
            }

            first_word_start = next_word[first_word_start];
            second_word_start = (first_word_start < n) ? next_word[first_word_start] : (int)n;
        }
    }
    int word_count = 0;
    int word_start = 0;
    while (word_start < n) {
        output[word_count++] = word_start;
        word_start = next_word[word_start];
    }

    free(next_word);
    return word_count;
}


/**
 * Test Duval algorithm implementation on random data
 */
void test_duval() {
    int tests = 1000;
    int text_length = 100000;
    int alphabet_size = 2;
    char * text = calloc(text_length + 1, sizeof(char));
    int * duval_output = calloc(text_length + 1, sizeof(int));
    int * naive_output = calloc(text_length + 1, sizeof(int));
    for (int i = 0; i < tests; ++i) {
        printf("Test %d...\n", i + 1);

        // fill text with random letters
        for (int c = 0; c < text_length; ++c) {
            text[c] = (char) (rand() % alphabet_size + 1);
        }
        text[text_length] = 0;

        // test Duval algorithm duval_output
        int duval_factor_count = duval(text, duval_output);
        int naive_factor_count = naive_lyndon_decomposition(text, naive_output);
        assert(duval_factor_count == naive_factor_count);
        for (int factor_number = 0; factor_number < duval_factor_count; ++factor_number) {
            assert(duval_output[factor_number] == naive_output[factor_number]);
        }
        printf("OK (factors: %d)\n", duval_factor_count);
    }
    printf("----------\n");
    printf("Tests passed: %d\n", tests);
    free(text);
    free(duval_output);
}



void usage(const char * program_name) {
    printf("Usage: %s [-h] TEXT\n", program_name);
    printf("Build Lyndon decomposition for text\n");
    printf("The output contains starting positions of decomposition factors\n\n");
    printf(" -h  Print decomposition in readable format\n");
    printf(" -t  Test Duval algorithm implementation instead of TEXT processing\n");
}


int main(int argc, char** argv) {
    int c;
    bool human_friendly = false;
    bool test = false;
    opterr = 1;
    while ((c = getopt (argc, argv, "ht")) != -1)
        switch (c)
        {
            case 'h':
                human_friendly = true;
                break;
            case 't':
                test = true;
                break;
            case '?':
            case ':':
                return -1;
            default:
                usage(argv[0]);
                return -1;
        }
    if (test) {
        test_duval();
        return 0;
    }
    if (optind >= argc) {
        usage(argv[0]);
        return -1;
    }
    char * text = argv[optind];
    int n = strlen(text);

    int * output = calloc(n, sizeof(int));

    int word_count = duval(text, output);

    printf("FACTOR COUNT: %d\n", word_count);
    printf("FACTOR POSITIONS:\n");

    for (int i = 0; i < word_count; ++i) {
        printf("%d ", output[i]);
    }
    printf("\n");
    if (human_friendly) {
        int next_factor = 1;
        for (int i = 0; i < n; ++i) {
            if (next_factor < word_count && i == output[next_factor]) {
                printf("|");
                next_factor++;
            }
            printf("%c", text[i]);
        }
        printf("\n");
    }

    return 0;
}
