# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica
#
#-------------------------------------------------------------------------------
# Processo de estratificação do solo
#-------------------------------------------------------------------------------
#

from __future__ import division
#from scipy.optimize import fmin, fmin_slsqp, anneal, basinhopping, brute, leastsq
from scipy.optimize import fmin_slsqp
from math import sqrt, pi, log, exp
from time import time
from xlrd import open_workbook
from numpy import zeros, shape, arange
#from pylab import arange, plot, show
import matplotlib.pyplot as plt
import sys
from os import getcwd
#from scipy.signal import butter
import r1haste
import ConfigParser

#import sympy

from scipy.integrate import quad, romberg, dblquad
from scipy.special import jn, jv
from scipy import Inf


# VARIÁVEIS de controle

infinito = 20 # :)

pho = []
es = []

chuteInicial = [0, 0, 0]

# implementando as restrições para a função de otimização
# no caso foram adotados,
# resistividade da primeira camada varia de 0.1 a 1000 ohm*m
# coeficiente de reflexao de -1 a 1
# profundidade da primeira camada de 0.1 a 100 m
limites = [(0.1, 1000), (-1, 1), (0.1, 100)]

infinitoEndrenyi = 100

debugPlot = None

def iniciaConstantes(ex = None, debug = None):
    global pho, es, chuteInicial, limites

    # valores encontrados no Kindermann
    if ex == 0:

        # OBSERVAÇÃO
        # Estes valores mostrado no livro do Kindermann não caracterizam um solo
        # de 2 camadas. A otimização para duas pode não ser satifatória.
        pho = [320, 245, 182, 162, 168, 152]
        es = [2.5, 5, 7.5, 10, 12.5, 15]
        #chuteInicial = [0, 0, 0] 

    elif ex == 1:

        pho = [996, 974, 858, 696, 549, 361, 276, 230, 210]
        es = [1, 2, 4, 6, 8, 12, 16, 22, 32]
        #chuteInicial = [0, 0, 0]

    elif ex == 2:

        pho = [684, 611, 415, 294, 237, 189, 182]
        es = [1, 2, 4, 6, 8, 16, 32]
        #chuteInicial = [0, 0, 0]

    # tabela do Mamede
    elif ex == 3:
        pho = [470.22200000000004, 
               467.07600000000002, 
               450.27600000000007, 
               409.14800000000002, 
               397.28800000000001]
        es = [2.0, 4.0, 8.0, 16.0, 32.0]
        #chuteInicial = [100, 1, 1]

    ############################################################################
    # estudo de caso encontrado em, Estimation of tow layer soil parameters using
    # finite wenner resistivity expressions. Hans R. Seedher....
    elif ex==4:
        pho = [693.74, 251.62, 84.56, 37.64, 25.32]
        es = [1, 2, 3, 4, 5]
    elif ex == 5:
        pho = [123.33, 189.99, 258.93, 320.27, 374.13]
        es = [2, 4, 6, 8, 10]
    elif ex == 6:
        pho = [102.26, 113.07, 129.77, 147.52, 163.95]
        es = [2, 4, 6, 8, 10]

    ############################################################################

    # if debug:
    #     print 'pho, ', pho
    #     print 'es, ', es
    #     print 'chute, ', chuteInicial

def funcaoEstratificacao(x):
    '''
    entrada:
    x[0] = p1 - resistividade da primeira camada
    x[1] = k  - coeficiente de reflexão
    x[2] = h  - altura da primeira camada
    '''    

    # aplicação da fórmula encontrada no livro do Geraldo volume 2
    f = 0
    for i in range(len(es)):
        s1 = 0
        # inicia o somatorio interno
        for n in range(1, infinito+1):
            s1 = s1 + ((x[1]**n)/sqrt(1+((2*n*x[2])/es[i])**2) - (x[1]**n)/sqrt(4+((2*n*x[2])/es[i])**2))
        # continua acumulando os dados
        f = f + (pho[i]-x[0]*(4*s1+1))**2

    return f

