#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include <stdio.h>
#include <stdbool.h>
#include "algo/borderless.h"
#include "algo/kmp.h"


// some buffers
char * CHAR_BUFFER;
int * INT_BUFFER;
int (* FUNCTION)();
char ALPHABET = 2;
char MINIMAL_CHAR = 1;
int LENGTH = 2;
bool TRACE = false;

void usage(const char * program_name) {
    printf("Usage: %s [options] ALGORITHM\n", program_name);
    printf("Calculate some value for words range\n");
    printf("Algorithms:\n");
    printf("MINPERIOD      find minimal period of a word\n");
    printf("MAXBORDERLESS  find longest borderless subword\n\n");
    printf("Options:\n");
    printf(" -l  Find average value for all words of given length\n");
    printf(" -s  Alphabet size (default: 2)\n");
    printf(" -t  Trace\n");
}

int do_for_all_words(int position) {
    int total = 0;
    int value = 0;
    char i;
    for (i = MINIMAL_CHAR; i <= ALPHABET; ++i) {
        CHAR_BUFFER[position] = i;

        if (position < LENGTH - 1) {
            total += do_for_all_words(position + 1);
        } else {
            value = FUNCTION();

            if (TRACE) {
                printf("%s\t%d\n", CHAR_BUFFER, value);
            }

            total += value;
        }
    }

    return total;
}


int minimal_period() {
    border(CHAR_BUFFER, INT_BUFFER);
    return LENGTH - INT_BUFFER[LENGTH - 1];
}


int longest_borderless() {
    return longest_borderless_subword(CHAR_BUFFER, INT_BUFFER);
}


int main(int argc, char** argv) {
    int c = 0;
    opterr = 1;
    while ((c = getopt(argc, argv, "tl:s:")) != -1)
        switch (c)
        {
            case 's':
                ALPHABET = (char) atoi(optarg);
                break;
            case 'l':
                LENGTH = atoi(optarg);
                break;
            case 't':
                TRACE = true;
                break;
            case '?':
            case ':':
                return -1;
            default:
                usage(argv[0]);
                return -1;
        }

    if (TRACE) {
        MINIMAL_CHAR = 'A';
        ALPHABET += 'A' - 1;
    }

    if (optind >= argc) {
        usage(argv[0]);
        return -1;
    }

    CHAR_BUFFER = calloc((size_t) LENGTH + 1, sizeof(char));
    INT_BUFFER = calloc((size_t) LENGTH + 1, sizeof(int));
    CHAR_BUFFER[LENGTH] = 0;

    if (strcmp(argv[optind], "MINPERIOD") == 0) {
        FUNCTION = minimal_period;
    } else if (strcmp(argv[optind], "MAXBORDERLESS") == 0) {
        FUNCTION = longest_borderless;
    }
    double count = pow((double) (TRACE) ? ALPHABET - 'A' + 1: ALPHABET, (double) LENGTH);
    printf("%.10f\n", (double) do_for_all_words(0) / count);

    free(CHAR_BUFFER);
    free(INT_BUFFER);
}