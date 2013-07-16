# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
import r1haste
import rnhastes
#from pylab import arange, plot, show, xlabel, ylabel
from numpy import arange, linspace
import matplotlib.pyplot as plt
from tkFileDialog import askopenfilename
from Tkinter import Tk
import estratificacao
import configuracoes
import sys
import rnHorizontais
import rAnel
import potenciais
from os import getcwd, mkdir, system
from os.path import basename, splitext
from time import localtime
import malhaAterramento
from sympy import pprint, symbols, Sum
from scipy.interpolate import UnivariateSpline

versao = '0.1'

#variaveis de controle do sistema
usaValoresArquivo = 1
debugAterramento = 0

# identificação do arquivo do excel ou arquivo qualquer, usado na criação de 
# arquivos com plot ou no armazenamento de variaveis
idPlanilha = ''

# diretorio para armazenamento das curvas
dirCurvas = getcwd()+'\\curvas'

def formataHora():
    t = localtime()
    return str(t.tm_hour)+str(t.tm_min)+str(t.tm_sec)

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
        print u'erro: entrada invalida, usando valores padrões'
        
        pa = 100    #resistividade aparente do solo
        l = 2.4     #comprimento da haste
        e = 3       #espacamento entre os eletrodos
        d = 0.0127  #diametro da haste
        q = 8       #quantidade de hastes

        print u'resistividade aparente do solo(ohm*m):', pa
        print u'comprimento da haste(m): ', l
        print u'espaçamento entre os eletrodos(m): ', e
        print u'diametro da haste(m): ', d
        print u'quantidade de hastes: ', q

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
        print u'erro: entrada invalida, usando valores padrões'        
        pa = 100
        l = 2.4
        e = 2
        d = 0.0127
        m = 2
        n = 2

        print u'resistividade aparente do solo(ohm*m):', pa
        print u'comprimento da haste(m): ', l
        print u'espaçamento entre os eletrodos(m): ', e
        print u'diâmetro da haste(m): ', d
        print u'na linha: ', m
        print u'na coluna: ', n

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
    print u'0 - cálculo para 1 haste'
    print u'1 - cálculo para n hastes em paralelo(linha)'
    print u'2 - quadrado cheio'
    print u'3 - triângulo'
    print u'4 - circunfêrencia'
    print u'5 - anel'
    
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
        print u'aviso: opção não disponivel'
        return 0

    print '_'*50
    print u'Resistência calculada:', res

def atualizaIdArquivo(nome = '', tipo = 'excel'):
    global idPlanilha

    if tipo == 'excel':

        idPlanilha = basename(nome)
        idPlanilha = splitext(idPlanilha)[0]
        print u'identificação atualizada, e, ', 
        print idPlanilha

    elif tipo == 'arquivo':

        idPlanilha = nome
        print u'identificação atualizada, a, ', 
        print idPlanilha

    else:

        print 'aviso: id limpo'
        idPlanilha = ''

def planilhaExcel(p = None, debug = True):
    global profundidade, resistividadeMedia

    if p == None:
        try:
            mainTkinter = Tk()
            planilha = askopenfilename()
            mainTkinter.destroy()

            if len(planilha) > 0:
                atualizaIdArquivo(planilha, tipo = 'excel')
            else:
                print u'Parabêns, é sempre bom selecionar um arquivo'
                print 'aviso: nada atualizado'
                return 1

            if debug:
                print planilha    
        except:
            atualizaIdArquivo('', tipo = 'erro')
            planilha = None
            print 'erro: na planilha'
            return 1
    else:
        planilha = p
        try:
            a = open(planilha, 'rb')
        except:
            print u'erro: planilha não encontrada'
            return 
            atualizaIdArquivo(planilha, tipo = 'excel')
        atualizaIdArquivo(planilha, tipo = 'arquivo')
        
    #atualizaIdArquivo(planilha)

    try:
        mDados = estratificacao.lerPlanilha(planilha)
    except:
        print 'aviso: nenhum arquivo'
        planilha = None
        return 2

    [profundidade, resistividadeMedia] = estratificacao.resistividadeMediaPlanilha(mDados)        

    if debug:
        print 'Valores disponiveis da tabela,'
        print mDados
        print u'profundidade | resisitividade média'
        for i in range(len(profundidade)):
            print profundidade[i], resistividadeMedia[i]

    print 'aviso: valores de profundidade e resistividade foram atualizados'

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
    print
    print u'Lista de comandos disponiveis:'
    print u'h = ajuda'
    print u'o = sistema de calculos'
    print u's = extermina o programa'
    print u'c = inicia os calculos para sistema aterramento'
    print u'k = levanta a curva K de uma malha'
    print u'e = inicia o processo de estratificação do solo'
    print u'a = ler uma planilha de dados'
    #print u'q = ler um arquivo csv'
    print u'p = plota curva h-pho'
    print u'l = resistividade aparente'
    print u'n = mostra algumas equações'
    print u'm = abre arquivo de configuracão para projeto de malha'