def estratifica2Camadas(debug = None):

    if debug:
        d = 1
        t = time()

        print 'funcao de estratificacao, usando,'
        print 'pho, ', pho
        print 'es, ', es
        print 'chute, ', chuteInicial

    else:
        d = 0

    # aplica a formula de redução basica encontrada do scipy
    #return fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)
    #print fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)
    #val = anneal(funcaoEstratificacao, chuteInicial)
    #val = basinhopping(funcaoEstratificacao, chuteInicial)

    # FUNCIONA
    # Minimize a function using Sequential Least SQuares Programming
    # Python interface function for the SLSQP Optimization subroutine originally implemented by Dieter Kraft.
    [x, fun, nit, status, mes] = fmin_slsqp(funcaoEstratificacao, 
                                            chuteInicial, 
                                            bounds = limites, 
                                            iprint = d, 
                                            full_output = 1)


    #print 'leastsq,'
    #a = leastsq(funcaoEstratificacao, chuteInicial)
    #print a

    if status != 0:
        print '***'
        print 'erro: na otimizacao da funcao de estratificacao'
        print '***'
        print mes

    if debug:
        print x
        print 'tempo execucao(seg), ', time()-t

    return x

def p2solo2Camadas(p1, k):
    # apenas para um solo de 2 camadas
    return -((k+1)*p1)/(k-1)    

def lerPlanilha(planilha, debug = None):
    # p = open_workbook(planilha)
    # for s in p.sheets():
    #     print 'Sheet:', s.name
    #     for row in range(s.nrows):
    #         values = []
    #         for col in range(s.ncols):
    #             values.append(s.cell(row, col).value)
    #         print values
    #     print

    dadosMedidos = open_workbook(planilha)
    
    # inicio dos valores númericos contidos na planilha
    localDados = 2
    # número de linhas utilizadas pela planilha apenas para informações
    qLinhasInf = 2

    for s in dadosMedidos.sheets():
        if debug:
            print 'linhas,', s.nrows
            print 'colunas,', s.ncols

        linhasEfetivas = s.nrows - qLinhasInf
        matrizDados = zeros(shape = (linhasEfetivas, s.ncols))
        for row in range(s.nrows):
            if row >= localDados:
                for col in range(s.ncols):
                    #linha.append(s.cell(row, col).value)
                    matrizDados[row-qLinhasInf, col] = s.cell(row, col).value

        break

    if debug:
        print 'Matriz com os valores de resistividade,'
        print matrizDados

    return matrizDados

def resistividadeMediaPlanilha(mDados, desvioPadrao = 0.5, debug = None):

    [nLinha, nColuna] = shape(mDados)

    mediaResistividade = []
    media = 0
    maximoValor = 0
    minimoValor = mDados[0, 1]

    profundidadeTeste = []
    for l in range(nLinha):
        profundidadeTeste.append(mDados[l, 0])

    if debug:
        print 'Profundidades encontradas,'
        print profundidadeTeste

    # calcula os valores medios sem considerar os desvio padrão
    for l in range(nLinha):
        for c in range(1, nColuna):

            if mDados[l, c] > maximoValor:
                maximoValor = mDados[l, c]
            if mDados[l, c] < minimoValor:
                minimoValor = mDados[l, c]

            media = media + mDados[l, c]

        media = media / (nColuna-1)
        mediaResistividade.append(media)
        media = 0

    if debug:
        print 'Resistividade media,'
        print mediaResistividade

    # tabelaCalculo = zeros(shape = (nLinha, nColuna))
    
    q = 0
    media = 0
    resistividadeCorrigida = []

    # loop para a correção da tabela de resistividade média considerando
    # o desvio padrão de normalmente 50%
    for l in range(nLinha):
        for c in range(1, nColuna):

            if((abs(mDados[l, c]-mediaResistividade[l]))/mediaResistividade[l]) >= desvioPadrao:
                
                if debug:
                    print 'Valor com desvio maior que ', desvioPadrao*100, ' %'
                    print mDados[l, c]
                    print 'linha,', l
                    print 'coluna,', c

            else:

                media = media + mDados[l, c]

                q=q+1

        try:
            resistividadeCorrigida.append(media*q**-1)
        except:
            print 'erro: possivel erro na medicao em,'
            print 'linha, ', l
            print 'coluno, ', c
            print 'PARE COM ISSO PORFAVORRR!!!!'
            resistividadeCorrigida.append(0)
            #exit()
        media = 0
        q = 0

    if debug:
        print 'Resistividade corrigida,'
        print resistividadeCorrigida

    return [profundidadeTeste, resistividadeCorrigida]

def curvaEndrenyiSomatorio(a, p1, p2):

    # aplicação da curva de Endrenyi

    k = (p2 - p1)/(p2 + p1)

    s = 0
    for n in range(1, infinitoEndrenyi+1):
        s += (k**n)/sqrt(1+((2*n/a)**2))
    s = 2*s+1

    return s

