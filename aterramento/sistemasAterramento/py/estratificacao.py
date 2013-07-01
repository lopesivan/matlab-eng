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
from scipy.optimize import fmin, fmin_slsqp, anneal, basinhopping, brute, leastsq
from math import sqrt, pi
from time import time
from xlrd import open_workbook
from numpy import zeros, shape, arange
#from pylab import arange, plot, show
import matplotlib.pyplot as plt
import sys
from os import getcwd
from scipy.signal import butter


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

infinitoEndrenyi = 1000

debugPlot = None

def iniciaConstantes(ex = None, debug = None):
    global pho, es, chuteInicial, limites

    # valores encontrados no Geraldo
    if ex == 0:

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

        resistividadeCorrigida.append(media*q**-1)
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
    return 2*curvaEndrenyiSomatorio(a, p1, p2) - curvaEndrenyiSomatorio(2*a, p1, p2)

def curvaEndrenyiSomatorioBeta(a, k):

    # aplicação da curva de Endrenyi

    s = 0
    for n in range(1, infinitoEndrenyi+1):
        s += (k**n)/sqrt(1+((2*n/a)**2))
    s = 2*s+1

    return s

def curvaEdnrenyiBeta(a, b):
    k = (b-1)/(b+1)
    return 2*curvaEndrenyiSomatorioBeta(a, k) - curvaEndrenyiSomatorioBeta(2*a, k)

def plotCurvaEndrenyi():
    #eixo das abscissas 

    print 'plotando a curva de Endrenyi'

    alfa = arange(0.01, 1000, 1)    
    N = []
    for i in alfa:
        N.append(curvaEndrenyi(i))

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
    d - vetor com o espesura da n-esima camada

    Saída:
    peq = resisitividade da primeira camada
    deq = profundidade da primeira camada
    pn1 = resistividade da segunda camada
    """
    if len(p) != len(d):
        print "erro: tamanho de p e' incoerente com o de d"

    deq = 0
    for i in d:
        deq += i
    den = 0
    for i in range(len(p)):
        den += d[i]/p[i]
    peq = deq/den

    return [peq, deq, p[len(p)-1]]

if __name__ == '__main__':

    dirAtual = getcwd()
    pastaTabelas = "tabelas"
    planilhas = [dirAtual+"\\"+pastaTabelas+"\\"+"tabelaExemplo2_12GeraldoKindermann.xlsx", 
                 dirAtual+"\\"+pastaTabelas+"\\"+"subestacaoMamede.xlsx"]
    
    #--------------------------------------------------------------------------
    # testa a estratificação em duas camadas
    print 'Inciando teste de estratificacao em 2 camadas,'

    for i in range(4):
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
    # exemplo do Kindermann
    p = [200, 500, 65]
    d = [1, 6, 1]
    print 'resultado, ', formulaHummelReducao2Camadas(p, d)

    plotCurvaEndrenyi()

    print
    print '**fim'
    print '_'*80

    #saida = raw_input('[ENTER] para sair')
