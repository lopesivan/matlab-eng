# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
import r1haste
import rnhastes
#from pylab import arange, plot, show, xlabel, ylabel
from numpy import arange
import matplotlib.pyplot as plt
from tkFileDialog import askopenfilename
from Tkinter import Tk
import estratificacao
import configuracoes
import sys
import rnHorizontais
import rAnel

versao = '0.1'

#variaveis de controle do sistema
usaValoresArquivo = 1
debugAterramento = 0

def verificaVariaveisProfResi():
    global profundidade, resistividadeMedia
    try:
        if len(profundidade) > 0:
            if len(profundidade) == len(resistividadeMedia):
                return 0
            else:
                print 'erro: tamanho dos vetores de profundidade e resistividade nao sao os mesmos'
                return 2
        else:
            print 'erro: nada em profundidade'
            return 1
    except:
        print 'erro: impossivel ler profundidade'
        return 3
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

def entradaHastesQuadradoCheio():
    try:
        pa = input('resistividade do solo(ohm*m): ')
        l = input('comprimento da haste(m): ')
        d = input('diametro da haste(m): ')
        e = input('espacamento entre duas hastes(m): ')
        m = input('quantidade de hastes na linha')
        n = input('quantidade de hastes na coluna')
    except:
        print 'erro: entrada invalida, usando valores padroes'        
        pa = 100
        l = 2.4
        e = 2
        d = 0.0127
        m = 2
        n = 2

        print 'resistividade aparente do solo(ohm*m):', pa
        print 'comprimento da haste(m): ', l
        print 'espacamento entre os eletrodos(m): ', e
        print 'diametro da haste(m): ', d
        print 'na linha: ', m
        print 'na coluna: ', n

    return [m, n, e, pa, l, d]

def levantaCurvaK(pa, l, e, d, q, fim, passo):
    numeroHastes = arange(2, fim, passo)
    res = []
    for i in numeroHastes:
        res.append(rnhastes.resistenciaHastesLinha(pa, l, e, d, i))

    plt.plot(numeroHastes, res)
    plt.xlabel('Numero de Hastes')
    plt.ylabel('Resistencia')
    plt.show()
        
    
def curvaK():
    en = entradaHastesLinha()
    fim = input('quantidade final de hastes: ')
    passo = input('passo: ')

    levantaCurvaK(en[0], en[1], en[2], en[3], en[4], fim, passo)
    

def calculosResistividade(): 
    print '0 - calculo para 1 haste'
    print '1 - calculo para n hastes em paralelo(linha)'
    print '2 - quadrado cheio'
    print '3 - triangulo'
    print '4 - circunferencia'
    print '5 - anel'
    
    a = raw_input('>>>')
    
    if a == '0':
        en = entradaPhold()
        res = r1haste.r1haste(en[0], en[1], en[2])

    elif a == '1':
        en = entradaHastesLinha()
        res = rnhastes.resistenciaHastesLinha(en[0], en[1], en[2], en[3], en[4])

    elif a == '2':
        en = entradaHastesQuadradoCheio()
        res = rnhastes.quadradoCheio(en[0], en[1], en[2], en[3], en[4], en[5])

    else:
        print 'aviso: opcao nao disponivel'
        return 0

    print '_'*50
    print 'Resistencia calculada:', res

def planilhaExcel(p = None, debug = True):
    global profundidade, resistividadeMedia

    if p == None:
        try:
            mainTkinter = Tk()
            planilha = askopenfilename()
            mainTkinter.destroy()
            if debug:
                print planilha    
        except:
            planilha = None
            return
    else:
        planilha = p

    try:
        mDados = estratificacao.lerPlanilha(planilha)
    except:
        print 'aviso: nenhum arquivo'
        planilha = None
        return

    [profundidade, resistividadeMedia] = estratificacao.resistividadeMediaPlanilha(mDados)        

    if debug:
        print 'Valores disponiveis da tabela,'
        print mDados
        print 'profundidade | resisitividade media'
        for i in range(len(profundidade)):
            print profundidade[i], resistividadeMedia[i]

    print 'aviso: valores de profundidade e resistivdade foram atualizados'

def estratificacaoSolo():

    if verificaVariaveisProfResi():
        return

    print 'Iniciando a estratificacao do solo'

    estratificacao.pho = resistividadeMedia
    estratificacao.es = profundidade

    [p1, k, h] = estratificacao.estratifica2Camadas(debugAterramento)  
    p2 = estratificacao.p2solo2Camadas(p1, k)  
    print 'Resistividade da primeira camada(ohm*m), ', p1
    print 'Resisitivdade da segunda camada(ohm*m), ', p2
    print 'Coeficiente de reflexao, ', k
    print 'Profundidade da primeira camada(m), ', h

    pass

def lerCSV():
    pass

