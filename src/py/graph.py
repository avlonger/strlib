import csv
from collections import defaultdict

import pylab as pl
import numpy as np


def func(n, c):
    return c * n / np.log2(n)

if __name__ == '__main__':
    # a lot of hard-coded numbers here
    counts = defaultdict(lambda: defaultdict(float))
    print 'Reading...'
    with open('min_period_max_borderless_diff.txt') as fd:
        reader = csv.reader(fd, delimiter='\t')
        reader.next()
        try:
            while True:
                alphabet_size, length, diff, _ = reader.next()
                alphabet_size = int(alphabet_size)
                length = int(length)
                diff = float(diff)
                if diff < 100000000:
                    counts[alphabet_size][length] += diff
        except StopIteration:
            pass

        for alphabet_size in [5]:
            lengths = sorted(counts[alphabet_size])
            values = map(lambda x: counts[alphabet_size].get(x) * 1.0 / alphabet_size ** x, lengths)
            print lengths, values
            pl.plot(lengths, values, label='Diff- $\sigma = {}$'.format(alphabet_size))
        pl.legend(loc=2)
        pl.grid()
        pl.xlabel('Text length')
        pl.savefig('../../results/diff_5.png')
        pl.savefig('min_period_max_borderless_diff.png')

    # with open('../../result_alphabets_borderless.txt') as fd:
    #     reader = csv.reader(fd, delimiter=' ')
    #     try:
    #         while True:
    #             alphabet_size, length = map(int, reader.next())
    #             all_counts = map(int, reader.next()[:-1])
    #             counts[alphabet_size][length] = np.average(all_counts)
    #     except StopIteration:
    #         pass
    #
    #     for alphabet_size in [2, 100]:
    #         lengths = range(2, 349)
    #         values = map(counts[alphabet_size].get, lengths)
    #         pl.plot(lengths, values, label='Max borderless $\sigma = {}$'.format(alphabet_size))
    #     pl.legend(loc=4)
    #     pl.grid()
    #     pl.xlabel('Text length')
    #     pl.savefig('../../results/alphabets_max_factor_borderless.png')
    #     pl.clf()



        # step = 10
        # lengths = range(2, 50) + range(50, 1001, step)
        # for alphabet_size in [2, 3, 5, 10, 100]:
        #     values = []
        #     for i, length in enumerate(lengths[:-1]):
        #         values.append(np.average(
        #             map(counts[alphabet_size].get, xrange(length, lengths[i + 1]))
        #         ))
        #     pl.plot(range(2, 50) + range(55, 1001, step), values, label='$\sigma = {}$'.format(alphabet_size))
        # pl.legend(loc=4)
        # pl.xlabel('Text length')
        # pl.ylabel('Factors count')
        # pl.savefig('../../results/alphabets-borderless-smooth.png')
        # pl.clf()
        #
        # for length in [10, 100] + range(200, 1001, 200):
        #     sizes = sorted(counts)
        #     pl.plot(sizes, map(lambda x: counts[x][length], sizes), label='$n = {}$'.format(length))
        # pl.legend(loc=4)
        # pl.xlabel('Alphabet size')
        # pl.ylabel('Factors count')
        # pl.savefig('../../results/lengths_borderless.png')
        # pl.clf()
        #
        # for length in [10, 100, 500, 1000]:
        #     sizes = sorted(counts)
        #     pl.plot(sizes, map(lambda x: counts[x][length], sizes))
        #     pl.title('Text length = {}'.format(length))
        #     pl.xlabel('Alphabet size')
        #     pl.ylabel('Factors count')
        #     pl.savefig('../../results/length-borderless-{}.png'.format(length))
        #     pl.clf()
        #
        # for length in [10, 100, 500, 1000]:
        #     step = 10
        #     sizes = range(2, 10) + range(10, 101, step)
        #     values = []
        #     for i, size in enumerate(sizes[:-1]):
        #         values.append(np.average(
        #             map(lambda x: counts[x][length], xrange(size, sizes[i + 1]))
        #         ))
        #     pl.plot(range(2, 10) + range(15, 101, 10), values)
        #     pl.title('Text length = {}'.format(length))
        #     pl.xlabel('Alphabet size')
        #     pl.ylabel('Factors count')
        #     pl.savefig('../../results/smooth-length-borderless-{}.png'.format(length))
        #     pl.clf()

    # genom_counts = defaultdict(list)
    # with open(sys.argv[2]) as fd:
    #     reader = csv.reader(fd, delimiter=' ')
    #     for line in reader:
    #         length, count = map(int, line)
    #         genom_counts[length].append(count)
    #
    #     for length, counts_list in genom_counts.iteritems():
    #         genom_counts[length] = sum(counts_list) * 1.0 / len(counts_list)
    #
    #     genom_lengths = sorted(genom_counts)
    #
    #     pl.plot(genom_lengths, map(genom_counts.get, genom_lengths))
    #     pl.title('E.coli')
    #     pl.xlabel('Text length')
    #     pl.ylabel('Factors count')
    #     pl.savefig('../../results/ecoli.png')
    #     pl.clf()
    #
    #     # plot factors count for alphabet size == 4
    #     # to compare it to E.coli
    #     lengths = sorted(counts[4])
    #     pl.plot(lengths, map(counts[4].get, lengths), 'b', label='Random words')
    #     pl.plot(genom_lengths, map(genom_counts.get, genom_lengths), 'r', label='E.coli')
    #     pl.title('E.coli and random words comparison')
    #     pl.xlabel('Text length')
    #     pl.ylabel('Factors count')
    #     pl.savefig('../../results/ecoli-compare.png')



