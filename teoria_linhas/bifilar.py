#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felippe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

# Transmissão Bifilar, aérea

from __future__ import division
import sys
from math import sqrt, exp, log, pi

def impedanciaNatural(L, C):
    return sqrt(L/C)

def energiaCampoMagnetico(I0, L):
    return ((I0**2)*L)/2

def correnteI0(U, Z0):
    return U/Z0

def energiaCampoEletrico(U, C):
    return ((U**2)*C)/2

def velocidadePropagacao(L, C):
    return 1/sqrt(L*C)

def Ur(Z2, Z0, Ud):
    return kr(Z2, Z0)*Ud

def Ir(Z2, Z0, Id):
    return kr(Z2, Z0)*Id

def kr(Z2, Z0):
    """ Coeficiente de reflexão """
    if (Z2+Z0)==0 or (Z2-Z0)== 0:
        print u'aviso: divisão por zero no coeficiente de reflexão'
        return 0
    return (Z2-Z0)/(Z2+Z0)

def tempoPropagacao(l, v):
    return l/v

def ondasViajantes(R2, Z0):
    print
    print u'Informações relevantes:'
    print

    if R2>Z0:
        print "R2 > Z0"
        print u"""-a onda de tensão refletida possui o mesmo sinal
que a onda de tensão incidente. A tensão resultante será, então,
maior do que a da onda incidente.
- a onda da corrente refletida possui sinal contrário do da onda
incidente, resultanto em corrente menor do que a incidente.
"""
    elif R2==Z0:
        print "R2 igual Z0"
        print u"""- tanto a onda refletida da tensão como a da corrente
são nulas, não havendo, portanto, alterações em seus valores.
"""
    elif R2<Z0:
        print "R2 < Z0"
        print u"""- a onda da tensão se reflete com sinal oposto ao da
incidente, resultando em diminuição da tensão.
- a onda da corrente se reflete com o mesmo sinal, o que leva ao seu
aumento.
"""

def exemplo1():
    print """Uma linha de transmissão bifilar aérea é suprida por
uma fonte de tensão constante e igual a 800[volt]. A indutância
dos condutores é de 0.001358[henry/m](fluxo interno considerado)
sua capacitância é igual a 0.008488e-6 [farad/km]
Tratando-se de uma linha sem perdas, deseja-se saber, sendo
seu comprimento igual a 100[km]
a - sua impedância natural
b - energia armazenada por quilômetro de linha nos campos
elétricos e magnéticos
c - velocidade de propagação
d - qual o valor da tensão no recpetor no decorrido tempo
t=(3l)/v do instante em que a linha foi energizada, para as
seguintes condições:
a - z2 = 100 [ohm]
b - z2 = 400 [ohm]
c - z2 = 1600 [ohm]
"""

    tensao = 800
    induCondutor = 0.001358
    capaCondutor = 0.008488e-6
    cLinhakm = 100

    Z0 = impedanciaNatural(induCondutor, capaCondutor)
    I0 = correnteI0(tensao, Z0)
    Em = energiaCampoMagnetico(I0, induCondutor)
    Ee = energiaCampoEletrico(tensao, capaCondutor)
    Et = Em+Ee  # energia total armazenada
    v = velocidadePropagacao(induCondutor, capaCondutor)

    Z2a = 100
    Z2b = 400
    Z2c = 1600

    #ondasViajantes(Z2a, Z0)
    #ondasViajantes(Z2b, Z0)
    #ondasViajantes(Z2c, Z0)

    # para Z2a
    kru2_Z2a = kr(Z2a, Z0)
    U2a_2 = tensao*(1-kru2_Z2a**2)
    U2a_1 = tensao*(1+kru2_Z2a)
    # para Z2b
    kru2_Z2b = kr(Z2b, Z0)
    U2b_2 = tensao*(1-kru2_Z2b**2)
    U2b_1 = tensao*(1+kru2_Z2b)
    # para Z2c
    kru2_Z2c = kr(Z2c, Z0)
    U2c_2 = tensao*(1-kru2_Z2c**2)
    U2c_1 = tensao*(1+kru2_Z2c)

    print u'Impedância natural [ohm]:', Z0
    print u'Corrente I0[A]          :', I0
    print u'Energia magnética [Ws]  :', Em
    print u'Energia elétrica [Ws]   :', Ee
    print u'Energia total [Ws]      :', Et
    print u'Velocidade prop. [km/s] :', v

    print u'coeficientes de reflexão:'
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2a, kru2_Z2a, U2a_2, U2a_1)
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2b, kru2_Z2b, U2b_2, U2b_1)
    print u'> Z2 = %f -> kr = %f, u2_2 = %f, u2_1 = %f' % (Z2c, kru2_Z2c, U2c_2, U2c_1)

