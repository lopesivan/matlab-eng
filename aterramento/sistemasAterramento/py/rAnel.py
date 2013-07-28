# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica
#
#-------------------------------------------------------------------------------
# Cáculos para condutores enrolados formando um anel
#-------------------------------------------------------------------------------
#
from __future__ import division
import r1haste
from math import pi, log

def ranel(pa, p, r, d):
    """
    pa = resistividade do solo
    p = profundida que está enterrado o anel[m]
    r = raio do anel[m]
    d = diâmetro do circulo equivalente à soma de seção transversal dos 
    condutores que formam o anel [m]
    """
    return (pa/((pi**2) * r))*log((4*(r**2))/(d*p))

if __name__ == "__main__":
    print 'Resistência de aterramento em anel'

    r = 0.5
    d = 0.01
    p = .6
    pa = 1e3

    print 'raio do anel, ', r
    print 'diâmentro do condutor, ', d
    print 'profundida, ', p
    print 'resistividade do solo', pa
    print 'resistencia do aterramento, ', ranel(pa, p, r, d)
