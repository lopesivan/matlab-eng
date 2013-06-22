import r1haste

print 'Calculos para sistemas de aterramento'
print 'Felipe Bandeira, 22/06/2013'

def ajuda():
    print 'aviso: nada implementado'

def entradaPhold():
    pa = input('resistividade(ohm*m): ')
    l = input('comprimento(m): ')
    d = input('diametro da haste(m): ')
    return [pa, l, d]

def calculosResistividade():
    
    print '[0] - calculo para 1 haste'
    print '[1] - calculo para 2 hastes'
    print '[3] - calculo para n hastes'
    
    a = raw_input('>')

    if a == '0':
        entrada = entradaPhold()
        res = r1haste.r1haste(entrada[0], entrada[1], entrada[2])
        print 'resistencia:', res
        
    else:
        return
    
if __name__ == '__main__':
    while True:
        cmd = raw_input('>>')

        if cmd == 'h':
            ajuda()
        elif cmd == 's':
            exit()
        elif cmd == 'c':
            calculosResistividade()
        else:
            pass

    
        
