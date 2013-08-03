# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 03/08/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
from math import cos, sin, sqrt, exp, asin, pi, log
import matplotlib.pyplot as plt
from numpy import arange
from scipy.optimize import fmin_slsqp
import sys

limitesRL = ((1, 10), (1e-6, 200e-6))

def f1(w, y, v, l, t):
    """ Função da corrente
    Entrada:
        w - frequencia de amortecimento
        y - alfa
        v - tensão inicial do capacitor
        l - indutancao
        t - instante t em segundos

    Saída:
        corrente no instante t
    """
    return (v/(w*l))*exp(-y*t)*sin(w*t)

def cAlfa(r, l):
    """ frequencia de amortecimento
    Entrada:
        r - resistência em ohms
        l - indutância em henry
    Saída:
        frequencia de amortecimento
    """
    return r/(2*l)

def cOmega(r, l, c):
    """
    Entrada:
        r - resistência
        l - indutância
        c - capacitância
    Saída:
        Omega
    """
    return sqrt((1/(l*c))-(r**2)/(4*l**2))

def cOmegaNatural(L, C):
    """
    Entrada:
        L - indutância
        C - capacitância
    Saída
        Frequencia natural do circuito
    """
    return 1/sqrt(L*C)

def subamotercido(alfa, omegaNatural):
    """ Verifica se o circuito RLC série é caracterizado como sendo subamortecido
    Entrada:
    Saída:
    """
    if alfa <  omegaNatural:
        return 1
    else:
        return 0

def tf(w, l, c):
    """ Tempo que a onda atingi o seu primeiro pico de corrente
    Entrada:
        w - omega
        l - indutância em henry
        c - capacitância em faradays
    Saída:
        tempo em segundos
    """
    return (1/w)*asin((w/sqrt(l*c))%1)

def t1(r, l, c):
    """ Tempo que a onda demora para atingir metade do máximo
    Entrada:
        r - resistência em ohm
        l - indutância em henry
        c - capacitância em faradays
    Saída
        tempo em segundos
    """
    return pi/sqrt(1/(l*c) - (r**2)/(4*l**2))

def ondaCorrente(V, L, C, R, alfa, omega, tFinal, p):
    """ Constroe a onda da corrente
    Entrada:
        L - indutância em Henry
        C - capacitância em Faradays
        R - resistência em Ohm
        alfa
        omega
        tFinal - tempo final para a construção
        p - passo para a construção
    Saída:
        t - comprimento total da onda
        I - vetor com os pontos da corrente em Amperes
    """
    t = arange(0, tFinal, p)
    I = []
    for i in t:
        I.append(f1(omega, cAlfa(R, L), V, L, i))
    return [t, I]

def plotOnda(x, y):
    """ Plota um vetor x e y
    """
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

def buscaTf(I):
    return I.index(max(I))

def buscaTh(I):
    # tempo t0.5 padrão IEC, considerado a cauda da onda
    t05 = max(I)*.5
    t = range(len(I))
    posMaximo = buscaTf(I)
    for i in t[posMaximo:]:
        if I[i] < t05:
            pos05 = i
            break

    return pos05

#--------------------------------------------------------------------------
# ONDA TEORICA
#--------------------------------------------------------------------------

def ondaTeoricaCorrente(alfa, omega, V, L, t):
    return (V/(omega*L))*exp(-alfa*t)*sin(omega*t)

def ondaTeoricaCorrenteOtimizacao(x):
    pass


def testaOndaTeorica():
    global tempoBaseOndaTeorica, tensaoBaseOndaTeorica

    omega = .113e6
    alfa = .0535e6
    L = 108e-6
    V = 30e3

    t = arange(0, 100e-6, .1e-6)
    I = []
    for i in t:
        I.append(ondaTeoricaCorrente(alfa, omega, V, L, i))

    plotOnda(t, I)

    tempoBaseOndaTeorica = t
    tensaoBaseOndaTeorica = V

    ondaTeoricaCorrenteOtimizacao(1)
#--------------------------------------------------------------------------
# CASO 1
# Artigo: Development of a Small Scale Standard Lightning Impulse Current
#--------------------------------------------------------------------------

def testaCaso1():
    #print 'Artigo:'
    #print 'Development of a Small Scale Standard Lightning Impulse Current Generator'

    V = 30e3    # tensão inicial do capacitor
    L = 108e-6  # indutância
    R = 11.56   # resitência
    C = 0.6e-6  # capacitância

    alfa = cAlfa(R, L)
    # verifica se o circuito é caracterizado como sendo subamortecido
    if not subamotercido(alfa, cOmegaNatural(L, C)):
        print 'erro: esse circuito não é subamortecido'
        # refaça os cálculos
        return -1
    omega = cOmega(R, L, C)

    print 'alfa : ', alfa
    print 'omega: ', omega

    print 'Time to half (s): ', tf(omega, L, C)
    print 'Front time   (s): ', t1(R, L, C)
    [t, I] = ondaCorrente(V, L, C, R, alfa, omega, 100e-6, 1e-7)
    #plotOnda(t, I)

    print 'Corrente de pico (A): ', max(I)

    # busca os valores tf e th
    print 'posição tf : ', buscaTf(I)
    print 'valor tf   : ', I[buscaTf(I)]
    print 'tempo tf(s): ', t[buscaTf(I)]

    print 'posicao th : ', buscaTh(I)
    print 'valor th   : ', I[buscaTh(I)]
    print 'tempo th(s): ', t[buscaTh(I)]

    return 0

if __name__ == '__main__':
    testaCaso1()
    #testaOndaTeorica()

    sys.exit(0)

