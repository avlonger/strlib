# -*- coding: utf-8 -*-
"""
"""
import csv
import subprocess
from multiprocessing.pool import ThreadPool


def worker(args):
    size, length = args
    p = subprocess.Popen(['../../bin/experiment', '-s', str(size), '-a', str(length), 'PERIOD_BORDERLESS_DIFF'], stdout=subprocess.PIPE)
    p.wait()
    return size, length, float(p.stdout.read())

if __name__ == '__main__':
    ALPHABET_SIZE = 2
    MAX_LENGTH = 30
    pool = ThreadPool(5)
    tasks = [(ALPHABET_SIZE, length) for length in xrange(1, MAX_LENGTH + 1)]

    with open('minimal_period.txt', 'w') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerow(('ALPHABET', 'LENGTH', 'MINPERIOD'))
        for size, length, result in pool.imap_unordered(worker, tasks):
            writer.writerow((size, length, result))
            out_file.flush()