def problema1(tensao, capaCondutor, induCondutor, comprimento, Zs, debug = False):

    Z0 = impedanciaNatural(induCondutor, capaCondutor)
    I0 = correnteI0(tensao, Z0)
    Em = energiaCampoMagnetico(I0, induCondutor)
    Ee = energiaCampoEletrico(tensao, capaCondutor)
    Et = Em+Ee  # energia total armazenada
    v = velocidadePropagacao(induCondutor, capaCondutor)

    Z2a, Z2b, Z2c = Zs
    # para Z2a
    kru2_Z2a = kr(Z2a, Z0)
    U2a_2 = tensao*(1-kru2_Z2a**2)
    U2a_1 = tensao*(1+kru2_Z2a)
    # para Z2b
    kru2_Z2b = kr(Z2b, Z0)
    U2b_2 = tensao*(1-kru2_Z2b**2)
    U2b_1 = tensao*(1+kru2_Z2b)
    # para Z2c
    kru2_Z2c = kr(Z2c, Z0)
    U2c_2 = tensao*(1-kru2_Z2c**2)
    U2c_1 = tensao*(1+kru2_Z2c)

    U22 = [U2a_2, U2b_2, U2c_2]
    U21 = [U2a_1, U2b_1, U2c_1]

    return [Z0, I0, Em, Ee, Et, v, U22, U21]

def exemploLinhaAssimetrica():
    D12 = 20
    D23 = 20
    D31 = 38
    Ds = 0.0373

    Deq, La = linhaInduEspAssimetrico(D12, D23, D31, Ds)
    print 'Linha assimetrica'
    print 'Deq: ', Deq
    print 'L  : ', La

def indLinhaMono2Fios(D, rl):
    """Indutância de uma linha monofásica a dois fios
    Entrada:
        D - espaçamento entre os condutores [metros]
        rl - raio do condutor   [metros]
    Saída:
        Indutância por metro
    """
    return 4e-7*log(D/rl)

def indLinha3Fases_HKm(Dm, Ds):
    """
    Introdução teórica:
        Um linha de transmissão de energia elétrica possui quatro
        parâmetros: resistência, indutância, capacitância e condutância.
        que influem em seu comportamente como componentes de um
        sistema de potência. A condutância entre condutores ou entre
        condutor e terra leva em conta a corrente de fuga nos isoladores
        das linhas aéreas de transmissão ou na isolção dos cabos
        subterrâneos. No entanto, a condutância entre condutores de
        uma linha aérea pode ser considerada nula pois a fuga nos
        seus isoladores é desprezível. Uma variação de corrente nos
        condutores provoca uma variação do número de linhas de fluxo
        magnético contatenadas com o circuito. Por sua vez, qualquer
        vairação do fluxo concatenado com o circuito lhe induz uma
        tensão, cujo valor é proporcional à taxa de variação do fluxo.
        Indutância é o parâmetro do circuito que relaciona a tensão
        induzida por variação de fluxo com a taxa de variação da corrente.
        Com maior diâmetro, a densidade de fluxo elétrico na superfície
        do condutor de aluminio é menor que a mesma tensão. Isto
        significa menor gradiente de potencial na superfície e menor
        tendência à ionização do ar em volta do condutor. Esta ionização
        do ar produz um efeito chamado efeito corona.
    """
    return 2e-4*log(Dm/Ds)

def ds1Condutor(R):
    """Ds para um 1 condutor por fase, em um sistema trifásico
    Entrada:
        R - raio do condutor
    """
    return exp(-1/4)*R

def ds2Condutores(R, d):
    """Ds para um 2 condutor por fase, em um sistema trifásico
    Entrada:
        R - raio do condutor
        d - espaçamento entre os condutores
    """
    return (exp(-1/4)*R*d)**(1/2)

def ds3Condutores(R, d):
    """Ds para um 3 condutor por fase, em um sistema trifásico
    Entrada:
        R - raio do condutor
        d - espaçamento entre os condutores
    """
    return (exp(-1/4)*R*d**2)**(1/3)

def ds4Condutores(R, d):
    """Ds para um 4 condutor por fase, em um sistema trifásico
    Entrada:
        R - raio do condutor
        d - espaçamento entre os condutores
    """
    return (exp(-1/4) * (2**(1/2)) * R * (d**3))**(1/4)

def dmLinha3FasesEspUnico(d):
    """Espaçamento Dm entre os condutores, considerando que
    os mesmo estão a uma mesma distância tanto da linha ou coluna.
    Entrada:
        d - Espaçamento
    """
    return (d*d*(d+d))**(1/3)

def ind3Fases1Condutores(EspFases, RaioCondutores):
    """ Indutância em um sistema trifásico com 1 condutor
    por fase.
    Entrada:
        EspFases - Espaçamento entre as fases
        EspCondutores - Espaçamento entre os condutores
        RaioCondutores - Raio dos condutores
    Saída:
        L - indutância [Henry/Km]
        Ds
        Dm
    """
    Ds = ds1Condutor(RaioCondutores)
    Dm = dmLinha3FasesEspUnico(EspFases)
    L = indLinha3Fases_HKm(Dm, Ds)

    return [L, Ds, Dm]

