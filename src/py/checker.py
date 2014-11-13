# -*- coding: utf-8 -*-
"""
"""
import string
import subprocess
from random import choice

import pylab as pl


EXPERIMENTS = 1000
LENGTH = 1000
AVAILABLE_LETTERS = string.lowercase + string.uppercase + string.digits


def random_string(length, alphabet_size):
    return ''.join(choice(AVAILABLE_LETTERS[:alphabet_size]) for _ in xrange(length))


def is_lyndon_word(word):
    for i in xrange(1, len(word)):
        if word >= word[i:]:
            return False
    return True


def is_lyndon_decomposition(word, factor_positions):
    slice_positions = list(factor_positions)
    slice_positions.append(len(slice_positions))
    factors = []

    # testing if each factor is Lyndon-word
    for i, position in enumerate(slice_positions[:-1]):
        factor = word[position:slice_positions[i + 1]]
        if not is_lyndon_word(factor):
            return False
        factors.append(factor)

    # testing if each factor is not less than the next factor
    for i, factor in enumerate(factors[:-1]):
        if not factor >= factors[i + 1]:
            return False

    return True

if __name__ == '__main__':
    print 'Testing duval algorithm in series of {} experiments...'.format(EXPERIMENTS)
    for _ in xrange(EXPERIMENTS):
        text = random_string(LENGTH, len(AVAILABLE_LETTERS))
        process = subprocess.Popen(['../../bin/duval', text], stdout=subprocess.PIPE)
        output = process.stdout.read().strip()
        factor_positions = map(int, output.splitlines()[1].split())
        assert is_lyndon_decomposition(text, factor_positions)
    print 'OK'

    alphabet_sizes = range(2, len(AVAILABLE_LETTERS) + 1)
    for length in [10, 100, 500, 999]:
        average_values = []
        print 'Plotting for length: {}'.format(length)
        for alphabet_size in alphabet_sizes:
            values = []
            for _ in xrange(EXPERIMENTS / 10):
                text = random_string(length, alphabet_size)
                process = subprocess.Popen(['../../bin/duval', text], stdout=subprocess.PIPE)
                output = process.stdout.read().strip()
                words_count = int(output.splitlines()[0].split()[-1].strip())
                values.append(words_count)
            average_values.append(sum(values) * 1.0 / len(values))
        pl.plot(alphabet_sizes, average_values)
        pl.title('Text length = {}'.format(length))
        pl.xlabel('Alphabet size')
        pl.ylabel('Factors count')
        pl.savefig('../../results/py-length-{}.png'.format(length))
        pl.clf()