def curvaEndrenyi(a, p1, p2):
    """
    Curva de Endrenyi
    Entrada:
    a - alfa, coeficiente de penetração
    p1 - resistividade da n-esima camada
    p2 - resistividade da n-esima+1 camada
    Saída:
    N
    """
    return 2*curvaEndrenyiSomatorio(a, p1, p2) - curvaEndrenyiSomatorio(2*a, p1, p2)

def curvaEndrenyiSomatorioBeta(a, k):

    # aplicação da curva de Endrenyi usando k

    s = 0
    for n in range(1, infinitoEndrenyi+1):
        s += (k**n)/sqrt(1+((2*n/a)**2))
    s = 2*s+1

    return s

def curvaEdnrenyiBeta(a, b):
    """
    Curva de Endrenyi
    Entrada:
    a - alfa, coeficiente de penetração
    b - beta, coeficiente de divergência
    Saída:
    N
    """

    k = (b-1)/(b+1)

    return 2*curvaEndrenyiSomatorioBeta(a, k) - curvaEndrenyiSomatorioBeta(2*a, k)

def plotCurvaEndrenyi():
    #eixo das abscissas 

    # print 'plotando a curva de Endrenyi'

    # alfa = [.1, .2, .5, 1, 2, 5, 10, 20, 50, 75, 100, 200, 500, 1000]
    # beta = .01

    # k = (beta-1)/(beta+1)

    # N = []
    # print 'beta, ', beta
    # print 'k, ', k
    # print 'alfa | N'
    # for i in alfa:
    #     a = curvaEdnrenyiBeta(i, beta)
    #     print i, a
    #     N.append(a)

    # # plt.plot(alfa, N)
    # # plt.xlabel('alfa')
    # # plt.ylabel('N')
    # # plt.grid(True)
    # # plt.show()

    #alfa = [.1, .2, .5, 1, 2, 5, 10, 20, 50, 75, 100, 200, 500, 1000]
    beta = 0.01
    alfa = []
    N = []
    for i in arange(1, 100, 1):
        alfa.append(i)
        N.append(endrenyi1963(beta, i, i))

    plt.plot(alfa, N)
    plt.grid(True)
    plt.show()




# Calculo da resistividade aparente para uma MALHA especifica de terra
# com espaçamento igual entre duas hastes e mesma profundidade
def resistividadeAparente2CamadasMalha(p1, p2, d1, A, D, debug = None):
    '''
    Entrada:
    p1 = resistividade da primeira camada
    p2 = resistividade da segunda camada
    d1 = profundidade da primeira camada
    A = área da malha
    D = dimensão da malha

    Saida:
    pa = resistividade aparente
    A = área da malha
    r = raio da malha
    alfa = coeficiente de penetração
    beta = coeficiente de divergência
    m0 = curva de Endrenyi no ponto alfa
    '''

    #[p1, k, h] = estratifica2Camadas()
    #p2 = p2solo2Camadas(p1, k)
    #print 'p2, ', p2

    ###################################
    # Aplicando as fórmulas de HUMMEL #
    ###################################

    # Área da malha
    #A = (es*(ordem-1))**2

    # Raio do anel equivalente do sistema de aterramento
    #r = sqrt(A/pi)
    r = A/D

    # coeficiente de penetração
    alfa = r/d1

    # coeficiente de divergência
    beta = p2/p1

    # aplicando a curva Endrenyi
    m0 = curvaEndrenyi(alfa, p1, p2)

    # resistividade aparente
    pa = m0*p1

    return [pa, A, r, alfa, beta, m0]

def resistividadeAparente1Haste(l):
    [p1, k, h] = estratifica2Camadas()
    p2 = p2solo2Camadas(p1, k)

def resistividadeAparenteHastesAlinhadas(n, e, p1, p2, h):
    """
    Entrada:
    n = número de hastes cravadas verticalmente 
    e = espaçamento entre as hastes
    p1 = resistividade da primeira camada
    p2 = resistividade da segunda camada
    h = profundidade da primeira camada

    Saída:

    """
    # anel equivalente de Endrenyi
    r = ((n-1)/2)*e

    # coeficiente de penetracao
    alfa = r/h

    # coeficiente de divergência
    beta = p2/p1

    # valor de N para pela curva de Endrenyi
    N = curvaEndrenyi(alfa, p1, p2)

    pa = N*p1

    return [pa, r, alfa, beta, N]


