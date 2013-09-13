#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Núcleo do programa de linha e transmissão

from  __future__ import division
import cargaModelagem
import sys
import bifilar
import formatacao
import quadripolos
import linhas
import problemas

# frequência base para qualquer cálculo que leve frequência
# No Brasil temos a maior parte 60Hz
freqREDE = 60

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


# Cores no terminal, muito massa
# http://stackoverflow.com/questions/8924173/python-print-bold-text
# mais informações interessantes
# http://ascii-table.com/ansi-escape-sequences.php
class colortext:
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

def impedanciaIndutiva(L, f):
    return L*f*1j

def impedanciaCapacitiva(C, f):
    return 1/(C*f*1j)

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
    """Modelagem de carga trifásica equilibrada
    """

    print u'1- potência constante'
    print u'2- impedância constante'
    print u'3- carga mista'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
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
        print u'Indutância dos condutores [H/km]   :',
        ind = float(raw_input())

        print u'Capacitância dos condutores [F/km] :',
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
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        bifilar.exemplo1()
    elif a == 2:
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
d - qual o valor da tensão no receptor no decorrido tempo
t=(3l)/v do instante em que a linha foi energizada, para as
seguintes condições:
a - z2 = x [ohm]
b - z2 = x [ohm]
c - z2 = x [ohm]
"""

        tensao, L, C,  l, Zs = entradaBifilar()
        if tensao == -1:
            print 'erro: entrada inválida'
            return -1

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

def entradaIndCap(nCondutores=3, mono = 0):
    """Processamento da entrada do usuário para os cálculos
    dos parâmetros indutivos e capacitivos de uma linha de transmissão
    Entrada:
        nCondutores - número de condutores
        mono - 0 = linha trifásica
               1 = linha monofásica
    """

    try:
        print u'Espaçamento entre as fases       [m]:',
        espFases = float(raw_input())
        if nCondutores > 1:
            print u'Espaçamento entre os condutores [cm]:',
            espCondutores= float(raw_input())
        else:
            espCondutores = 0

        print u'Raio condutor                   [mm]:',
        raio = float(raw_input())
        print u'Comprimento da linha            [km]:',
        compLinha = float(raw_input())
    except:
        print u'erro: inesperado'
        return [-1, -1, -1, -1]

    return [espFases, espCondutores, raio, compLinha]

def indutancia():
    """Cálculos para indutância em um sistema trifásico
    """

    print u'Linha trifásica:'
    print u'1 - 1 condutor por fase'
    print u'2 - 2 condutores por fase'
    print u'3 - 3 condutores por fase'
    print u'4 - 4 condutores por fase'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        espFases, espCondutores, raio, comprimento = entradaIndCap(1, 0)
        if espFases == -1:
            return -1
        L, Ds, Dm = bifilar.ind3Fases1Condutores(espFases*1e3, raio)

    elif a == 2:
        espFases, espCondutores, raio, comprimento = entradaIndCap()
        if espFases == -1:
            return -1
        L, Ds, Dm = bifilar.ind3Fases2Condutores(espFases*1e3, espCondutores*10, raio)

    elif a == 3:
        espFases, espCondutores, raio, comprimento = entradaIndCap()
        if espFases == -1:
            return -1
        L, Ds, Dm = bifilar.ind3Fases3Condutores(espFases*1e3, espCondutores*10, raio)

    elif a == 4:
        espFases, espCondutores, raio, comprimento = entradaIndutancia()
        if espFases == -1:
            return -1
        L, Ds, Dm = bifilar.ind3Fases4Condutores(espFases*1e3, espCondutores*10, raio)

    else:
        print u'erro: opção não disponível'
        return -1

    print u'Indutância [H/km]: ', L
    print u'Indutância    [H]: ', L * comprimento
    print u'DsI          [mm]: ', Ds
    print u'Dm           [mm]: ', Dm

    return [L, L*comprimento, Ds, Dm]


def capacitancia():
    """Cálculos para capacitância de um linha de transmissão
    """

    print u'Linha trifásica:'
    print u'1 - 1 condutor por fase'
    print u'2 - 2 condutores por fase'
    print u'3 - 3 condutores por fase'
    print u'4 - 4 condutores por fase'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        espFases, espCondutores, raio, comprimento = entradaIndCap(1, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio)

    elif a == 2:
        espFases, espCondutores, raio, comprimento = entradaIndCap(2, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 2)

    elif a == 3:
        espFases, espCondutores, raio, comprimento = entradaIndCap(3, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 3)

    elif a == 4:
        espFases, espCondutores, raio, comprimento = entradaIndCap(4, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 4)

    else:
        print u'erro: opção não disponível'
        return -1

    print u'Capacitância [H/km]: ', C
    print u'Capacitância    [H]: ', C * comprimento
    print u'DsC            [mm]: ', Ds
    print u'Dm             [mm]: ', Dm

    return [C, C*comprimento, Ds, Dm]

def parametrosLT():
    print """Cálculos para capacitância, indutância e resistência de um linha de transmissão
    """


    print u'Linha trifásica:'
    print u'1 - 1 condutor por fase'
    print u'2 - 2 condutores por fase'
    print u'3 - 3 condutores por fase'
    print u'4 - 4 condutores por fase'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        espFases, espCondutores, raio, comprimento = entradaIndCap(1, 0)
        if espFases == -1:
            return -1

        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio)
        L, DsI, Dm = bifilar.ind3Fases1Condutores(espFases*1e3, raio)

    elif a == 2:
        espFases, espCondutores, raio, comprimento = entradaIndCap(2, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 2)
        L, DsI, Dm = bifilar.ind3Fases2Condutores(espFases*1e3, espCondutores*10, raio)

    elif a == 3:
        espFases, espCondutores, raio, comprimento = entradaIndCap(3, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 3)
        L, DsI, Dm = bifilar.ind3Fases3Condutores(espFases*1e3, espCondutores*10, raio)

    elif a == 4:
        espFases, espCondutores, raio, comprimento = entradaIndCap(4, 0)
        if espFases == -1:
            return -1
        C, Ds, Dm = bifilar.capLT(espFases*1e3, raio, espCondutores*10, 4)
        L, DsI, Dm = bifilar.ind3Fases4Condutores(espFases*1e3, espCondutores*10, raio)

    else:
        print u'erro: opção não disponível'
        return -1

    print u'Indutância   [H/km]: ', L
    print u'Indutância      [H]: ', L * comprimento
    print u'DsI            [mm]: ', DsI
    print u'Capacitância [H/km]: ', C
    print u'Capacitância    [H]: ', C * comprimento
    print u'DsC            [mm]: ', Ds
    print u'Dm             [mm]: ', Dm

    return [C, C*comprimento, Ds, Dm]

def entrada_modelagem(tipo):
    try:
        c = float(raw_input('Comprimento              [km]? '))
        xl = float(raw_input('Reatância indutiva  [ohm/km]? '))
        r = float(raw_input('Resistência          [ohm/km]? '))
    except:
        print 'erro: entrada invalida'
        c = -1
        xl = -1
        r = -1
        xc = -1

    if tipo != 'curta' and c > 0:
        try:
            xc = float(raw_input('Reatância capacitiva [ohm/km]? '))
        except:
            print 'erro: entrada invalida'
            xc = -1

        return [c, xl, r, xc]

    return [c, xl, r]

def modelagem():
    """Modelagem de uma linha de transmissão, seja ela curta, média pi, media T
    ou longa. Cálculos necessários para cada aproximação.
    Para a modelagem de uma linha necessário:
        - o comprimento da linha
        - indutância da linha
        - resistência da linha
        - capacitância da linha
    Com isto é possível obter os parâmetros(A, B, C, D) do quadripolo.
    """

    print '1 - curta'
    print '2 - média pi'
    print '3 - média T'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        c, xl, r = entrada_modelagem('curta')

        linhaAB = linhas.curta(r, xl, c)

        print 'Parâmetros do quadripolo'
        print 'A :', linhaAB.A
        print 'B :', linhaAB.B
        print 'C :', linhaAB.C
        print 'D :', linhaAB.D

        print 'R  [ohm :', linhaAB.R
        print 'XL [ohm]:', linhaAB.XL

    elif a == 2:
        c, xl, r, xc = entrada_modelagem('media_pi')

        linhaAB = linhas.media_pi(r, xl, xc, c)

        print 'Parâmetros do quadripolo'
        print 'A :', linhaAB.A
        print 'B :', linhaAB.B
        print 'C :', linhaAB.C
        print 'D :', linhaAB.D

        print 'R  [ohm]:', linhaAB.R
        print 'XL [ohm]:', linhaAB.XL
        print 'YC [mho]:', linhaAB.Y

    elif a == 3:
        c, xl, r, xc = entrada_modelagem('media_t')

        linhaAB = linhas.media_t(r, xl, xc, c)

        print 'Parâmetros do quadripolo'
        print 'A :', linhaAB.A
        print 'B :', linhaAB.B
        print 'C :', linhaAB.C
        print 'D :', linhaAB.D

        print 'R  [ohm]:', linhaAB.R
        print 'XL [ohm]:', linhaAB.XL
        print 'YC [mho]:', linhaAB.Y


    elif a == 4:
        pass
    else:
        print u'erro: opção não disponível'
        return -1


    return 0

def entrada_quadripolo(topologia = 1):
    """Entrada do usuário para a impedância e susceptância para o quadripolo
    topologia:
        1 - curta
        2 - media pi
        3 - media T
    """

    if topologia == 1:
        print 'Impedância Z[ohm], indutância,'
        R = float(raw_input('R  [ohm] ? '))
        Z = float(raw_input('XL [ohm] ? '))
        Z = R+Z*1j

        return [Z, 0]
    elif topologia >= 2:
        print 'Impedância Z[ohm], indutância,'
        R = float(raw_input('R  [ohm] ? '))
        Z = float(raw_input('XL [ohm] ? '))
        Z = R+Z*1j

        print 'Susceptância Y[mho], capacitância,'
        R = float(raw_input('S [mho] ? '))
        Y = float(raw_input('U [mho] ? '))
        Y = R + Y*1j

        return [Z, Y]
    else:
        print 'erro: opção não disponível'
        return [-1, -1]

def parametros_quadripolo():
    print 'Parâmetros para o quadripolo'

    print '1 - curta'
    print '2 - média pi'
    print '3 - média T'
    print '99 - ajuda'

    try:
        a = input('>')
    except:
        print u'erro: algo inesperado ocorreu na entrada do usuário'
        return -2

    if a == 1:
        Z = entrada_quadripolo(1)[0]
        A, B, C, D = quadripolos.linha_curta(Z)
        print 'Saída,'
        print ' A :', A
        print ' B :', B
        print ' C :', C
        print ' D :', D

    elif a == 2:
        Z, Y = entrada_quadripolo(2)
        A, B, C, D = quadripolos.linha_media_pi(Z, Y)
        print 'Saída,'
        print ' A :', A
        print ' B :', B
        print ' C :', C
        print ' D :', D

    elif a == 3:
        Z, Y = entrada_quadripolo(2)
        A, B, C, D = quadripolos.linha_media_T(Y)
        print 'Saída,'
        print ' A :', A
        print ' B :', B
        print ' C :', C
        print ' D :', D

    elif a == 99:
        print 'erro: Nada aqui!!'
    else:
        print u'erro: opção não disponível'
        return -1

def diversos():
    problemas.problemas()


################################################################################
# Interação homem maquina
# -Ajuda
# -Processamento de comandos
# -Loop principal
################################################################################
def ajuda():
    print 'Comandos cadastrados'
    print u's     - finaliza o programa'
    print u'm     - modelagem de uma carga'
    print u'b     - sistema bifilar'
    print u'i     - indutância sistema trifásico'
    print u'c     - capacitância sistema trifásico'
    print u'q     - quadripolo'
    print u'plt   - parâmetros de um LT: capacitância, indutância e resistência'
    print u'mod   - modelagem de uma linha de transmissão(curta, média(pi, T))'
    print u'pro   - diversos problemas'
    print u'curto - curto circuito'

def sair():
    print u'finalizando...'
    sys.exit(0)

dicionarioComandos = {
    'a' : ajuda,
    's' : sair,
    'm' : entradaCargaMod,
    'b' : sistemaBifilar,
    'i' : indutancia,
    'c' : capacitancia,
    'plt': parametrosLT,
    'mod': modelagem,
    'q': parametros_quadripolo,
    'pro' : diversos,
}

def nada():
    print colortext.BOLD +  colortext.RED + u'erro: comando não reconhecido' + colortext.END

def comandos(cmd):
    return dicionarioComandos.get(cmd, nada)()

################################################################################

if __name__ == '__main__':
    print colortext.BOLD + u'Transmissão de energia elétrica, linhas aéreas' + colortext.END

    while True:
        entrada = raw_input(':')
        if entrada == '':
            continue

        comandos(entrada.lower())

