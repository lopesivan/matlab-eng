#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Teoria geral dos quadripolos
class ct:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def linha_curta(Z):
    if type(Z) is not complex:
        print 'erro: impedância não é um número complexo'
        return -1

    A = 1
    B = Z
    C = 0
    D = 1

    return [A, B, C, D]

def linha_media_pi(Z, Y):
    if type(Z) is not complex or type(Y) is not complex:
        print 'erro: impedância ou susceptância não é um número complexo'
        return -1

    A = 1 + (Z*Y)/2
    B = Z
    C = Y*(1 + (Z*Y)/4)
    D = A

    return [A, B, C, D]

def linha_media_T(Z, Y):

    if type(Z) is not complex or type(Y) is not complex:
        print 'erro: impedância ou susceptância não é um número complexo'
        return -1

    A = 1 + (Z*Y)/2
    B = Z*(1 + (Z*Y)/4)
    C = Y
    D = A

    return [A, B, C, D]


def zona_teste():
    print '-'*10
    print ct.BOLD+'Parâmetros do quadripolo'+ct.END

    print ct.BLUE+'LINHA CURTA'+ct.END
    Z = 1+2j
    A, B, C, D = linha_curta(Z)

    print 'Entrada,'
    print ' z [ohm]: ', Z
    print 'Saída,'
    print ' A :', A
    print ' B :', B
    print ' C :', C
    print ' D :', D

    print
    print ct.BLUE+'LINHA MÉDIA PI'+ct.END
    Y = 2+3j

    A, B, C, D = linha_media_pi(Z, Y)

    print 'Entrada,'
    print ' z [ohm]: ', Z
    print 'Saída,'
    print ' A :', A
    print ' B :', B
    print ' C :', C
    print ' D :', D

    print
    print ct.BLUE+'LINHA MÉDIA T'+ct.END
    Y = 2+3j

    A, B, C, D = linha_media_T(Z, Y)

    print 'Entrada,'
    print ' z [ohm]: ', Z
    print 'Saída,'
    print ' A :', A
    print ' B :', B
    print ' C :', C
    print ' D :', D


if __name__ == '__main__':
    print 'Teoria dos quadripolos'
    zona_teste()

