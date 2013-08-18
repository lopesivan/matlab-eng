#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

import os
import sys
import csv
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from numpy import arange, copy, mean

def zpDir(dir, nivelRecursao = 50, ddir = None, debug = 0):
    """ Calcula a impedancia para cada arquivo csv
    Busca recursiva dos arquivos
    """

    idArquivoCSV = 'csv'

    qArquivos = 0

    arquivos = []

    if debug:
        #print 'atual', dir, '...'
        pass
    try:
        nomes = os.listdir(dir)
    except os.error:
        print 'erro: nao foi possivel listar', dir
        nomes = []

    nomes.sort()
    sucesso = 1
    for nome in nomes:
        nomeCompleto = os.path.join(dir, nome)
        if ddir is not None:
            dfile = os.path.join(ddir, nome)
        else:
            dfile = None
        if not os.path.isdir(nomeCompleto):

            if nomeCompleto[-3:].lower() == idArquivoCSV:
                arquivos.append(nomeCompleto)
                qArquivos += 1

            if qArquivos == 2:
                #for i in arquivos:
                    #int(i[-5:-4])
                #with open(i, 'rb') as f:
                #    cf = csv.reader(f)

                if debug:
                    print '*'*80
                    print 'arquivos <csv> no diretorio atual'
                    print arquivos
                    print

                zpArquivo(arquivos, plot = 0)

            elif qArquivos > 2 and debug:
                print 'erro: mais de um arquivo <csv> no diretorio'
                print arquivos

            sucesso = 0

        elif nivelRecursao > 0  and \
            nome != os.curdir and nome != os.pardir and \
            os.path.isdir(nomeCompleto) and \
            not os.path.islink(nomeCompleto):

            if not zpDir(nomeCompleto, nivelRecursao-1, dfile, debug):
                sucesso = 0

    return sucesso


def zpArquivo(arq, plot = 0):
    tensao = csv.reader(open(arq[0], 'rb'))
    corrente = csv.reader(open(arq[1], 'rb'))

    t = []
    v = []
    c = []

    for i in tensao:
        t.append(float(i[0]))
        v.append(float(i[1]))
    for i in corrente:
        c.append(float(i[1]))

    t = copy(t)
    v = copy(v)
    c = copy(c)

    if t[0] < 0:
        t = t-t[0]

    fs = 1/(t[1]-t[0])
    fc = 100e3

    [B, A] = butter(2, fc/(fs/2))

    v2 = lfilter(B, A, v)
    i2 = lfilter(B, A, c)

    z = v2/i2
    zEstabilizado = v2[len(t)/2:]/i2[len(t)/2:]

    rTerra = mean(zEstabilizado)

    print 'resistencia [ohm], ', rTerra
    #print t

    #plt.plot(t, v)
    #plt.plot(t[len(t)/2:], v2[len(t)/2:])
    #plt.plot(t, v2, t, i2)

    if plot == 1 or rTerra < 0:
        plt.subplot(311)
        plt.ylabel('tensao')
        plt.plot(t, v2)

        plt.grid(True)

        plt.subplot(312)
        plt.ylabel('corrente')
        plt.plot(t, i2)

        plt.grid(True)

        plt.subplot(313)
        plt.ylabel('z = v/i')
        plt.plot(t, z)

        plt.xlabel('tempo(s)')

        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    print 'Impedancia Impulsiva'
    zpDir('.', debug = 1)
