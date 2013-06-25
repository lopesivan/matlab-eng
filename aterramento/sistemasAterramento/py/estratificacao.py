# -*- coding: cp1252 -*-
from __future__ import division
from scipy.optimize import fmin, fmin_slsqp
from math import sqrt
from time import time
from xlrd import open_workbook
from numpy import zeros, shape

infinito = 20 # :)
numeroMaximoFuncoes = 1e8

pho = []
es = []
chuteInicial = []

def iniciaConstantes(ex = None, debug = None):
    global pho, es, chuteInicial

    if ex == None:
        pho = [320, 245, 182, 162, 168, 152]
        es = [2.5, 5, 7.5, 10, 12.5, 15]
        chuteInicial = [0, 0, 0]    
    elif ex == 0:
        pho = [996, 974, 858, 696, 549, 361, 276, 230, 210]
        es = [1, 2, 4, 6, 8, 12, 16, 22, 32]
        chuteInicial = [0, 0, 0]

    if debug:
        print 'pho, ', pho
        print 'es, ', es
        print 'chute, ', chuteInicial

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
    else:
        d = 0

    # aplica a formula de redução basica encontrada do scipy
    #return fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)
    #print fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)

    val = fmin_slsqp(funcaoEstratificacao, chuteInicial, iprint = d)

    if debug:
        print val
        print 'tempo execucao(seg), ', time()-t

    return val

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
        print 'Resistividade média,'
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

def resistividadeAparente2Camadas(debug = None):
    [p1, k, h] = estratifica2Camadas()
    p2 = p2solo2Camadas(p1, k)

    print 'p2, ', p2

    #Aplicando as fórmulas de HUMMEL

    #coeficiente de divergência
    beta = p2/p1




if __name__ == '__main__':
    planilha = "tabelaExemplo2_12GeraldoKindermann.xlsx"
    
    # testa a estratificação em duas camadas
    print 'Inciando teste de estratificação em 2 camadas,'

    iniciaConstantes(debug = True)
    print 'saida, ', estratifica2Camadas(debug = True)

    print '_'*80
    print 'testando individualmente a funcao de estratificacao'
    print 'saida, ', funcaoEstratificacao([364.67, -0.43, -2.827])

    print '_'*80

    iniciaConstantes(0, debug = True)
    print 'saida, ', estratifica2Camadas(debug = True)

    print
    print '**fim'
    print '_'*80

    # testa a leitura da planilha com os dados
    print 'Iniciando teste leitura de uma planilha'
    m = lerPlanilha(planilha, debug = True)
    [p, r] = resistividadeMediaPlanilha(m, debug = True)
    print 'Retorno,'
    print p
    print r

    print
    print '**fim'
    print '_'*80

    resistividadeAparente2Camadas()

    #saida = raw_input('[ENTER] para sair')
