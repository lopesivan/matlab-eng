# -*- coding: cp1252 -*-
# Felipe Bandeira, 27/01/2013. Fortaleza-CE

from glob import glob
from os import walk, getcwd, path, remove

dir_atual = '.'
formatos_simulacao = [".smv"]

print 'pasta atual:', getcwd()

lista = []

# Inicia a busca por um arquivo na pasta atual, finalizando quando
# pecorre todos os arquivos e sub pastas
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

    apaga = raw_input('apagar o(s) arquivo(s) [S/n]?')
    if apaga == 's' or apaga == '':
        for q in lista:
            try:
                remove(q)
                print q, ' --> deletado'
            except:
                print 'erro: nao foi possivel deletar, ', q
    else:
        print 'aviso: nenhum arquivo deletado'
else:
    print 'aviso: nada encontrado'

a = raw_input('[ENTER] para sair')

        
