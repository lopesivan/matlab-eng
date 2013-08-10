# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from  __future__ import division
import cargaModelagem
import sys
import bifilar

dadosEntBifilar = {
    'tensao' : 0,
    'impedancia' : 0,
    'capacitancia' : 0,
    'comprimento' : 0,
    'Z2a' : 0,
    'Z2b' : 0,
    'Z2c' : 0,
    'flag' : 0,
}

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

def entradaBifilar():
    if dadosEntBifilar['flag'] == 1:
        print u'Usar valores antigos[S/n]?',
        if raw_input() != 'n':
            z2 = []
            z2.append(dadosEntBifilar['Z2a'])
            z2.append(dadosEntBifilar['Z2a'])
            z2.append(dadosEntBifilar['Z2a'])
            return [dadosEntBifilar['tensao'], dadosEntBifilar['indutancia'], dadosEntBifilar['capacitancia'], dadosEntBifilar['comprimento'], z2]
    try:
        print u'Tensão constante [V]               :',
        tensao = float(raw_input())
        print u'Indutância dos contudores [H/km]   :',
        ind = float(raw_input())

        print u'Capacitância dos contudores [F/km] :',
        cap = float(raw_input())
        print u'Comprimento da linha [km]          :',
        comp = float(raw_input())

        z2 = []
        print u'Z2-1 [ohm]                         :',
        z2.append(float(raw_input()))
        print u'Z2-2 [ohm]                         :',
        z2.append(float(raw_input()))
        print u'Z2-3 [ohm]                         :',
        z2.append(float(raw_input()))

    except:
        print u'erro: inesperado'
        return [-1, -1, -1, -1, [-1, -1, -1]]

    dadosEntBifilar['tensao'] = tensao
    dadosEntBifilar['indutancia'] = ind
    dadosEntBifilar['capacitancia'] = cap
    dadosEntBifilar['comprimento'] = comp
    dadosEntBifilar['Z2a'] = z2[0]
    dadosEntBifilar['Z2a'] = z2[1]
    dadosEntBifilar['Z2a'] = z2[2]

    dadosEntBifilar['flag'] = 1

    return [tensao, ind, cap, comp, z2]

def sistemaBifilar():
    print u'1 - exemplo 1'
    print u'2 - problema 1, uma linha de transmissão bifilar aérea...'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuario'
        return -2

    if a == 1:
        bifilar.exemplo1()
    if a == 2:
        print  """Uma linha de transmissão bifilar aérea é suprida por
uma fonte de tensão constante e igual a x[volt].
A indutância dos condutores é de -[henry/m](fluxo interno considerado)
sua capacitância é igual a x[farad/km].
Tratando-se de uma linha sem perdas, deseja-se saber, sendo seu
comprimento igual a x[km].
a - sua impedância natural
b - energia armazenada por quilômetro de linha nos campos
elétricos e magnéticos
c - velocidade de propagação
d - qual o valor da tensão no recpetor no decorrido tempo
t=(3l)/v do instante em que a linha foi energizada, para as
seguintes condições:
a - z2 = x [ohm]
b - z2 = x [ohm]
c - z2 = x [ohm]
"""

        tensao, L, C,  l, Zs = entradaBifilar()
        Z0, I0, Em, Ee, Et, v, U22, U21= bifilar.problema1(tensao, C, L, l, Zs)

        print u'Impedância natural [ohm]:', Z0
        print u'Corrente I0[A]          :', I0
        print u'Energia magnética [Ws]  :', Em
        print u'Energia elétrica [Ws]   :', Ee
        print u'Energia total [Ws]      :', Et
        print u'Velocidade prop. [km/s] :', v
        print u'Valores de tensão:'
        print u'Z1 | Z2 | Z3'
        print U22
        print U21

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

