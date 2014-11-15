import csv
import sys
from collections import defaultdict

import pylab as pl
import numpy as np
from scipy.interpolate import spline

if __name__ == '__main__':
    counts = defaultdict(lambda: defaultdict(float))
    print 'Reading...'
    with open('../../result.txt') as fd:
        reader = csv.reader(fd, delimiter=' ')
        try:
            while True:
                alphabet_size, length = map(int, reader.next())
                all_counts = map(int, reader.next()[:-1])
                counts[alphabet_size][length] = np.average(all_counts)
        except StopIteration:
            pass

        for alphabet_size in [2, 3, 5, 10, 100]:
            lengths = sorted(counts[alphabet_size])
            pl.plot(lengths, map(counts[alphabet_size].get, lengths), label='$\sigma = {}$'.format(alphabet_size))
        pl.legend(loc=4)
        pl.xlabel('Text length')
        pl.ylabel('Factors count')
        pl.savefig('../../results/alphabets.png')
        pl.clf()

        step = 10
        lengths = range(2, 50) + range(50, 1001, step)
        for alphabet_size in [2, 3, 5, 10, 100]:
            print 'Alphabet size:', alphabet_size
            values = []
            for i, length in enumerate(lengths[:-1]):
                values.append(np.average(
                    map(counts[alphabet_size].get, xrange(length, lengths[i + 1]))
                ))
            pl.plot(range(2, 50) + range(55, 1001, step), values, label='$\sigma = {}$'.format(alphabet_size))
        pl.legend(loc=4)
        pl.xlabel('Text length')
        pl.ylabel('Factors count')
        pl.savefig('../../results/alphabets-smooth.png')
        pl.clf()

        for length in [10, 100, 500, 999]:
            print 'Plotting for word length {}...'.format(length)
            sizes = sorted(counts)
            pl.plot(sizes, map(lambda x: counts[x][length], sizes))
            pl.title('Text length = {}'.format(length))
            pl.xlabel('Alphabet size')
            pl.ylabel('Factors count')
            pl.savefig('../../results/length-{}.png'.format(length))
            pl.clf()

    genom_counts = defaultdict(list)
    with open(sys.argv[2]) as fd:
        reader = csv.reader(fd, delimiter=' ')
        for line in reader:
            length, count = map(int, line)
            genom_counts[length].append(count)

        for length, counts_list in genom_counts.iteritems():
            genom_counts[length] = sum(counts_list) * 1.0 / len(counts_list)

        genom_lengths = sorted(genom_counts)

        pl.plot(genom_lengths, map(genom_counts.get, genom_lengths))
        pl.title('E.coli')
        pl.xlabel('Text length')
        pl.ylabel('Factors count')
        pl.savefig('../../results/ecoli.png')
        pl.clf()

        # plot factors count for alphabet size == 4
        # to compare it to E.coli
        lengths = sorted(counts[4])
        pl.plot(lengths, map(counts[4].get, lengths), 'b', label='Random words')
        pl.plot(genom_lengths, map(genom_counts.get, genom_lengths), 'r', label='E.coli')
        pl.title('E.coli and random words comparison')
        pl.xlabel('Text length')
        pl.ylabel('Factors count')
        pl.savefig('../../results/ecoli-compare.png')



