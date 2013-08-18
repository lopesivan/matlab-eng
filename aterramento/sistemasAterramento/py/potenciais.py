#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
from math import sqrt

def iChoqueDaziel(t):
    """
    Entrada:
    t = tempo de duração do choque de 0.03 a 3 segundos
    Saída:
    Corrente de choque suportada, para não causar fibrilação
    """
    return 0.116/sqrt(t)

def fatorCorrecaoBrita(hs, pa, ps):
    """
    Entrada:
    hs = profundidade da brita [m]
    pa = resistividade aparente da malha [ohm*m]
    ps = resistividade da camada de brita [ohm*m]
    Saída:
    CS
    """
    infinito = 100

    k = (pa-ps)/(pa+ps)

    # prepara o somatório
    s = 0
    for n in range(1, infinito+1):
        s+=(k**n)/sqrt(1+(2*n*(hs/0.08))**2)
    cs = (2*s+1)*(1/0.96)

    return cs

def potencialToque(rch, rc, iChoque):
    """
    Entrada:
    rch = resistência do corpo humano
    rc = resistência de contato entre as partes metálicas
    Saída:
    potencial
    """
    vtoque = (rch + rc/2)*iChoque
    return vtoque

def potencialMaximoToque(ps, t):
    """
    Entrada:
    ps = resistência de contato em [ps] IEEE-80
    t = tempo de exposição ao choque
    Saída:
    potencial
    """
    vtoqueMaximo = (116+0.174*ps)/sqrt(t)
    return vtoqueMaximo

def potencialMaximoToqueCS(ps, t, cs = 1):
    """
    Entrada:
    ps = resistência de contato em [ps] IEEE-80
    cs = fator de correção para uma camada de brita
    t = tempo de exposição ao choque
    Saída:
    potencial
    """
    vtoqueMaximo = (1000 + 1.5*cs*ps)*(0.116/sqrt(t))
    return vtoqueMaximo

def potencialMaximoPasso(ps, t):
    """
    Entrada:
    ps = resistência de contato em [ps] IEEE-80
    t = tempo de exposição ao choque
    Saída:
    potencial
    """
    vpassoMaximo = (116 + 0.696*ps)/sqrt(t)
    return vpassoMaximo

def potencialMaximoPassoCS(ps, t, cs = 1):
    """
    Entrada:
    ps = resistência de contato em [ps] IEEE-80
    cs = fator de correção para uma camada de brita
    t = tempo de exposição ao choque
    Saída:
    potencial
    """
    vpassoMaximo = (1000 + 6*cs*ps)*(0.116/sqrt(t))
    return vpassoMaximo

if __name__ == '__main__':
    print 'Calculos dos potencias de risco para um ser humano'
    print 'fator de correcao da brita, ', fatorCorrecaoBrita(2, 1000, 1000)
