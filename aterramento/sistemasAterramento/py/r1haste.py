# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

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

