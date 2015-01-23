# -*- coding: utf-8 -*-
"""
"""
import pylab as pl
import numpy as np



if __name__ == '__main__':
    with open('time.txt') as fd:
        lines = fd.read().strip().splitlines()
        super_naive = [l.split()[1:] for l in lines if l.startswith('MAXBORDERLESS_SUPER_NAIVE') and int(l.split()[1]) < 101]
        border = [l.split()[1:] for l in lines if l.startswith('MAXBORDERLESS_BORDER_FAST') and int(l.split()[1]) < 101]

        pl.plot(*zip(*border), linewidth=2, label='Border Array')
        pl.plot(*zip(*super_naive), linewidth=2, label='Super Naive')

        pl.xlabel('String length')
        pl.ylabel('Time')
        pl.legend(loc=2)
        pl.grid()
        pl.savefig('time.png')