def ajudaCompleta():
    limpaTela()

    print u"""pyAterramento

    """

    print 

def sistema(): 
    global usaValoresArquivo
    global profundidade
    global resistividadeMedia
    global debugAterramento 

    print u'Controle do sistema,'
    print u'Usa variáveis adquiridas apartir de um arquivo, @', usaValoresArquivo

    print u'Limites para a otimização,'
    print 'p1, ', estratificacao.limites[0]
    print 'k, ', estratificacao.limites[1]
    print 'h, ', estratificacao.limites[2]

    print u'mostrar variáveis aterramento[s/N]?',
    if raw_input() == 's':
        try:
            if len(profundidade)>0 and len(resistividadeMedia):
                print 'profundidade | resisitividade media'
                for i in range(len(profundidade)):
                    print profundidade[i], resistividadeMedia[i]
        except:
            print 'aviso: nada para mostrar'
            print 'carregue um arquivo antes desta acao'

    print u'carregar o arquivo de configuracao[s/N]?',
    if raw_input() == 's':
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
        
    #plt.subplot(211)
    plt.plot(profundidade, resistividadeMedia)
    plt.xlabel('Profundidade [m]')
    plt.ylabel('Resistividade Media [ohm*m]')
    plt.title('Curva de Resistividade')
    plt.grid(True)


    plt.savefig(dirCurvas+'\\curvadeResistividade_'+idPlanilha+'_'+formataHora()+'_.png')
    print 'aviso: arquivo png da figura salvo na pasta <curvas>'
    
    #plt.show()
    #s = UnivariateSpline(profundidade, resistividadeMedia, s=1)
    #xs = linspace(0, profundidade[len(profundidade)-1], 1000)
    #ys = s(xs)
    #plt.subplot(212)
    #plt.plot(xs, ys)

    plt.show()
    

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

def projetoMalha():

    try:
        mainTkinter = Tk()
        arquivo = askopenfilename()
        mainTkinter.destroy()  
        print 'usando,'
        print arquivo
    except:
        print 'erro:'
        return 

    malhaAterramento.lerArquivoProjeto(arquivo)
    malhaAterramento.mostraDadosProjeto()
    malhaAterramento.projetaMalhaAterramento(debug = True)

def exterminaPrograma(): 
    print 'saindo...'
    exit()

def nada():
    print 'aviso: comando nao reconhecido!'

dicionarioComandos = {  
    'h' : ajudaBasica,
    'ajuda' : ajudaCompleta,

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
    'equacoes' : mostraEquacoes,

    'm' : projetoMalha,
    'malha' : projetoMalha
}

# interpreta os comandos do usuário
def cmds(cmd): 
    return dicionarioComandos.get(cmd, nada)()

def inicializacao():
    print 'aviso: carregando arquivo de configuracao'
    try:
        
        if planilhaExcel(configuracoes.arquivoExcel, debug = None) == 0:
            print configuracoes.arquivoExcel

    except Exception, e:
        print 'erro: nao foi possivel iniciar pelo arquivo de configuracao'
        print e
    try:
        mkdir(dirCurvas)
    except Exception, e:
        print 'erro: nao foi possivel criar diretorio para as curvas, talvez ele ja exista'
    else:
        pass
    finally:
        pass

    print 'aviso: inicializacao finalizada'

def artMain():
    m, u, ln, oo, k0, c0, km1, km2, km3, cm1, cm2, cm3, d0, a, N= symbols('m, u, ln, oo, k0, c0, km1, km2, km3, cm1, cm2, cm3, d0, a, N')
    f = 1 + Sum((u**m*(km1/cm1 + (2*km2)/cm2 + km3/cm3))/(ln(16*a/d0) + k0/c0),(m, 1, oo))
    pprint(f)

def limpaTela():
    return system('cls')

def mensagemInicial():
    print 'Calculos para sistemas de aterramento , v.', versao
    print 'Felipe Bandeira, junho/2013, Fortaleza-CE'
    print
    print 'digite "ajuda" para mais informacoes'
    print 

if __name__ == '__main__':

    limpaTela()
    mensagemInicial()
    inicializacao()
    ajudaBasica()

    if configuracoes.limpaTelaInicializacao == 1:
        limpaTela()
    else:
        print

    while True:
        entrada = raw_input(configuracoes.textoPrompt)
        # converte tudo para letras minúsculas e inicia a interpretação
        cmds(entrada.lower())
        