def formulaHummelReducao2Camadas(p, d):
    """
    Entrada:
    p - vetor com a resistividade das camadas
        p = [p1, p2, p3, ..., pn, pn+1]
    d - vetor com o espesura da n-esima camada
        d = [d1, d2, d3, ..., dn]

    Saída:
    peq = resisitividade da primeira camada
    deq = profundidade da primeira camada
    pn1 = resistividade da segunda camada

    Obs: a profundidade da segunda camada é considerada infinita
    """
    if (len(p)-1) != len(d):
        print "erro: tamanho de p e' incoerente com o de d"

    deq = 0
    for i in d:
        deq += i
    den = 0
    for i in range(len(p)-1):
        den += d[i]/p[i]
    peq = deq/den

    return [peq, deq, p[len(p)-1]]

def hasteSoloVariasCamadas(p, l, d):
    """
    Calcula a resistencia de aterramento de uma haste cravada verticalmente 
    em um solo com várias camadas. Conhecida como fórmula de Hummel.
    Entrada:
    p = vetor com a resistividade de cada camada que a haste encontrada
    l = profundidade de cada camada que a haste vê
    d = diâmetro da haste
    Saída:
    pa = resistividade aparente vista pela haste
    r1 = resitência da haste
    """

    if len(p) != len(l):
        print "erro: dimensao de p nao e' coerente com l"

    deq = sum(l)
    den = 0
    for i in range(len(p)):
        den += l[i]/p[i]
    pa = deq/den

    r1 = r1haste.r1haste(pa, deq, d)
    return [pa, r1]

################################################################################
# Curva de Endrenyi, Evaluation of Resistivity tests for design os station 
# grounds in nonuniform soil.
#
# beta = coeficiente de diverência
# alfa = coeficiente de penetração
# phi = razão profundidade da malha com tamanho da camada em que a malha está presente
# a = raio da malha
# d0 = altura dos elementos da malha
#
# Os termos c1, c2, c3, k1, k2, k3 são coeficientes da solução de uma integral
# eliptica. Ver:
# http://en.wikipedia.org/wiki/Elliptic_integral 
# http://mathworld.wolfram.com/EllipticIntegral.html
# 
# OBS: No artigo do Endrenyi ele informa que para valores de d0 = 1 e phi = 0.5
# a margem de erro é pequena para casos praticos.
################################################################################

def c1(m, phi, alfa): 
    return sqrt(1 + ((m+phi)/alfa)**2)

def c2(m, phi, alfa): 
    return sqrt(1 + ((m-phi)/alfa)**2)

def c3(m, alfa): 
    return sqrt(1 + ((m)/alfa)**2)

def k1(m, phi, alfa): 
    return alfa/sqrt(alfa**2 + (m+phi)**2)

def k2(m, phi, alfa): 
    return alfa/sqrt(alfa**2 + (m-phi)**2)

def k3(m, alfa): 
    return alfa/sqrt(alfa**2 + m**2)

# Equacionamento válido apenas para quando p1>p2
def endrenyi1963(beta,  alfa, a, phi = 0.5, d0 = 1):
    # boa margem de erro
    infE = 100

    if alfa < 1:
        print 'erro: esta funcao nao pode ser usada para p2>p1'

    # coeficiente de divergência, letra micro para o Endrenyi
    micro = (beta-1)/(beta+1)

    # inicia o somátorio
    s = 0
    for m in range(1, infE+1):
        #s += (micro**m)*(k1(m, phi, alfa)/c1(m, phi, alfa) + (2*k3(m, alfa))/c3(m, alfa) + k2(m, phi, alfa)/c2(m, phi, alfa))

        s += (micro**m)*(k1(m, phi, alfa)/c1(m, phi, alfa) \
             + (2*k3(m, alfa))/c3(m, alfa) \
             + k2(m, phi, alfa)/c2(m, phi, alfa))

    N = 1 + (s / (log((16*a)/d0) + k1(0, phi, alfa)/c1(0, phi, alfa)))

    return N

################################################################################
# Equacionamento para estratificação do solo em várias camadas
# Documentação utilizada:
# [1] T. Takahashi, T. Kawase: Calculation of earth resistance for a deep- driven rod in a multi-layer earth structure
#pTT = [1, 100]
#hTT = [1, 1]

def kiTT(pTT, hTT, i):
    if i == 0:
        return 1
    i-=1
    return (pTT[i+1]-pTT[i])/(pTT[i+1]+pTT[i])

