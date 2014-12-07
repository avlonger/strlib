# -*- coding: utf-8 -*-
"""
"""
import csv
import argparse
import datetime
import subprocess
import multiprocessing as mp
from multiprocessing.pool import ThreadPool


def worker(args):
    size, length, algo, binary = args
    p = subprocess.Popen([binary, '-s', str(size), '-a', str(length), algo], stdout=subprocess.PIPE)
    p.wait()
    return size, length, float(p.stdout.read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate some statistics')
    parser.add_argument('-a', '--alphabets', nargs='*', type=int,
                        help='Alphabet sizes for which calculate statistics')
    parser.add_argument('-l', '--lengths', nargs='*', type=int,
                        help='Word lengths for which calculate statistics')
    parser.add_argument('-c', '--cpu_count', type=int,
                        help='Processor cores to use (default: all available)',
                        default=mp.cpu_count())
    parser.add_argument('-f', '--filename', help='Output file')
    parser.add_argument('-b', '--binary', help='Binary to use', default='../../bin/experiment')
    parser.add_argument('algo', metavar='ALGORITHM',
                        choices=('MINPERIOD', 'MAXBORDERLESS', 'PERIOD_BORDERLESS_DIFF'))
    options = parser.parse_args()

    pool = ThreadPool(options.cpu_count)

    tasks = []
    for alphabet_size in options.alphabets:
        for length in options.lengths:
            tasks.append((alphabet_size, length, options.algo, options.binary))

    if options.filename is None:
        options.filename = '{}-{}.txt'.format(options.algo, datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S'))

    with open(options.filename, 'w') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerow(('ALPHABET', 'LENGTH', options.algo))
        for size, length, result in pool.imap_unordered(worker, tasks):
            writer.writerow((size, length, '{:.10f}'.format(result)))
            out_file.flush()
