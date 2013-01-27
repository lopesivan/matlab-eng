from glob import glob
from os import walk, getcwd, path, remove

dir_atual = '.'
formatos_simulacao = [".smv"]

print 'pasta atual:', getcwd()

lista = []
for root, dirs, files in walk(dir_atual):
    for f in files:
        for a in formatos_simulacao:
            if f.endswith(a):
                c = path.join(root, f)
                lista.append(c)

if len(lista) > 0:
    print 'arquivo(s) encontrado(s):'
    
    for q in lista:
        print q
        try:
            remove(q)
        except:
            print 'erro: nao foi possivel remover o arquivo,', q

    print 'arquivo(s) removido(s)'
    
else:
    print 'nada encontrado'

a = raw_input('[ENTER] para sair')

        
