#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Modelos de linha de transmissão
import quadripolos

class curta:
    """
    R - resistência [ohm/m]
    XL - reatância indutiva [ohm/m]
    c - comprimento [m]
    """
    def __init__(self, R, XL, c):
        self.tipo = 'curta'
        self.Z = c*(R + XL*1j)
        self.comprimento = c
        self.R = self.Z.real
        self.XL = self.Z.imag

        self.A, self.B, self.C, self.D  = quadripolos.linha_curta(self.Z)

class media_pi:
    """
    R - resistência [ohm/m]
    XL - reatância indutiva [ohm/m]
    XC - reatância capacitiva [ohm/m]
    c - comprimento [m]
    """
    def __init__(self, R, XL, XC, c):
        self.tipo = 'pi'
        self.Z = c*(R + XL*1j)

        # susceptância capacitiva
        self.B = (c*XC)/2
        # admitância
        self.Y = self.B * 1j

        self.comprimento = c
        self.R = self.Z.real
        self.XL = self.Z.imag

        self.A, self.B, self.C, self.D  = quadripolos.linha_media_pi(self.Z, self.Y)

class media_t:
    """
    R - resistência [ohm/m]
    XL - reatância indutiva [ohm/m]
    XC - reatância capacitiva [ohm/m]
    c - comprimento [m]
    """
    def __init__(self, R, XL, XC, c):
        self.tipo = 'pi'
        self.Z = (c*(R + XL*1j))/2

        # susceptância capacitiva
        self.B = (c*XC)/2
        # admitância
        self.Y = self.B * 1j

        self.comprimento = c
        self.R = self.Z.real
        self.XL = self.Z.imag

        self.A, self.B, self.C, self.D  = quadripolos.linha_media_pi(self.Z, self.Y)

def zona_teste():
    print 'Entrando na zona de teste'


    print '--Teste para o objeto, linha curta'
    linha_AB = curta(1.1, 1.2, 10)
    print 'Tipo         :', linha_AB.tipo
    print 'Impedância   :', linha_AB.Z
    print ' Resistência :', linha_AB.R
    print ' Reatância   :', linha_AB.XL
    print 'Comprimento  :', linha_AB.comprimento

    print '--Teste para o objeto, linha media pi'
    linha_AB = media_pi(1.1, 1.2, 1, 10)
    print 'Tipo            :', linha_AB.tipo
    print 'Impedância(Z)   :', linha_AB.Z
    print ' Resistência    :', linha_AB.R
    print ' Reatância      :', linha_AB.XL
    print 'Susceptância(C) :', linha_AB.Y
    print 'Comprimento     :', linha_AB.comprimento

    print '--Teste para o objeto, linha media T'
    linha_AB = media_t(1.1, 1.2, 1, 10)
    print 'Tipo            :', linha_AB.tipo
    print 'Impedância      :', linha_AB.Z
    print ' Resistência    :', linha_AB.R
    print ' Reatância      :', linha_AB.XL
    print 'Susceptância(C) :', linha_AB.Y
    print 'Comprimento     :', linha_AB.comprimento


if __name__ == '__main__':
    print 'Modelagem de linhas de transmissão'
    print 'Modelos disponíveis'
    print '-Curta'
    print '-Média pi'
    print '-Média T'

    zona_teste()