def ajudaBasica():
    print 'Lista de comandos disponiveis:'
    print 'h - ajuda'
    print 'o - sistema de calculos'
    print 's - extermina o programa'
    print 'c - inicia os calculos para sistema aterramento'
    print 'k - levanta a curva K de uma malha'
    print 'e - inicia o processo de estratificacao do solo'
    print 'a - ler uma planilha de dados'
    print 'q - ler um arquivo csv'
    print 'p - plota curva h-pho'
    print 'l - resistividade aparente'
    print 'n - mostra algumas equacoes'
    print 

def sistema(): 
    global usaValoresArquivo
    global profundidade
    global resistividadeMedia
    global debugAterramento 

    print 'Controle do sistema,'
    print 'Usa variaveis adquiridas apartir de um arquivo, @', usaValoresArquivo

    print 'Limites para a otimizacao,'
    print 'p1, ', estratificacao.limites[0]
    print 'k, ', estratificacao.limites[1]
    print 'h, ', estratificacao.limites[2]

    if raw_input('mostrar variaveis aterramento[s/N]?') == 's':
        try:
            if len(profundidade)>0 and len(resistividadeMedia):
                print 'profundidade | resisitividade media'
                for i in range(len(profundidade)):
                    print profundidade[i], resistividadeMedia[i]
        except:
            print 'aviso: nada para mostrar'
            print 'carregue um arquivo antes desta acao'

    if raw_input('carregar o arquivo de configuracao[s/N]?') == 's':
        try:
            print configuracoes.arquivoExcel
            planilhaExcel(configuracoes.arquivoExcel, debug = None)
        except:
            pass

    if debugAterramento == 0:
        if raw_input('ENTRAR no modo de debug[s/N]?') == 's':
            debugAterramento = 1
            print 'debug ativado'
    else:
        if raw_input('SAIR do modo de debug[s/N]?') == 's':
            debugAterramento = 0
            print 'debug desativado'

def plotPhoH():
    if verificaVariaveisProfResi():
        return
        
    plt.plot(profundidade, resistividadeMedia)
    plt.xlabel('Profundidade [m]')
    plt.ylabel('Resistividade Media [ohm*m]')
    plt.title('Curva de Resistividade')
    plt.grid(True)
    plt.show()
    plt.savefig('curvadeResistividade.pdf')

def mostraEquacoes():
    print 'r1 - apenas 1 haste disposta verticalmente no solo'
    print 'h - hastes dispostas horizontalmente no solo'

    tipo = raw_input('?')
    tipo = tipo.lower()

    if tipo == 'h':
        print '0 - condutor unico'
        print '1 - dois condutores em angulo reto'
        print '2 - estrela 3 pontas'
        print '3 - estrela 4 pontas'
        print '4 - estrela 6 pontas'
        print '5 - estrela 8 pontas'

        try:
            v = input('h?')
        except:
            print 'erro: entrada invalida'
            return

        rnHorizontais.mostraEquacao(v)

    elif tipo == 'r1':
        r1haste.mostraEquacao()


def exterminaPrograma(): 
    print 'saindo...'
    exit()

def nada():
    print 'aviso: comando nao reconhecido!'

dicionarioComandos = {  'h' : ajudaBasica,
                        'ajuda' : ajudaBasica,

                        'o' : sistema, 
                        'sistema' : sistema,

                        's' : exterminaPrograma, 
                        'sair' :  exterminaPrograma, 

                        'c' : calculosResistividade,
                        'resistividade' : calculosResistividade,

                        'k' : curvaK,
                        'curvak' : curvaK,

                        'e' : estratificacaoSolo,
                        'estratificacao' : estratificacaoSolo,

                        'a' : planilhaExcel,
                        'excel' : planilhaExcel,

                        'q' : lerCSV, 
                        'csv' : lerCSV,

                        'p' : plotPhoH,
                        'ploth' : plotPhoH,

                        'n' : mostraEquacoes, 
                        'equacoes' : mostraEquacoes

                    }

# interpreta os comandos do usuário
def cmds(cmd): 
    return dicionarioComandos.get(cmd, nada)()

def inicializacao():
    print 'aviso: carregando arquivo de configuracao'
    try:
        print configuracoes.arquivoExcel
        planilhaExcel(configuracoes.arquivoExcel, debug = None)
    except:
        print 'erro: nao foi possivel iniciar pelo arquivo de configuracao'
        pass 
    print 'aviso: inicializacao finalizada'

if __name__ == '__main__':

    print 'Calculos para sistemas de aterramento , v.', versao
    print 'Felipe Bandeira, junho/2013, Fortaleza-CE'
    print '.'*80
    print 'digite "ajuda" para mais informacoes'

    inicializacao()

    #ajudaBasica()

    while True:
        entrada = raw_input('>')
        # converte tudo para letras minúsculas e inicia a interpretacao
        cmds(entrada.lower())
        
