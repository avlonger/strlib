import csv
import sys
from collections import defaultdict

import pylab as pl

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: {} RANDOM_FILENAME GENOM_FILENAME'.format(sys.argv[0])
        sys.exit(1)
    counts = defaultdict(lambda: defaultdict(float))
    with open(sys.argv[1]) as fd:
        reader = csv.reader(fd, delimiter=' ')
        try:
            while True:
                alphabet_size, length = map(int, reader.next())
                all_counts = map(int, reader.next()[:-1])
                counts[alphabet_size][length] = sum(all_counts) * 1.0 / len(all_counts)
        except StopIteration:
            pass

        for alphabet_size in [2, 3, 5, 10, 50, 127]:
            lengths = sorted(counts[alphabet_size])
            pl.plot(lengths, map(counts[alphabet_size].get, lengths))
            pl.title('Alphabet size = {}'.format(alphabet_size))
            pl.xlabel('Text length')
            pl.ylabel('Factors count')
            pl.savefig('../../results/alphabet-{}.png'.format(alphabet_size))
            pl.clf()

        for length in [10, 100, 500, 999]:
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