def alfaTT(pTT, hTT, N1, N2, la):
    N1-=1
    N2-=1

    if N1 == N2:
        return 1

    r = alfaTT(pTT, hTT, N1, N2+1, la)+ \
        kiTT(pTT, hTT, N2+1)* \
        betaTT(pTT, hTT, N1, N2+1, la)* \
        exp(-2*la*hTT[N2+1])

    return r

def betaTT(pTT, hTT, N1, N2, la):
    N1-=1
    N2-=1

    if N1 == N2:
        return 0

    r = kiTT(pTT, hTT, N2+1)* \
        alfaTT(pTT, hTT, N1, N2+1, la)+ \
        betaTT(pTT, hTT, N1, N2+1, la)* \
        exp(-2*la*hTT[N2+1])

    return r

def HsTT(hTT):
    return sum(hTT)

def HNMenos1(hTT, N):
    r = 0
    for  i in hTT[:(N-1)]:
        r+=i

    return r

def parteA_TakahashiKawase(h, p, l, N, a):
    r = 0
    for i in range(0, N-1):
        r+=h[i]/p[i]
    r+=(l-HNMenos1(h, N))/p[N-1]
    r=(1/(2*pi))*(1/r)

    return r

def parteB_TakahashiKawase(h, p, l, N, a):
    r = 0
    for s in range(1, N+1):
        for i in range(s):
            (1-kiTT(p, h, i))

            f = lambda t, la: (exp(-la*t)/(1-0.818*exp(-2*la)))*jn(0, la)
            r = (1-.818)*dblquad(f, 0, Inf, lambda t: 1, lambda t: 2)[0]

    return r

def duasCamadasTakahashiKawase():
    #f = lambda t, la: (exp(-la*t)/(1-0.818*exp(-2*la)))*jn(0, la)
    #r = (1-.818)*dblquad(f, 0, Inf, lambda t: 1, lambda t: 2)[0]    
    k1 = 0.818
    h = 1
    l = 2
    x = 1
    p1 = 10
    I1 = 1


    a = lambda t, la: (exp(-la*t)/(1-k1*exp(-2*la*h)))*jv(0, la*x)
    r1 = (1-k1)*dblquad(a, 0, Inf, lambda t: h, lambda t: l)[0]

    b = lambda t, la: ((exp(-la*t)+k1*exp(-2*la*h)*exp(-la*t))/(1-k1*exp(-2*la*h)))*jv(0, la*x)
    r2 = dblquad(b, 0, Inf, lambda t: 0, lambda t: h, full_output = True)[0]

    f = (r1+r2)*((p1*I1)/2*pi)

    print 'r1, ', r1
    print 'r2, ', r2
    print 'f , ', f

def testeTT():
    pTT = [10, 100]
    hTT = [5, 0]
    N = 2
    l = 30
    a = 1

    print '- '*40
    print u'Iniciando teste para as funções de Takahashi e Kawase'
    print
    print 'alfa   , ', alfaTT(pTT, hTT, N, 1, 1)
    print 'beta   , ', betaTT(pTT, hTT, N, 1, 1)
    print 'Hs     , ', HsTT(hTT)
    print 'HN-1   , ', HNMenos1(hTT, N)
    print 'parte A, ', parteA_TakahashiKawase(hTT, pTT, l, N, a)
    print 'parte B, ', parteB_TakahashiKawase(hTT, pTT, l, N, a)

    print 
    print 'Solo em duas camadas'
    duasCamadasTakahashiKawase()

    return 0



