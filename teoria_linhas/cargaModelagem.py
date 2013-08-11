#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
from math import tan, acos, sqrt, degrees
from cmath import phase

def potenciaConstante(potMVA, fpCarga, vNominalkV, vLinhakV, debug = False):
    potAtiva = potMVA*abs(fpCarga) # potência ativa da carga
    # potência reativa não modulada
    potReativa = potAtiva*tan(acos(fpCarga))

    # modelando a carga
    qmod = potReativa*(vLinhakV/vNominalkV)**2

    # potência complexa
    smod = potAtiva+qmod*1j

    if debug:
        print u'Potência ativa[MW]       : ', potAtiva
        print u'Potência reativa[MVAr]   : ', potReativa
        print u'Potência reativa modelada: ', qmod
        print u'Potência complexa[MVA]   : ', smod

    return smod

def impedanciaConstante(potMVA, fpCarga, vNominalkV, vLinhakV, debug = False):
    potAtiva = potMVA*abs(fpCarga) # potência ativa da carga
    # potência reativa não modulada
    potReativa = potAtiva*tan(acos(fpCarga))

    # modelando a carga
    qmod = potReativa*(vLinhakV/vNominalkV)**2
    pmod = potAtiva*(vLinhakV/vNominalkV)**2

    smod = pmod + qmod*1j

    if debug:
        print u'Potência ativa[MW]       : ', potAtiva
        print u'Potência reativa[MVAr]   : ', potReativa
        print u'Potência reativa modelada: ', qmod
        print u'Potência ativa modelada  : ', pmod
        print u'Potência complexa[MVA]   : ', smod

    return smod

def cargaMista(potMVA, fpCarga, vNominalkV, vLinhakV, PCTE, ZCTE, debug = False):
    potAtiva = potMVA*abs(fpCarga) # potência ativa da carga
    # potência reativa não modulada
    potReativa = potAtiva*tan(acos(fpCarga))

    # modelando a carga
    qmod = potReativa*(vLinhakV/vNominalkV)**2
    pmod = PCTE*potAtiva + ZCTE*potAtiva*(vLinhakV/vNominalkV)**2

    smod = pmod + qmod*1j

    if debug:
        print u'Potência ativa[MW]       : ', potAtiva
        print u'Potência reativa[MVAr]   : ', potReativa
        print u'Potência reativa modelada: ', qmod
        print u'Potência ativa modelada  : ', pmod
        print u'Potência complexa[MVA]   : ', smod

    return smod

def correnteCarga(smod, vLinhakV, debug = 0):
    i = (smod*1000)/(sqrt(3)*vLinhakV)
    i = i.conjugate()

    if debug:
        print 'Corrente[A]: ', i
        print 'modulo     : ', abs(i)
        print 'fase[graus]: ', degrees(phase(i))

    return i

def teste(debug):
    # 1- potência ativa constante (Pcte)
    # 2- impedância constante (Zcte)
    # 3- Mista % Pcte e % Zcte

    if debug:
        print '################################'
        print '# CASO 1, Potência constante   #'
        print '################################'

    # Carga
    potMVA = 150
    fpCarga = -.95      # fator de potência capacitivo
    vNominalkV = 138    # tensão nominal da carga
    # Tensão no barramento
    vLinhakV = 130

    smod = potenciaConstante(potMVA, fpCarga, vNominalkV, vLinhakV, debug)
    correnteCarga(smod, vLinhakV, debug)

    if debug:
        print '################################'
        print '# CASO 2, Impedância constante #'
        print '################################'

    smod = impedanciaConstante(potMVA, fpCarga, vNominalkV, vLinhakV, debug)
    correnteCarga(smod, vLinhakV, debug)

    if debug:
        print '################################'
        print '# CASO 3, Carga Mista          #'
        print '################################'
    PCTE = .4
    ZCTE = .6
    smod = cargaMista(potMVA, fpCarga, vNominalkV, vLinhakV, PCTE, ZCTE, debug)
    correnteCarga(smod, vLinhakV, debug)

if __name__ == '__main__':
    print u'Modelagem de carga trifásica'
    teste(True)

