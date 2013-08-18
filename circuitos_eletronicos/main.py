#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from  __future__ import division
import sys
import amplificadorDiferencial

def ajuda():
    print 'Comandos cadastrados'
    print u's - finaliza o programa'

def sair():
    print u'finalizando...'
    sys.exit(0)

dicionarioComandos = {
    'a' : ajuda,
    's' : sair,
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

