#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>
#include "algo/duval.h"

void usage(const char * program_name) {
    printf("Usage: %s [-h] [-f FILENAME | TEXT]\n\n", program_name);
    printf("Build Lyndon decomposition for text\n");
    printf(" -h  Print decomposition in readable format\n");
    printf(" -f  Filename (not supported yet)\n");
}


int main(int argc, char** argv) {
    int c;
    char * filename = NULL;
    bool human_friendly = false;
    opterr = 1;
    while ((c = getopt (argc, argv, "hf:")) != -1)
        switch (c)
        {
            case 'f':
                filename = (char *) optarg[0];
                break;
            case 'h':
                human_friendly = true;
                break;
            case '?':
            case ':':
            default:
                usage(argv[0]);
                return -1;
        }
    if (optind >= argc) {
        usage(argv[0]);
        return -1;
    }
    char * text = argv[optind];
    int n = strlen(text);

    int * output = calloc(n, sizeof(int));

    int word_count = duval(text, output);

    printf("WORD COUNT: %d\n", word_count);

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