################################################################################
# ROTINAS DE TESTE
################################################################################
def testeEstratificacaoArquivos():
    dirAtual = getcwd()
    pastaTabelas = "tabelas"
    planilhas = [dirAtual+"\\"+pastaTabelas+"\\"+"tabelaExemplo2_12GeraldoKindermann.xlsx", 
                 dirAtual+"\\"+pastaTabelas+"\\"+"subestacaoMamede.xlsx"]
    
    #--------------------------------------------------------------------------
    # testa a estratificação em duas camadas
    print 'Inciando teste de estratificacao em 2 camadas,'

    for i in range(7):

        print
        print 'caso, ', i

        iniciaConstantes(i, debug = True)
        [p1, k, h] = estratifica2Camadas(debug = True)
        print 'valores,'
        print 'p1, ', p1
        print 'k, ', k
        print 'h, ', abs(h)
        print 'p2, ', p2solo2Camadas(p1, k)

        print '_'*80

    print 'testando individualmente a funcao de estratificacao'
    iniciaConstantes(0, debug = True)
    print 'saida, ', funcaoEstratificacao([364.67, -0.43, -2.827])
    print '-'*40
    iniciaConstantes(3, debug = True)
    print 'saida, ', funcaoEstratificacao([12, 0, 0])
    print '-'*40
    iniciaConstantes(3, debug = True)
    print 'saida, ', funcaoEstratificacao([472, 0.088811995, 7.8])

    print
    print '**fim'
    print '_'*80

    #--------------------------------------------------------------------------
    # testa a leitura da planilha com os dados
    
    print 'Iniciando teste leitura de uma planilha' 

    for i in planilhas:
        print 'lendo planilha, ', i
        m = lerPlanilha(i, debug = True)
        [phoTabela, esTabela] = resistividadeMediaPlanilha(m, debug = True)
        print 'retorno, '
        print phoTabela
        print esTabela

        pho = esTabela
        es = phoTabela

        print pho, es

        if debugPlot:
            plt.plot(phoTabela, esTabela)
            plt.show()

        [p1, k, h] = estratifica2Camadas(debug = True)
        print 'valores, '
        print 'p1, ', p1
        print 'k, ', k
        print 'h, ', h
        print 'p2, ', p2solo2Camadas(p1, k)

        print '-'*80

    print

def testeResistividadeAparente():
    #--------------------------------------------------------------------------
    # testando os cálculos de resistividade aparente    

    #print 'calculando a resistividade aparente'

    #ordem = 4
    #espacamento = 3
    #prof = 16

    #pa = resistividadeAparente2CamadasMalha(ordem, espacamento, prof)

    #print 'resistividade aparente calculada, '
    #print 'pa, ', pa

    print 'resistividade para hastes alinhadas'
    # exemplo do Kindermann
    n = 7
    e = 3
    deq = 8
    p1 = 247
    p2 = 80
    pa = resistividadeAparenteHastesAlinhadas(n, e, p1, p2, deq)
    print 'pa, ', pa

    #--------------------------------------------------------------------------

    print 'testando a formula de hummel para reducao de 2 camadas'
    print 'para haste unica e verticalmente no solo'
    
    print 'caso 1'
    # exemplo do Kindermann
    p = [200, 500, 65, 96]
    d = [1, 6, 1]
    print 'resultado, ', formulaHummelReducao2Camadas(p, d)

    print 'caso 2'
    p = [300, 450, 100, 20]
    d = [2, 3, 4]
    print 'resultado, ', formulaHummelReducao2Camadas(p, d)

    print 'caso 3'
    p = [500, 200, 120]
    d = [2, 5]
    print 'resultado, ', formulaHummelReducao2Camadas(p, d)

    print 'haste unica vertical cravada em um solo com varias camadas'
    p = [500, 200, 120]
    l = [2, 5, 3]
    pa = hasteSoloVariasCamadas(p, l, 15e-3)
    print pa    

    print

def testeCurvasEndrenyi():
    # curvas de Endrenyi

    #--------#
    # caso 1 #
    #--------#
    alfa = 1.15
    beta = 4.3
    
    N = curvaEdnrenyiBeta(alfa, beta)

    print 'curva de Endrenyi, caso 1'
    print 'alfa, ', alfa
    print 'beta, ', beta
    print 'N, ', N

    print

    #--------#
    # caso 2 #
    #--------#
    alfa = .3333
    beta = .119
    
    N = curvaEdnrenyiBeta(alfa, beta)

    print 'curva de Endrenyi, caso 2'
    print 'alfa, ', alfa
    print 'beta, ', beta
    print 'N, ', N

    #--------#
    # caso 3 #
    #--------#
    alfa = 2.6
    beta = .138
    
    N = curvaEdnrenyiBeta(alfa, beta)

    print 'curva de Endrenyi, caso 3'
    print 'alfa, ', alfa
    print 'beta, ', beta
    print 'N, ', N


    plotCurvaEndrenyi()

    print
    print '**fim'
    print '_'*80


    print 'Curva de proposta por Endrenyi em 1963,'
    print endrenyi1963(.138, 2.603, 31.23, 0.5,  1)

################################################################################

if __name__ == '__main__':     

    print u'Biblioteca: Estratificação'

    #testeEstratificacaoArquivos()
    #testeResistividadeAparente()
    #testeCurvasEndrenyi()
    testeTT()

    #saida = raw_input('[ENTER] para sair')
