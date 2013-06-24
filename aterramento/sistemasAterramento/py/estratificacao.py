# -*- coding: cp1252 -*-
from scipy.optimize import fmin, fmin_bfgs
from math import sqrt
from time import time
from xlrd import open_workbook
from numpy import zeros, shape

infinito = 10 # :)
numeroMaximoFuncoes = 1e8

def funcaoEstratificacao(x):
    '''
    entrada:
    x[0] = p1
    x[1]= k
    x[2] = h
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

def estratifica2Camadas():
    t = time()

    # aplica a formula de redução basica encontrada do scipy
    return fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)
    
    print time()-t

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


if __name__ == '__main__':
    global pho, es, chuteInicial
    planilha = "tabelaExemplo2_12GeraldoKindermann.xlsx"
    
    # testa a estratificação em duas camadas
    print 'Inciando teste de estratificação em 2 camadas,'
    pho = [320, 245, 182, 162, 168, 152]
    es = [2.5, 5, 7.5, 10, 12.5, 15]
    chuteInicial = [0, 0, 0]

    print estratifica2Camadas()
    print '**fim'

    # testa a leitura da planilha com os dados
    print 'Iniciando teste leitura de uma planilha'
    m = lerPlanilha(planilha, debug = True)
    [p, r] = resistividadeMediaPlanilha(m, debug = True)
    print 'Retorno,'
    print p
    print r
    print '**fim'

    #saida = raw_input('[ENTER] para sair')
