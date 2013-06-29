# -*- coding: utf-8 -*-

from __future__ import division
from math import pi, log

def r1haste(pa, l, d):
    return pa/(2*pi*l) * log(4*l/d)


if __name__ == '__main__':
    
    pa = input('resistividade(ohm*m): ')
    l = input('comprimento(m): ')
    d = input('diametro da haste(m): ')
    r = r1haste(pa, l, d)
    print 'resistencia: ', r
    
    saida = raw_input('ENTER] para sair')

