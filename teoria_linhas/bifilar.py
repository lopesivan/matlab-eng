# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Transmissão Bifilar, aérea

from __future__ import division
import sys
from math import sqrt

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

    print u'Impedância natural [ohm]:', Z0
    print u'Corrente I0[A]          :', I0
    print u'Energia magnética [Ws]  :', Em
    print u'Energia elétrica [Ws]   :', Ee
    print u'Energia total [Ws]      :', Et
    print u'Velocidade prop. [km/s] :', v
if __name__ == '__main__':
    print u'Transmissão bifilar'
    exemplo1()

