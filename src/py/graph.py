from collections import defaultdict, namedtuple

import pylab as pl
import matplotlib.font_manager as fm


def save_me(name, font, clear=True):
    set_font(font)
    pl.tight_layout()
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

Entity = namedtuple('Entity', ['name', 'readable_name'])

if __name__ == '__main__':

    font = fm.FontProperties(fname='/Users/alonger/HSE/cmunrm.ttf', size=19)

    entities = [
        Entity('borderless', 'unbordered factor'),
        Entity('borderless_prefix', 'unbordered prefix'),
    ]

    for name, verbose_name in entities:

        counts = defaultdict(lambda: defaultdict(int))

        with open('max_{}.txt'.format(name)) as fd:
            for line in fd:
                alphabet_size, length, val = map(int, line.strip().split())
                counts[alphabet_size][length] = val

        for
        # save figures for binary alphabet
        if name == 'border':
            keys2 = sorted(counts[2])
            values2 = map(lambda x: counts[2].get(x) * 1.0 / 2 ** x, keys2)
            pl.plot(keys2, values2, label='$\sigma = 2$', color='k')
            pl.axes().set_xlim(min(keys2), max(keys2))
            save_me('n_minus_min_period_2.pdf', font)
        else:
            keys2 = sorted(counts[2])
            values2 = map(lambda x: x - counts[2].get(x) * 1.0 / 2 ** x, keys2)
            pl.plot(keys2, values2, label='$\sigma = 2$', color='k')
            pl.axes().set_xlim(min(keys2), max(keys2))
            save_me('n_minus_max_{}_2.pdf'.format(name), font)

        if name == 'border':
            for i, alphabet in enumerate([2, 3, 4, 5]):
                keys = sorted(counts[alphabet])[:17]
                values = map(lambda x: counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
                pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet), color='k', dashes=dashes[i])
            pl.axes().set_xlim(min(keys), max(keys))
            pl.legend(loc=2, prop=font)
            save_me('n_minus_min_period_2_3_4_5.pdf', font)
        else:
            for i, alphabet in enumerate([2, 3, 4, 5]):
                keys = sorted(counts[alphabet])[:17]
                values = map(lambda x: x - counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
                pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet), color='k', dashes=dashes[i])
            pl.axes().set_xlim(min(keys), max(keys))
            pl.legend(loc=2, prop=font)
            save_me('n_minus_max_{}_2_3_4_5.pdf'.format(name), font)


# def save_me(name, font, clear=True):
#     set_font(font)
#     pl.savefig('final_figs/' + name)
#     pl.grid()
#     pl.savefig('final_figs/' + name[:-4] + '.png')
#     if clear:
#         pl.axes().clear()
#
#
# def set_font(font):
#     pl.xlabel('String length', fontproperties=font)
#     pl.tight_layout()
#     for label in pl.axes().get_xticklabels():
#         label.set_fontproperties(font)
#     for label in pl.axes().get_yticklabels():
#         label.set_fontproperties(font)
#
# dashes = [
#     [],
#     [5, 5],
#     [5, 3, 1, 3],
#     [1, 1],
# ]
#
# if __name__ == '__main__':
#
#     font = fm.FontProperties(fname='/Users/alonger/HSE/cmunrm.ttf', size=14)
#
#     for name in ['border', 'borderless']:
#
#         counts = defaultdict(lambda: defaultdict(int))
#
#         with open('max_{}.txt'.format(name)) as fd:
#             for line in fd:
#                 alphabet_size, length, val = map(int, line.strip().split())
#                 counts[alphabet_size][length] = val
#
#         # save figures for binary alphabet
#         if name == 'border':
#             keys2 = sorted(counts[2])
#             values2 = map(lambda x: counts[2].get(x) * 1.0 / 2 ** x, keys2)
#             pl.plot(keys2, values2, label='$\sigma = 2$')
#             pl.axes().set_xlim(min(keys2), max(keys2))
#             pl.title('Average difference between the length $n$ of a string\n'
#                      'and its minimal period for alphabet of size $\sigma = 2$\n', fontproperties=font)
#             save_me('n_minus_min_period_2.pdf', font)
#         else:
#             values2 = map(lambda x: x - counts[2].get(x) * 1.0 / 2 ** x, keys2)
#             pl.plot(keys2, values2, label='$\sigma = 2$')
#             pl.axes().set_xlim(min(keys2), max(keys2))
#             pl.title('Average difference between the length $n$ of a string and the length\n'
#                      'of its maximal borderless factor for alphabet of size $\sigma = 2$\n', fontproperties=font)
#             save_me('n_minus_max_{}_2.pdf'.format(name), font)
#
#         if name == 'border':
#             for i, alphabet in enumerate([2, 3, 4, 5]):
#                 keys = sorted(counts[alphabet])[:17]
#                 values = map(lambda x: counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
#                 pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet))
#             pl.axes().set_xlim(min(keys), max(keys))
#             pl.legend(loc=2, prop=font)
#             pl.title('Average difference between the length $n$ of a string \n '
#                      'and its minimal period for alphabets of size $\sigma = \{2,3,4,5\}$\n', fontproperties=font)
#             save_me('n_minus_min_period_2_3_4_5.pdf', font)
#         else:
#             for i, alphabet in enumerate([2, 3, 4, 5]):
#                 keys = sorted(counts[alphabet])[:17]
#                 values = map(lambda x: x - counts[alphabet].get(x) * 1.0 / alphabet ** x, keys)
#                 pl.plot(keys, values, label='$\sigma = {}$'.format(alphabet))
#             pl.title('Average difference between the length $n$ of a string and the length\n'
#                      'of its maximal borderless factor for alphabets of size $\sigma = \{2,3,4,5\}$\n', fontproperties=font)
#             pl.axes().set_xlim(min(keys), max(keys))
#             pl.legend(loc=2, prop=font)
#             save_me('n_minus_max_{}_2_3_4_5.pdf'.format(name), font)