def ind3Fases2Condutores(EspFases, EspCondutores, RaioCondutores):
    """ Indutância em um sistema trifásico com 2 condutores
    por fase.
    Entrada:
        EspFases - Espaçamento entre as fases
        EspCondutores - Espaçamento entre os condutores
        RaioCondutores - Raio dos condutores
    Saída:
        L - indutância [Henry/Km]
        Ds
        Dm
    """
    Ds = ds2Condutores(RaioCondutores, EspCondutores)
    Dm = dmLinha3FasesEspUnico(EspFases)
    L = indLinha3Fases_HKm(Dm, Ds)

    return [L, Ds, Dm]

def ind3Fases3Condutores(EspFases, EspCondutores, RaioCondutores):
    """ Indutância em um sistema trifásico com 3 condutores
    por fase.
    Entrada:
        EspFases - Espaçamento entre as fases
        EspCondutores - Espaçamento entre os condutores
        RaioCondutores - Raio dos condutores
    Saída:
        L - indutância [Henry/Km]
        Ds
        Dm
    """
    Ds = ds3Condutores(RaioCondutores, EspCondutores)
    Dm = dmLinha3FasesEspUnico(EspFases)
    L = indLinha3Fases_HKm(Dm, Ds)

    return [L, Ds, Dm]

def ind3Fases4Condutores(EspFases, EspCondutores, RaioCondutores):
    """ Indutância em um sistema trifásico com 4 condutores
    por fase.
    Entrada:
        EspFases - Espaçamento entre as fases
        EspCondutores - Espaçamento entre os condutores
        RaioCondutores - Raio dos condutores
    Saída:
        L - indutância [Henry/Km]
        Ds
        Dm
    """
    Ds = ds4Condutores(RaioCondutores, EspCondutores)
    Dm = dmLinha3FasesEspUnico(EspFases)
    L = indLinha3Fases_HKm(Dm, Ds)

    return [L, Ds, Dm]

def dsCapacitor1Condutores(R):
    """Ds para a análise capacitiva de uma linha trifásica
    Entrada:
        R - Raio real dos condutores
    Saída:
        Ds
    """

    # usando a mesma fórmula para o Ds indutivo só que retirando
    # o termo exp(-1/4)
    return ds1Condutor(R/exp(-1/4))

def dsCapacitor2Condutores(R, d):
    """Ds para a análise capacitiva de uma linha trifásica
    Entrada:
        R - Raio real dos condutores
        d - espaçamento entre os condutores
    Saída:
        Ds
    """

    return ds2Condutores(R/exp(-1/4), d)

def dsCapacitor3Condutores(R, d):
    """Ds para a análise capacitiva de uma linha trifásica
    Entrada:
        R - Raio real dos condutores
        d - espaçamento entre os condutores
    Saída:
        Ds
    """

    return ds3Condutores(R/exp(-1/4), d)

def dsCapacitor4Condutores(R, d):
    """Ds para a análise capacitiva de uma linha trifásica
    Entrada:
        R - Raio real dos condutores
        d - espaçamento entre os condutores
    Saída:
        Ds
    """

    return ds4Condutores(R/exp(-1/4), d)

def formCapLT(Dm, Ds):
    """Capacitância para uma linha trifásica
    Entrada:
        Dm
        Ds
    Saída:
        Capacitância em km
    """
    C = (2*pi*8.85e-9)/log(Dm/Ds)
    return C

def capLT(EspFases, RaioCondutores, EspCondutores, NumCondutores = 1):
    """ Capacitância em uma linha de transmissao.
    Entrada:
        EspFases - Espaçamento entre as fases
        RaioCondutores - Raio dos condutores
        EspCondutores - espaçamento entre os condutores
        NumCondutores - Número de condutores por fase
    Saída:
        C - capacitância [C/Km]
        Ds
        Dm
    """
    if EspFases > 0:
        if NumCondutores == 1:
            Ds = dsCapacitor1Condutores(RaioCondutores)
        elif NumCondutores == 2:
            Ds = dsCapacitor2Condutores(RaioCondutores, EspCondutores)
        elif NumCondutores == 3:
            Ds = dsCapacitor3Condutores(RaioCondutores, EspCondutores)
        elif NumCondutores == 4:
            Ds = dsCapacitor4Condutores(RaioCondutores, EspCondutores)
        else:
            print 'erro: formula para esse número (%d) de condutores não disponivel' % NumCondutores
            return -1
        Dm = dmLinha3FasesEspUnico(EspFases)
        C = formCapLT(Dm, Ds)

    return [C, Ds, Dm]


def zonaTeste():
    print 'Zona de teste'
    print

    print 'Ds capacitor, 3 condutores: ', dsCapacitor3Condutores(16, 420)

if __name__ == '__main__':
    print u'Transmissão bifilar'

    exemplo1()
    zonaTeste()

