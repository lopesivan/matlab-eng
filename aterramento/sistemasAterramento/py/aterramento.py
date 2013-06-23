# -*- coding: cp1252 -*-
import r1haste
import rnhastes
from pylab import arange, plot, show

def entradaPhold():
    try:
        pa = input('resistividade do solo(ohm*m): ')
        l = input('comprimento da haste(m): ')
        d = input('diametro da haste(m): ')
    except:
        print 'erro: entrada invalida, usando valores padroes'
        pa = 100
        l = 2.4
        d = 15e-3
        print 'pa: ', pa
        print 'l: ', l
        print 'd: ', d
        
    return [pa, l, d]

def entradaHastesLinha():
    try:
        pa = input('resistividade do solo(ohm*m): ')
        l = input('comprimento da haste(m): ')
        d = input('diametro da haste(m): ')
        e = input('espacamento entre duas hastes(m): ')
        q = input('quantidade de hastes: ')
    
    except:
        print 'erro: entrada invalida, usando valores padroes'
        
        pa = 100    #resistividade aparente do solo
        l = 2.4     #comprimento da haste
        e = 3       #espacamento entre os eletrodos
        d = 0.0127  #diametro da haste
        q = 8       #quantidade de hastes

        print 'resistividade aparente do solo(ohm*m):', pa
        print 'comprimento da haste(m): ', l
        print 'espacamento entre os eletrodos(m): ', e
        print 'diametro da haste(m): ', d
        print 'quantidade de hastes: ', q

    return [pa, l, e, d, q]

def levantaCurvaK(pa, l, e, d, q, fim, passo):
    numeroHastes = arange(2, fim, passo)
    res = []
    for i in numeroHastes:
        res.append(rnhastes.resistenciaHastesLinha(pa, l, e, d, i))

    plot(numeroHastes, res)
    show()
        
    
def curvaK():
    en = entradaHastesLinha()
    fim = input('quantidade final de hastes: ')
    passo = input('passo: ')

    levantaCurvaK(en[0], en[1], en[2], en[3], en[4], fim, passo)
    

def calculosResistividade():
    
    print '[0] - calculo para 1 haste'
    print '[1] - calculo para n hastes'
    
    a = raw_input('>>>')
    
    if a == '0':
        en = entradaPhold()
        res = r1haste.r1haste(en[0], en[1], en[2])

    elif a == '1':
        en = entradaHastesLinha()
        res = rnhastes.resistenciaHastesLinha(en[0], en[1], en[2], en[3], en[4])
            
    else:
        print 'aviso: opcao nao disponivel'
        return 0

    print '_'*50
    print 'resistencia calculada:', res

def ajudaBasica():
    print 'lista de comandos disponiveis:'
    print 'h - ajuda'
    print 's - extermina o programa'
    print 'c - inicia os calculos para sistema aterramento'
    print 'k - levanta a curva K de uma malha'
    print 'e - inicia o processo de estratificacao solo'
    print 
    
if __name__ == '__main__':

    print 'Calculos para sistemas de aterramento'
    print 'Felipe Bandeira, 22/06/2013'
    print 

    ajudaBasica()

    while True:
        cmd = raw_input('>>')

        if cmd == 'h':
            ajudaBasica()
        elif cmd == 's':
            exit()
        elif cmd == 'c':
            calculosResistividade()
        elif cmd == 'k':
            curvaK()
        else:
            pass        
