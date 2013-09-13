#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Diversos problema comuns encontrados na cadeira de linhas
# e transmissão do professor Garrido.

def p1():
    print """
No sistema de potência abaixo, a referência de tensão para efeito
de modelagem das cargas é V1 [kV]. Considere o modelo de LT curta
para os trechos "A-B" e "B-C"

           |--d1--|--d2--|

           A      B      C
  ---------|------|------|
  |        |      |-|    |-|
  |                 |      |
  |                 |      |
Fonte             carga2 carga1
  |                 |      |
  |                 |      |
terra             terra  terra

Sabendo que a tensão entre fases na subestação "C" é de 225 [kV]
Determine:
a - As tensões entre fases nas subestações "A" e "B"
b - A perda ativa em [kW] no trecho "A-B"
c - O reativo consumido pela LT em [kVar] no trecho "B-C"
    """



    if continuar():
        return -1

    return 0

def continuar():
    if raw_input('continuar[S/n]?') == 'n':
        return -1
    else:
        return 0

def msg_curtas():
    print '1 - ... no sistema de potência... duas linhas curtas'
    print '2 - ... linha curta e media pi, banco de capacitores'
    return 0

def problemas():
    print 'Problemas cadastrados:'

    msg_curtas()

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2


    if a == 1:
        p1()
    else:
        print 'erro: opção não cadastrada'
        return -1

    return 0

