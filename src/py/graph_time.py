# -*- coding: utf-8 -*-
"""
"""
import pylab as pl
import matplotlib.font_manager as fm


def set_font(font):
    pl.xlabel('String length', fontproperties=font)
    pl.tight_layout()
    for label in pl.axes().get_xticklabels():
        label.set_fontproperties(font)
    for label in pl.axes().get_yticklabels():
        label.set_fontproperties(font)


def save_me(name, font):
    set_font(font)
    pl.savefig('final_figs/' + name)
    pl.savefig('final_figs/' + name[:-4] + '.png')
    pl.axes().clear()


if __name__ == '__main__':

    font = fm.FontProperties(fname='/Users/alonger/HSE/cmunrm.ttf', size=20)

    with open('time.txt') as fd:
        lines = fd.read().strip().splitlines()
        super_naive = [(l.split()[1], float(l.split()[2]) * 100000) for l in lines if l.startswith('MAXBORDERLESS_SUPER_NAIVE') and int(l.split()[1]) < 101]
        border = [(l.split()[1], float(l.split()[2]) * 100000) for l in lines if l.startswith('MAXBORDERLESS_BORDER_FAST') and int(l.split()[1]) < 101]

    pl.plot(*zip(*border), color='k', dashes=[5, 3])
    pl.plot(*zip(*super_naive), color='k')

    pl.ylabel('Time, $10^{-5}$s', fontproperties=font)
    save_me('time.pdf', font)
