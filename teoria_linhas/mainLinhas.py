# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from  __future__ import division
import cargaModelagem
import sys
import bifilar

def dadosCargaMod():
    try:
        print u'potência aparente [MVA]           :',
        potMVA = float(raw_input())
        print u'fator de potência                 :',
        fp = float(raw_input())

        if abs(fp) > 1:
            raise Exception()

        print u'tensão nominal da carga [kV]      :',
        vn = float(raw_input())
        print u'tensão de linha no barramento [kV]:',
        vl = float(raw_input())
    except:
        print u'erro: inesperado'
        return [-1, -1, -1, -1]

    return [potMVA, fp, vn, vl]

def entradaCargaMod():
    print u'1- potência constante'
    print u'2- impedância constante'
    print u'3- carga mista'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuario'
        return -2

    if a == 1:
        dados = dadosCargaMod()

        if dados[0] == -1:
            print u'erro: entrada inválida'
            return -1

        smod = cargaModelagem.potenciaConstante(dados[0], dados[1], dados[2], dados[3], debug = True)
        corrente = cargaModelagem.correnteCarga(smod, dados[3], debug = True)
        return 0

    elif a == 2:
        dados = dadosCargaMod()

        if dados[0] == -1:
            print u'erro: entrada inválida'
            return -1

        smod = cargaModelagem.impedanciaConstante(dados[0], dados[1], dados[2], dados[3], debug = True)
        corrente = cargaModelagem.correnteCarga(smod, dados[3], debug = True)

        return 0
    elif a == 3:
        dados = dadosCargaMod()

        if dados[0] == -1:
            print u'erro: entrada inválida'
            return -1

        try:
            print u'PCTE %:',
            pcte = float(raw_input())
            print u'ZCTE %:',
            zcte = float(raw_input())
        except:
            print u'erro: entrada inválida'
            return -1

        smod = cargaModelagem.cargaMista(dados[0], dados[1], dados[2], dados[3], pcte, zcte, debug = True)
        corrente = cargaModelagem.correnteCarga(smod, dados[3], debug = True)

        return 0
    else:
        print u'erro: opção não reconhecida'
        return -1

def sistemaBifilar():
    print u'1 - exemplo 1'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuario'
        return -2

    if a == 1:
        bifilar.exemplo1()
    else:
        print u'erro: opção não reconhecida'
        return -1

    return 0

def ajuda():
    print 'Comandos cadastrados'
    print u's - finaliza o programa'
    print u'm - modelagem de uma carga'
    print u'b - sistema bifilar'

def sair():
    print u'finalizando...'
    sys.exit(0)

dicionarioComandos = {
    'a' : ajuda,
    's' : sair,
    'm' : entradaCargaMod,
    'b' : sistemaBifilar,
}

def nada():
    print u'erro: comando não reconhecido'

def comandos(cmd):
    return dicionarioComandos.get(cmd, nada)()

if __name__ == '__main__':
    print u'Transmissão de energia elétrica, linhas aéreas'

    while True:
        entrada = raw_input(':')
        if entrada == '':
            continue

        comandos(entrada.lower())

