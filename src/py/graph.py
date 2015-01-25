from collections import defaultdict

import pylab as pl
import matplotlib.font_manager as fm


def save_me(name, font, clear=True):
    set_font(font)
    pl.savefig('final_figs/' + name)
    pl.savefig('final_figs/' + name[:-4] + '.png')
    if clear:
        pl.axes().clear()


def set_font(font):
    pl.xlabel('String length', fontproperties=font)
    for label in pl.axes().get_xticklabels():
        label.set_fontproperties(font)
    for label in pl.axes().get_yticklabels():
        label.set_fontproperties(font)

dashes = [
    [],
    [5, 5],
    [5, 3, 1, 3],
    [1, 1],
]

if __name__ == '__main__':

    font = fm.FontProperties(fname='/Users/alonger/HSE/cmunrm.ttf', size=14)

    for name in ['border', 'borderless']:

        counts = defaultdict(lambda: defaultdict(int))

        with open('max_{}.txt'.format(name)) as fd:
            for line in fd:
                alphabet_size, length, val = map(int, line.strip().split())
                counts[alphabet_size][length] = val

        # save figures for binary alphabet
        keys2 = sorted(counts[2])
        values2 = map(lambda x: counts[2].get(x) * 1.0 / 2 ** x, keys2)
        pl.plot(keys2, values2, label='$\sigma = 2$', color='k')
        pl.axes().set_xlim(min(keys2), max(keys2))
        save_me('max_{}_2.pdf'.format(name), font)

        values2 = map(lambda x: x - counts[2].get(x) * 1.0 / 2 ** x, keys2)
        pl.plot(keys2, values2, label='$\sigma = 2$', color='k')
        pl.axes().set_xlim(min(keys2), max(keys2))
        save_me('n_minus_max_{}_2.pdf'.format(name), font)

        # save figures for all except 2
        for i, alphabet in enumerate([2, 3, 4, 5]):
            keys = sorted(counts[alphabet])[:17]
            values = map(lambda x: counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
            pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet), color='k', dashes=dashes[i])
        pl.axes().set_xlim(min(keys), max(keys))
        pl.legend(loc=2, prop=font)
        save_me('max_{}_2_3_4_5.pdf'.format(name), font)

        for i, alphabet in enumerate([2, 3, 4, 5]):
            keys = sorted(counts[alphabet])[:17]
            values = map(lambda x: x - counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
            pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet), color='k', dashes=dashes[i])
        pl.axes().set_xlim(min(keys), max(keys))
        pl.legend(loc=2, prop=font)
        save_me('n_minus_max_{}_2_3_4_5.pdf'.format(name), font)