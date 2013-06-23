from scipy.optimize import fmin, fmin_bfgs
from math import sqrt

infinito = 10 # :)
pho = [320, 245, 182, 162, 168, 152]
es = [2.5, 5, 7.5, 10, 12.5, 15]
numeroMaximoFuncoes = 1e6
chuteInicial = [0, 0, 0]

def funcaoEstratificacao(x):
    '''
    entrada:
    x[0] = p1
    x[1]= k
    x[2] = h
    '''
    f = 0
    for i in range(len(es)):
        s1 = 0
        for n in range(1, infinito+1):
            s1 = s1 + ((x[1]**n)/sqrt(1+(2*n*x[2]/es[i])**2) - (x[1]**n)/sqrt(4+(2*n*x[2]/es[i])**2))

        f = f + (pho[i]-x[0]*(4*s1+1))**2

    return f

print fmin(funcaoEstratificacao, chuteInicial, maxfun = numeroMaximoFuncoes)
            
    
