# -*- coding: utf-8 -*-
from __future__ import division
from math import cos, sin, sqrt, exp, asin, pi
import matplotlib.pyplot as plt
from numpy import arange

def f1(w, y, v, l, t):
    """ Função da corrente
    """
    return (v/(w*l))*exp(-y*t)*sin(w*t)

def cAlfa(r, l):
    """ frequencia de amortecimento
    """
    return r/(2*l)

def cOmega(r, l, c):
    return sqrt((1/(l*c))-(r**2)/(4*l**2))

def cOmegaNatural(L, C):
    return 1/sqrt(L*C)

def subamotercido(alfa, omegaNatural):
    if alfa <  omegaNatural:
        return 1
    else:
        return 0

def tf(w, l, c):
    """ Front time
    """
    return (1/w)*asin((w/sqrt(l*c))%1)

def t1(r, l, c):
    """ Time to Half
    """
    return pi/sqrt(1/(l*c) - (r**2)/(4*l**2))

def ondaCorrente(L, C, R, alfa, omega, tFinal, p):
    t = arange(0, tFinal, p)
    I = []
    for i in t:
        I.append(f1(omega, cAlfa(R, L), V, L, i))
    return [t, I]

def plotOnda(x, y):
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print 'Artigo:'
    print 'Development of a Small Scale Standard Lightning Impulse Current Generator'

    V = 30e3
    L = 108e-6
    R = 11.56
    C = 0.6e-6

    alfa = cAlfa(R, L)
    if not subamotercido(alfa, cOmegaNatural(L, C)):
        print 'erro: esse circuito não é subamortecido'
        exit(-1)
    omega = cOmega(R, L, C)

    print 'alfa : ', alfa
    print 'omega: ', omega

    print 'Time to half (s): ', tf(omega, L, C)
    print 'Front time   (s): ', t1(R, L, C)
    [t, I] = ondaCorrente(L, C, R, alfa, omega, 100e-6, 1e-7)
    plotOnda(t, I)


    print 'Corrente de pico (A): ', max(I)



