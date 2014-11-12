#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

/**
* This is an implementation of the Knuth Morris Pratt algorithm
* TODO: more comments and docs
*/
int kmp(const char * pattern, const char * text, int * output){
    // build border array
    size_t m = strlen(pattern);
    int border[m];
    int i, j, k;
    i = 0;
    j = border[0] = -1;
    while (i < m) {
        while (j > -1 && pattern[i] != pattern[j])
            j = border[j];
        i++;
        j++;
        if (i<m && pattern[i] == pattern[j])
            border[i] = border[j];
        else
            border[i] = j;
    }

    // now we do pattern matching
    size_t n = strlen(text);
    i = j = k = 0;
    while (j < n) {
        while (i > -1 && pattern[i] != text[j])
            i = border[i];
        i++;
        j++;
        if (i >= m) {
            output[k++] = j - i;
            i = border[i];
        }
    }
    return k;
}
