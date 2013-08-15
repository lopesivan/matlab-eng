#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Transmissão Bifilar, aérea

from __future__ import division
import sys
from math import sqrt, exp, log, pi

def impedanciaNatural(L, C):
    return sqrt(L/C)

def energiaCampoMagnetico(I0, L):
    return ((I0**2)*L)/2

def correnteI0(U, Z0):
    return U/Z0

def energiaCampoEletrico(U, C):
    return ((U**2)*C)/2

def velocidadePropagacao(L, C):
    return 1/sqrt(L*C)

def Ur(Z2, Z0, Ud):
    return kr(Z2, Z0)*Ud

def Ir(Z2, Z0, Id):
    return kr(Z2, Z0)*Id

def kr(Z2, Z0):
    """ Coeficiente de reflexão """
    if (Z2+Z0)==0 or (Z2-Z0)== 0:
        print u'aviso: divisão por zero no coeficiente de reflexão'
        return 0
    return (Z2-Z0)/(Z2+Z0)

def tempoPropagacao(l, v):
    return l/v

def ondasViajantes(R2, Z0):
    print
    print u'Informações relevantes:'
    print

    if R2>Z0:
        print "R2 > Z0"
        print u"""-a onda de tensão refletida possui o mesmo sinal
que a onda de tensão incidente. A tensão resultante será, então,
maior do que a da onda incidente.
- a onda da corrente refletida possui sinal contrário do da onda
incidente, resultanto em corrente menor do que a incidente.
"""
    elif R2==Z0:
        print "R2 igual Z0"
        print u"""- tanto a onda refletida da tensão como a da corrente
são nulas, não havendo, portanto, alterações em seus valores.
"""
    elif R2<Z0:
        print "R2 < Z0"
        print u"""- a onda da tensão se reflete com sinal oposto ao da
incidente, resultando em diminuição da tensão.
- a onda da corrente se reflete com o mesmo sinal, o que leva ao seu
aumento.
"""

def exemplo1():
    """Uma linha de transmissão bifilar aérea é suprida por
    uma fonte de tensão constante e igual a 800[volt]. A indutância
    dos condutores é de 0.001358[henry/m](fluxo interno considerado)
    sua capacitância é igual a 0.008488e-6 [farad/km]
    Tratando-se de uma linha sem perdas, deseja-se saber, sendo
    seu comprimento igual a 100[km]
    a - sua impedância natural
    b - energia armazenada por quilômetro de linha nos campos
    elétricos e magnéticos
    c - velocidade de propagação
    d - qual o valor da tensão no recpetor no decorrido tempo
    t=(3l)/v do instante em que a linha foi energizada, para as
    seguintes condições:
        a - z2 = 100 [ohm]
        b - z2 = 400 [ohm]
        c - z2 = 1600 [ohm]
    """

    tensao = 800
    induCondutor = 0.001358
    capaCondutor = 0.008488e-6
    cLinhakm = 100

    Z0 = impedanciaNatural(induCondutor, capaCondutor)
    I0 = correnteI0(tensao, Z0)
    Em = energiaCampoMagnetico(I0, induCondutor)
    Ee = energiaCampoEletrico(tensao, capaCondutor)
    Et = Em+Ee  # energia total armazenada
    v = velocidadePropagacao(induCondutor, capaCondutor)

    Z2a = 100
    Z2b = 400
    Z2c = 1600

    #ondasViajantes(Z2a, Z0)
    #ondasViajantes(Z2b, Z0)
    #ondasViajantes(Z2c, Z0)

    # para Z2a
    kru2_Z2a = kr(Z2a, Z0)
    U2a_2 = tensao*(1-kru2_Z2a**2)
    U2a_1 = tensao*(1+kru2_Z2a)
    # para Z2b
    kru2_Z2b = kr(Z2b, Z0)
    U2b_2 = tensao*(1-kru2_Z2b**2)
    U2b_1 = tensao*(1+kru2_Z2b)
    # para Z2c
    kru2_Z2c = kr(Z2c, Z0)
    U2c_2 = tensao*(1-kru2_Z2c**2)
    U2c_1 = tensao*(1+kru2_Z2c)

    print u'Impedância natural [ohm]:', Z0
    print u'Corrente I0[A]          :', I0
    print u'Energia magnética [Ws]  :', Em
    print u'Energia elétrica [Ws]   :', Ee
    print u'Energia total [Ws]      :', Et
    print u'Velocidade prop. [km/s] :', v

    print u'coeficientes de reflexão:'
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2a, kru2_Z2a, U2a_2, U2a_1)
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2b, kru2_Z2b, U2b_2, U2b_1)
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2c, kru2_Z2c, U2c_2, U2c_1)

def problema1(tensao, capaCondutor, induCondutor, comprimento, Zs, debug = False):

    Z0 = impedanciaNatural(induCondutor, capaCondutor)
    I0 = correnteI0(tensao, Z0)
    Em = energiaCampoMagnetico(I0, induCondutor)
    Ee = energiaCampoEletrico(tensao, capaCondutor)
    Et = Em+Ee  # energia total armazenada
    v = velocidadePropagacao(induCondutor, capaCondutor)

    Z2a, Z2b, Z2c = Zs
    # para Z2a
    kru2_Z2a = kr(Z2a, Z0)
    U2a_2 = tensao*(1-kru2_Z2a**2)
    U2a_1 = tensao*(1+kru2_Z2a)
    # para Z2b
    kru2_Z2b = kr(Z2b, Z0)
    U2b_2 = tensao*(1-kru2_Z2b**2)
    U2b_1 = tensao*(1+kru2_Z2b)
    # para Z2c
    kru2_Z2c = kr(Z2c, Z0)
    U2c_2 = tensao*(1-kru2_Z2c**2)
    U2c_1 = tensao*(1+kru2_Z2c)

    U22 = [U2a_2, U2b_2, U2c_2]
    U21 = [U2a_1, U2b_1, U2c_1]

    return [Z0, I0, Em, Ee, Et, v, U22, U21]

def problema9(resistencia, reatanciaIndutiva, condutibilidade, susceptancia, freq):
    return -1

def exemplo2():
    Lkm, L, Xl, Zl = linhaTrifasicaIndutancia(2.5, 25/2, 60)

    print u'Indutância de uma linha trifásica com espaçamento equilaterais:'
    print '[H/km] :', Lkm
    print '[H]    :', L
    print 'Reatância:'
    print 'Ohm    :', Xl
    print 'Impedância:'
    print 'Ohm    :', Zl

def linhaTrifasicaIndutancia(espEqui, raio, comprimento, freq = 60):
    """Indutância de uma linha de transmissão trifásica com
    espaçamento equilateral.
    Entrada:
        espEqui - espaçamento equilateral entre os condutores [m]
        raio - raio do condutor [mm]
        comprimento - comprimento total da linha [km]
        freq = frequência da linha [Hz]
    Saída:
        IndutânciaKm [H/km]
        Indutância [H]
        Modulo da reatância indutiva [OHM]
        Impedância [OHM]
    """
    c1 = 2e-7
    e4 = exp(-1/4)
    re = e4*raio    # raio efetivo do condutor
    Lkm = c1*log(espEqui*1e3/re)*1e3
    L = comprimento*Lkm

    Xl = 2*pi*freq*L
    Zl = Xl*1j

    return [Lkm, L, Xl, Zl]

if __name__ == '__main__':
    print u'Transmissão bifilar'
    exemplo1()
    exemplo2()
