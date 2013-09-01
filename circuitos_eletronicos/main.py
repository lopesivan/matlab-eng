#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from  __future__ import division
import sys
import amplificadorDiferencial


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


def entradaPar():
    try:
        vcc = float(raw_input('VCC [V]: '))
        vee = float(raw_input('VEE [V]: '))
        rc =  float(raw_input('RC  [R]: '))
        re =  float(raw_input('RE  [R]: '))
        rb =  float(raw_input('RB  [R]: '))
        bcc = float(raw_input('BCC    : '))
    except:
        print 'erro: entrada inválida'
        vcc = vee = rc = re = rb = bcc = -1

    return [vcc, vee, rc, re, rb, bcc]

def par():
    print 'Análise para o par diferencial'
    print 'opções:'
    print '1 - configuração básica, resistor na base'
    print '2 - analise ac. malvino, figura 17.11'

    tNPN = amplificadorDiferencial.modeloNPN

    entrada = input('>')

    if entrada == 1:
        vcc, vee, rc, re, rb, bcc = entradaPar()
        if bcc == -1:
            return -1
        tNPN['bcc'] = bcc
        it, ie, vout, ib = amplificadorDiferencial.conf1_resistoresBase(tNPN, vcc, vee, re, rc, rb)

        print 'Corrente de cauda                [A]: ', it
        print 'Corrente emissor cada transistor [A]: ', ie
        print 'Corrente na base                 [A]: ', ib
        print 'Tensão de saída                  [V]: ', vout

    elif entrada == 2:
        vcc, vee, rc, re, rb, bcc = entradaPar()
        if bcc == -1:
           return -1
        tNPN['bcc'] = bcc
        It, Ie, Ib, re, A, ie, zin, vout_dc, vout_ganho = amplificadorDiferencial.modeloAC_ampDif(tNPN, vcc, vee, re, rc, rb, 1e-3)

        print 'Corrente de cauda                [A]: ', It
        print 'Corrente emissor cada transistor [A]: ', Ie
        print 'Corrente na base                 [A]: ', Ib
        print 'Resistência dinâmica             [R]: ', re
        print 'Ganho                          [V/V]: ', A
        print 'Corrente AC no emissor           [A]: ', ie
        print 'Impedância de entrada            [R]: ', zin
        print 'Tensão de saída DC               [V]: ', vout_dc
        print 'Tensão de saóda DC com ganho     [V]: ', vout_ganho

    else:
        print 'erro: opção indisponivel'

def ao():
    return -1

def ajuda():
    print u'Comandos cadastrados'
    print u'a - ajuda'
    print u's - finaliza o programa'
    print u'par - análise para par diferencial'
    print u'ao  - análise para configurações básicas amplificador operacional'

def sair():
    print u'finalizando...'
    sys.exit(0)

dicionarioComandos = {
    'a' : ajuda,
    's' : sair,
    'par' : par,
    'ao' : ao,
}


def nada():
    print u'erro: comando não reconhecido'

def comandos(cmd):
    return dicionarioComandos.get(cmd, nada)()

if __name__ == '__main__':
    print u'Circuitos eletrônicos'

    while True:
        entrada = raw_input(':')
        if entrada == '':
            continue

        comandos(entrada.lower())

