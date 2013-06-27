# -*- coding: cp1252 -*-
from __future__ import division
from scipy.optimize import fmin, fmin_slsqp, anneal, basinhopping, brute
from math import sqrt
from time import time
from xlrd import open_workbook
from numpy import zeros, shape
from pylab import arange, plot, show

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
    elif ex == 1:
        pho = [684, 611, 415, 294, 237, 189, 182]
        es = [1, 2, 4, 6, 8, 16, 32]
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
    #val = anneal(funcaoEstratificacao, chuteInicial)
    #val = basinhopping(funcaoEstratificacao, chuteInicial)


    # FUNCIONA
    # Minimize a function using Sequential Least SQuares Programming
    # Python interface function for the SLSQP Optimization subroutine originally implemented by Dieter Kraft.

    """
    Minimize a function using Sequential Least SQuares Programming

    Python interface function for the SLSQP Optimization subroutine
    originally implemented by Dieter Kraft.

    Parameters
    ----------
    func : callable f(x,*args)
        Objective function.
    x0 : 1-D ndarray of float
        Initial guess for the independent variable(s).
    eqcons : list
        A list of functions of length n such that
        eqcons[j](x,*args) == 0.0 in a successfully optimized
        problem.
    f_eqcons : callable f(x,*args)
        Returns a 1-D array in which each element must equal 0.0 in a
        successfully optimized problem.  If f_eqcons is specified,
        eqcons is ignored.
    ieqcons : list
        A list of functions of length n such that
        ieqcons[j](x,*args) >= 0.0 in a successfully optimized
        problem.
    f_ieqcons : callable f(x,*args)
        Returns a 1-D ndarray in which each element must be greater or
        equal to 0.0 in a successfully optimized problem.  If
        f_ieqcons is specified, ieqcons is ignored.
    bounds : list
        A list of tuples specifying the lower and upper bound
        for each independent variable [(xl0, xu0),(xl1, xu1),...]
    fprime : callable `f(x,*args)`
        A function that evaluates the partial derivatives of func.
    fprime_eqcons : callable `f(x,*args)`
        A function of the form `f(x, *args)` that returns the m by n
        array of equality constraint normals.  If not provided,
        the normals will be approximated. The array returned by
        fprime_eqcons should be sized as ( len(eqcons), len(x0) ).
    fprime_ieqcons : callable `f(x,*args)`
        A function of the form `f(x, *args)` that returns the m by n
        array of inequality constraint normals.  If not provided,
        the normals will be approximated. The array returned by
        fprime_ieqcons should be sized as ( len(ieqcons), len(x0) ).
    args : sequence
        Additional arguments passed to func and fprime.
    iter : int
        The maximum number of iterations.
    acc : float
        Requested accuracy.
    iprint : int
        The verbosity of fmin_slsqp :

        * iprint <= 0 : Silent operation
        * iprint == 1 : Print summary upon completion (default)
        * iprint >= 2 : Print status of each iterate and summary
    disp : int
        Over-rides the iprint interface (preferred).
    full_output : bool
        If False, return only the minimizer of func (default).
        Otherwise, output final objective function and summary
        information.
    epsilon : float
        The step size for finite-difference derivative estimates.

    Returns
    -------
    out : ndarray of float
        The final minimizer of func.
    fx : ndarray of float, if full_output is true
        The final value of the objective function.
    its : int, if full_output is true
        The number of iterations.
    imode : int, if full_output is true
        The exit mode from the optimizer (see below).
    smode : string, if full_output is true
        Message describing the exit mode from the optimizer.

    See also
    --------
    minimize: Interface to minimization algorithms for multivariate
        functions. See the 'SLSQP' `method` in particular.

    Notes
    -----
    Exit modes are defined as follows ::

        -1 : Gradient evaluation required (g & a)
         0 : Optimization terminated successfully.
         1 : Function evaluation required (f & c)
         2 : More equality constraints than independent variables
         3 : More than 3*n iterations in LSQ subproblem
         4 : Inequality constraints incompatible
         5 : Singular matrix E in LSQ subproblem
         6 : Singular matrix C in LSQ subproblem
         7 : Rank-deficient equality constraint subproblem HFTI
         8 : Positive directional derivative for linesearch
         9 : Iteration limit exceeded

    Examples
    --------
    Examples are given :ref:`in the tutorial <tutorial-sqlsp>`.
    """

    [x, fun, nit, status, mes] = fmin_slsqp(funcaoEstratificacao, chuteInicial, iprint = d, full_output = 1)

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
    
    #--------------------------------------------------------------------------
    # testa a estratificação em duas camadas
    print 'Inciando teste de estratificacao em 2 camadas,'

    iniciaConstantes(debug = True)
     
    [p1, k, h] = estratifica2Camadas(debug = True)
    print 'valores,'
    print 'p1, ', p1
    print 'k, ', k
    print 'h, ', abs(h)
    print 'p2, ', p2solo2Camadas(p1, k)

    print '_'*80

    #--------------------------------------------------------------------------
    iniciaConstantes(0, debug = True)

    [p1, k, h] = estratifica2Camadas(debug = True)
    print 'valores,'
    print 'p1, ', p1
    print 'k, ', k
    print 'h, ', abs(h)
    print 'p2, ', p2solo2Camadas(p1, k)

    print '_'*80

    iniciaConstantes(1, debug = True)
    
    #--------------------------------------------------------------------------

    [p1, k, h] = estratifica2Camadas(debug = True)
    print 'valores,'
    print 'p1, ', p1
    print 'k, ', k
    print 'h, ', abs(h)
    print 'p2, ', p2solo2Camadas(p1, k)

    print '_'*80

    print 'testando individualmente a funcao de estratificacao'
    print 'saida, ', funcaoEstratificacao([364.67, -0.43, -2.827])

    print
    print '**fim'
    print '_'*80

    #--------------------------------------------------------------------------
    # testa a leitura da planilha com os dados
    print 'Iniciando teste leitura de uma planilha'
    m = lerPlanilha(planilha, debug = True)
    [prof, resi] = resistividadeMediaPlanilha(m, debug = True)
    print 'Retorno,'
    print prof
    print resi

    pho = prof
    es = resi

    plot(prof, resi)
    show()

    print 'estratificando o solo apartir dos valores da tabela'
    print 'OBS: este solo nao pode ser estratificado em duas camadas'

    [p1, k, h] = estratifica2Camadas(debug = True)
    print 'valores,'
    print 'p1, ', p1
    print 'k, ', k
    print 'h, ', abs(h)
    print 'p2, ', p2solo2Camadas(p1, k)  

    print
    print '**fim'
    print '_'*80

    #--------------------------------------------------------------------------
    resistividadeAparente2Camadas()

    saida = raw_input('[ENTER] para sair')
