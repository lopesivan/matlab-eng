# -*- coding: utf-8 -*-

from __future__ import division
import r1haste
from math import sqrt, pi, log
from numpy import zeros

def resistenciaMutua(pa, l, e):
    bhm = sqrt(l**2 + e**2)
    #print bhm
    return pa/(4*pi*l) * log(((bhm+l)**2 - e**2)/(e**2 - (bhm-l)**2))

def resistenciaHastesLinha(pa, l, e, d, q):
    '''
    Hastes colocadas no solo em linha reta
    entrada:
    pa - resistividade do solo
    l - comprimento das hastes
    e - espacamento unico entre duas hastes
    d - diamentro da haste
    q - quantidade
    '''
    
    rh = [[0 for i in range(q)] for j in range(q)]        

    for j in range(q):
        for i in range(q):
            if j!=i:
                #distancia absoluta entre os pontos
                dhm = abs(i-j)
                rh[j][i] = resistenciaMutua(pa, l, dhm*e)
            else:
                rh[j][i] = r1haste.r1haste(pa, l, d)

    # mostra a matriz gerada
    '''
    for j in range(q):
        for i in range(q):
            print rh[j][i],
        print
    '''
    
    acumulador1 = 0
    acumulador2 = 0
    for j in range(q):
        for i in range(q):
            acumulador1 = acumulador1 + rh[j][i]
        acumulador2 = acumulador2 + 1/acumulador1
        acumulador1 = 0
                
    resitenciaEquivalente = 1/acumulador2

    #print 'resistencia: ', resitenciaEquivalente

    return resitenciaEquivalente

def quadradoCheio(m, n, esp, pa, l, d, debug = None):
    '''
    entrada,
    m - quantidade de hastes colocadas em linha
    n - quantidade de hastes colocas em coluna
    esp - espaÃ§amento entre duas hastes
    p - restividade aparente
    l - comprimento da haste
    d - diametro da haste
    '''
    r = zeros(shape = (m, n))
    r1 = r1haste.r1haste(pa, l, d)
    
    if debug:
        print r1

    for i in range(1, m+1):
        for j in range(1, n+1):
            for x in range(1, m+1):
                for y in range(1, n+1):
                    if (i==x) and (j==y):
                        r[i-1, j-1] = r[i-1, j-1]+r1
                        
                        if debug:
                            print r
                    else:
                        e = sqrt((i-x)**2+(j-y)**2)*esp
                        b = sqrt(l**2+e**2)
                        a = resistenciaMutua(pa, l, e)
                        r[i-1, j-1] = r[i-1, j-1]+a

    if debug:
        print r

    Ra = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            Ra = Ra + 1/r[i-1, j-1]

    return 1/Ra

if __name__ == '__main__':

    pa = 100    #resistividade aparente do solo
    l = 2.4     #comprimento da haste
    e = 3       #espacamento entre os eletrodos
    d = 0.0127  #diametro da haste
    q = 8       #quantidade de hastes

    print resistenciaHastesLinha(pa, l, e, d, q)
    print quadradoCheio(2, 2, 2, pa, l, d, debug = True)
    #saida = raw_input('ENTER] para sair')
