#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Circuitos com amplificador diferencial

from __future__ import division
import sys

modeloNPN = {
    'vbe' : 0.7,
    'bcc' : 100,
}

def conf1_resistoresBase(mNPN, VCC, VEE, RE, RC, RB):
    """Modelo simples de um amplificador diferencial
    Entrada:
        mNPN - modelo do transistor NPN
        VCC - tensão positiva da fonte simétrica [V]
        VEE - tensão negativa da fonte simétrica [V]
        RE - resistor de cauda [Ohm]
        RC - resistor do coletor [Ohm]
        RB - resistor da base [Ohm]
    Saída:
        It - corrente de cauda [A]
        Ie - corrente do emissor de cada transistor [A]
        Vout - tensão de saída, tensão coletor [V]
        Ib - corrente na base [A]
    """

    # corrente de cauda
    It = (VCC - mNPN['vbe'])/(RE+RB/(2*mNPN['bcc']))
    # corrente no emissor de cada transistor, identicos
    Ie = It/2
    # tensão no coletor do transistor Q2, lado direito
    Vout = VCC - Ie*RC
    # corrente na base
    Ib = Ie/mNPN['bcc']

    return [It, Ie, Vout, Ib]

def conf1Exemplo():
    transistor = modeloNPN
    transistor['vbe'] = 0.7
    transistor['bcc'] = 100
    vcc = 15
    vee = 15
    rc = 15e3
    rb = 33e3
    re = 15e3

    It, Ie, Vout, Ib = conf1_resistoresBase(transistor, vcc, vee, re, rc, rb)

    print 'It   [A]: ', It
    print 'Ie   [A]: ', Ie
    print 'Ib   [A]: ', Ib
    print 'Vout [V]: ', Vout

def modeloAC_ampDif(mNPN, VCC, VEE, RE, RC, RB):
    return -1

if __name__ == '__main__':
    print 'Amplificador diferencial'
    conf1Exemplo()

    sys.exit(0)

