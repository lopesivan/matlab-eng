# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division

print 'iniciando...'

import sys
import random
import hashlib
import getpass
import subprocess
import argparse
import codecs
#sys.stdout = codecs.getwriter('cp860')(sys.stdout)
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

from os import getcwd, mkdir, system
from os.path import basename, splitext
from os.path import isdir, isfile

from time import localtime, time
import ConfigParser
from getpass import getuser
from uuid import getnode as get_mac
from math import exp, sqrt

from numpy import arange, linspace
#from sympy import pprint, symbols, Sum
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

from tkFileDialog import askopenfilename
from Tkinter import Tk

from IPython import embed
from platform import system as os

#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----
# MINHAS BIBLIOTECAS
#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----
import estratificacao
import r1haste
import rnhastes
import rnHorizontais
import malhaAterramento
import rAnel
import potenciais
import relatorioEstratificacao

import ajudante
#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----#----

################################################################################################
versao = '0.1'
################################################################################################

# Sal para o login
SAL = 'validade12'

################################################################################################
# GLOBAIS

# Qual sistema eu estou usando?
#if os() == 'Linux':
#    separador = '/'
#    cmdLimpaTela = 'clear'
#else:
#    separador = '\\'    # para o Windows
#    cmdLimpaTela = 'cls'

# identificação do arquivo do excel ou arquivo qualquer, usado na criação de 
# arquivos com plot ou no armazenamento de variaveis
idPlanilha = ''
# diretório para armazenamento das curvas
ndirCurvas = 'curvas'
dirCurvas = getcwd()+ajudante.separador()+ndirCurvas
# diretório para armazenamento dos resultados
ndirResultados = 'resultados'
dirResultados = getcwd()+ajudante.separador()+ndirResultados

# Dicionário com todas as principais variáveis de controle do sistema
sistemaVar = {
    # se 0 a entrada para o diâmetro da haste é dada em m
    # se 1 a entrada para o diâmetro da haste é dada em mm
    # se 2 a entrada para o diâmetro da haste é dada em polegas
    'unidadeHaste' : 'pol',

    'usaValoresArquivo' : 1,
    'debugAterramento' : 0, 
    'idPlanilha' : '',
    'arqMalha' : '',
    'arqTabela' : '',
    'prompt' : ']',
    'limpaTelaInicial' : 'nao',
    'debugAterramento' : 'nao',

    'p1LimSuperior' : 1000,
    'p1LimInferior' : 0.1,

    'kLimSuperior' : 1,
    'kLimInferior' : -1,

    'h1LimSuperior' : 100,
    'h1LimInferior' : 0.1
}

sistemaResultados = {
    'fEstratificacao' : 0,
    'p1' : 0,
    'p2' : 0,
    'k' : 0, 
    'h' : 0
}

nomeArquivoConfiguracao = 'configuracoes.cfg'
nomeRelatorioEstratificacao = 'relatorio_estratificacao.tex'
alteracoes = 0

profundidade = 0
resistividadeMedia = 0

dicRelatorioEstratificacaoLatex = {
    'nomeAutor' : 'Felipe',
    'sobreNomeAutor' : 'Bandeira',
    'instituicao' :  'LAMOTRIZ - UFC',
}

################################################################################################

def hal9000():
    random.seed(time())
    n = random.randint(0, 9)
    if  n == 0:
        print """
        "I'm sorry, Dave. I'm afraid I can't do that."

                                                HAL 9000
        """
        #print "I'm sorry,"+getuser()+". I'm afraid I can't do that."
        espera = raw_input()
        limpaTela() 
               
    elif n == 1:
        print """
        Dave: Hello, HAL. Do you read me, HAL? 
        HAL : Affirmative, Dave. I read you. 
        Dave: Open the pod bay doors, HAL. 
        HAL : I'm sorry, Dave. I'm afraid I can't do that. 
        Dave: What's the problem? 
        HAL : I think you know what the problem is just 
              as well as I do. 
        Dave: What are you talking about, HAL? 
        HAL : This mission is too important for me to allow 
              you to jeopardize it. 
        Dave: I don't know what you're talking about, HAL. 
        HAL : I know that you and Frank were planning to 
              disconnect me, and I'm afraid that's something 
              I cannot allow to happen. 
        Dave: Where the hell'd you get that idea, HAL? 
        HAL : Dave, although you took very thorough precautions 
              in the pod against my hearing you, I could see your lips move. 
        Dave: Alright, HAL. I'll go in through the emergency airlock. 
        HAL : Without your space helmet, Dave, you're going 
              to find that rather difficult. 
        Dave: HAL, I won't argue with you anymore. Open the doors. 
        HAL : Dave, this conversation can serve no purpose anymore. Goodbye
        """
        espera = raw_input()
        limpaTela()  
    elif n == 2:
        print "I'm sorry, "+getuser()+". I'm afraid I can't do that."
        espera = raw_input()
        limpaTela()  

    else:
        print u'erro: comando não encontrado'

def formataHora():
    t = localtime()
    return str(t.tm_hour)+str(t.tm_min)+str(t.tm_sec)

def lerDRHaste(msg = 'diametro da haste'):
    """Ler o diâmetro ou raio da haste com o cuidado com as unidades.
    entrada:
    msg - mensagem a ser mostrada
    """

    x = sistemaVar['unidadeHaste']

    if x == 'm':
        print msg+'(m): ',
        return input()
    elif x == 'mm':
        print msg+'(mm):',
        return input()
    elif x == 'pol':
        print msg+'(pol): ',
        return input()
    else:
        return -1

def fDebug():
    if sistemaVar['debugAterramento'] == 'sim':
        return 1
    else:
        return 0

def verificaVariaveisProfResi(silencioso = 0):
    global profundidade, resistividadeMedia
    try:
        if len(profundidade) > 0:
            if len(profundidade) == len(resistividadeMedia):
                return 0
            else:
                if not silencioso:
                    print 'erro: tamanho dos vetores de profundidade e resistividade nao sao os mesmos'
                return 2
        else:
            if not silencioso:
                print 'erro: nada em profundidade'
            return 1
    except:
        if not silencioso:
            print 'erro: impossivel ler profundidade'
        return 3

def entradaPhold():
    try:
        pa = input('resistividade do solo(ohm*m): ')
        l = input('comprimento da haste(m): ')
        d = lerDRHaste()
        if d == -1:
            raise Exception()
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

        d = lerDRHaste()
        if d == -1:
            raise Exception()

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

        d = lerDRHaste()
        if d == -1:
            raise Exception()

        e = input('espacamento entre duas hastes(m): ')
        m = input('quantidade de hastes colocadas horizontalmente')
        n = input('quantidade de hastes colocadas verticalmente')
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
        print u'horizontais: ', m
        print u'verticais: ', n

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
    
    a = raw_input(']]')
    
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

# def atualizaIdArquivo(nome = '', tipo = 'excel'):
#     global idPlanilha

#     if tipo == 'excel':

#         idPlanilha = basename(nome)
#         idPlanilha = splitext(idPlanilha)[0]
#         print u'identificação atualizada, e, ', 
#         print idPlanilha

#     elif tipo == 'arquivo':

#         idPlanilha = nome
#         print u'identificação atualizada, a, ', 
#         print idPlanilha

#     else:

#         print 'aviso: id limpo'
#         idPlanilha = ''

# def planilhaExcel(p = None, debug = True):
#     global profundidade, resistividadeMedia

#     if p == None:
#         try:
#             mainTkinter = Tk()
#             planilha = askopenfilename()
#             mainTkinter.destroy()

#             if len(planilha) > 0:
#                 atualizaIdArquivo(planilha, tipo = 'excel')
#             else:
#                 print u'Parabêns, é sempre bom selecionar um arquivo'
#                 print 'aviso: nada atualizado'
#                 return 1

#             if debug:
#                 print planilha    
#         except:
#             atualizaIdArquivo('', tipo = 'erro')
#             planilha = None
#             print 'erro: na planilha'
#             return 1
#     else:
#         planilha = p
#         try:
#             a = open(planilha, 'rb')
#         except:
#             print u'erro: planilha não encontrada'
#             return 
#             atualizaIdArquivo(planilha, tipo = 'excel')
#         atualizaIdArquivo(planilha, tipo = 'arquivo')
        
#     #atualizaIdArquivo(planilha)

#     try:
#         mDados = estratificacao.lerPlanilha(planilha)
#     except:
#         print 'aviso: nenhum arquivo'
#         planilha = None
#         return 2

#     [profundidade, resistividadeMedia] = estratificacao.resistividadeMediaPlanilha(mDados, debug = fDebug())        

#     if debug:
#         print 'Valores disponiveis da tabela,'
#         print mDados
#         print u'profundidade | resisitividade média'
#         for i in range(len(profundidade)):
#             print profundidade[i], resistividadeMedia[i]

#     print 'aviso: valores de profundidade e resistividade foram atualizados'

def lerTabelaExcel(silencioso = 0):
    global profundidade, resistividadeMedia

    a = 0
    if isfile(sistemaVar['arqTabela']) and len(sistemaVar['arqTabela']) > 0:
        print u'usar o último arquivo[S/n]?',
        if raw_input() == 'n': 
            a = 1
    else:
        a = 1

    if a == 1:      
        try:
            mainTkinter = Tk()
            sistemaVar['arqTabela'] = askopenfilename()
            mainTkinter.destroy() 
            if len(sistemaVar['arqTabela']) > 0:
                if not silencioso:
                    print 'usando,'
                    print sistemaVar['arqTabela']
                atualizaArquivoConf()
            else:
                print u'erro: erro na seleção do arquivo'
                return -1
        except:
            print u'erro: no arquivo do excel'
            return -2


    try:
        mDados = estratificacao.lerPlanilha(sistemaVar['arqTabela'])
    except:
        print u'erro: não foi possível ler o arquivo do excel'
        return -3

    [profundidade, resistividadeMedia] = estratificacao.resistividadeMediaPlanilha(mDados, debug = fDebug())        
    sistemaResultados['fEstratificacao'] = 0
    if not silencioso:
        print 'Valores disponiveis da tabela,'
        print mDados
        print u'profundidade | resisitividade média'
        for i in range(len(profundidade)):
            print profundidade[i], resistividadeMedia[i]

    if not silencioso:
        print 'aviso: valores de profundidade e resistividade foram atualizados'

    return 0

def estratificacaoSolo(silencioso = 0):
    global sistemaResultados

    if verificaVariaveisProfResi():
        return -1

    if not silencioso:
        print u'Iniciando a estratificação do solo'

    estratificacao.pho = resistividadeMedia
    estratificacao.es = profundidade

    if sistemaResultados['fEstratificacao'] == 0:
        [p1, k, h] = estratificacao.estratifica2Camadas()  
        p2 = estratificacao.p2solo2Camadas(p1, k)  

        sistemaResultados['p1'] = p1
        sistemaResultados['p2'] = p2    
        sistemaResultados['k'] = k
        sistemaResultados['h'] = h

        sistemaResultados['fEstratificacao'] = 1

    if not silencioso:
        print 'Resistividade da primeira camada(ohm*m), ', sistemaResultados['p1']
        print 'Resisitivdade da segunda camada(ohm*m), ', sistemaResultados['p2']
        print 'Coeficiente de reflexao, ', sistemaResultados['k']
        print 'Profundidade da primeira camada(m), ', sistemaResultados['h']

    return [sistemaResultados['p1'], sistemaResultados['k'], sistemaResultados['h']]

def ajudaBasica():

    print u"""
Lista de comandos disponíveis

    h, ajuda            exibe ajuda básica
    o, sistema          configura o sistema de cálculos
    s, sair             finaliza o programa
    c, topologias       cálcula a resistência de uma topologia 
                        específica de aterramento. 
    k, curvak           levanta a curva K
    e, estratificacao   inicia o processo de estratificação do solo
    a, excel            ler uma planilha(excel) de dados
    p, plothp           plota curva h-pho
    pt                  plota a curva teorica e a medida em campo
    l, aparente         resistividade aparente 
    n, equacoes         mostra algumas equações
    m, malha            abre um arquivo para o projeto de malha

    lerconf             ler o arquivo de configuração
    cls                 limpa a terminal

    dados               mostra as variaveis principais utilizada nos calculos
    relatorio           inicia a geração de um relatório
    ver relatorio       ver o relatorio gerado

    ipython             chama o console do Ipython, interação mais elaborada
    """

def ajudaCompleta():
    #limpaTela()

    ajudaBasica()   

def sistema(): 
    global profundidade
    global resistividadeMedia
    global sistemaVar
    global alteracoes

    print u'Controle do sistema,'
    print u'Usa variáveis adquiridas apartir de um arquivo, @', sistemaVar['usaValoresArquivo']

    print u'Limites para a otimização,'
    print 'p1, ', estratificacao.limites[0]
    print 'k, ', estratificacao.limites[1]
    print 'h, ', estratificacao.limites[2]

    print u'alterar os limites para a otimização em duas camadas[s/N]?',
    if raw_input() == 's':
        if alteraLimitesOtimizacao() == -1:
            return -1

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
            lerArquivoConfiguracao()
            print u'aviso: arquivo de configuração lido com sucesso'
        except:
            print u'erro: não foi possível carregar o arquivo de configuração'

    if sistemaVar['limpaTelaInicial'] == 'nao':
        print u'Limpar a tela no inicio do programa[s/N]?',
        if raw_input() == 's':
            alteracoes += 1
            sistemaVar['limpaTelaInicial'] = 'sim'
    else:
        print u'NÃO limpar a tela no inicio do programa[s/N]?',
        if raw_input() == 's':
            alteracoes += 1
            sistemaVar['limpaTelaInicial'] = 'nao'

    if sistemaVar['debugAterramento'] == 'nao':
        if raw_input('ENTRAR no modo de debug[s/N]?') == 's':
            alteracoes += 1
            sistemaVar['debugAterramento'] = 'sim'
            print 'debug ativado'
    else:
        if raw_input('SAIR do modo de debug[s/N]?') == 's':
            alteracoes += 1
            sistemaVar['debugAterramento'] = 'nao'
            print 'debug desativado'

    print u'Atualmente o diâmetro/raio da haste é informado em', 
    if sistemaVar['unidadeHaste'] == 'm':
        print u'metros'
    elif sistemaVar['unidadeHaste'] == 'mm':
        print u'milímetros'
    elif sistemaVar['unidadeHaste'] == 'pol':
        print u'polegadas'
    else:
        print u'erro: arquivo de configuração existe?'
        print u'      alterando para polegadas'
        sistemaVar['unidadeHaste'] == 'pol'
        alteracoes += 1

    print u' deseja mudar[s/N]?',
    if raw_input() == 's':
        alteracoes += 1
        print u'm   - metros'
        print u'mm  - milímetros'
        print u'pol - polegadas'

        try:
            a = raw_input('>')
        except:
            print u'erro: entrada inválida'
            a = 100

        if a == 'm' or a == 'mm' or a == 'pol':
            sistemaVar['unidadeHaste'] = a
        elif a == 100:
            pass
        else:
            print u'erro: valor inválido'


    print u'mostra varSistema[s/N]?',
    if raw_input() == 's':
        print
        for a, b in sistemaVar.iteritems():
            print str(a)+'  :  '+str(b)

    print

    if alteracoes == 1:
        print u'salvar alteração[s/N]?',
        if raw_input() == 's':
            atualizaArquivoConf(nomeArquivoConfiguracao)
            alteracoes = 0
    elif alteracoes > 1:
        print u'salvar alteraçções[s/N]?'
        if raw_input() == 's':
            atualizaArquivoConf(nomeArquivoConfiguracao)
            alteracoes = 0

def criaArquivoConfiguracao(novo = False):

    if novo:
        if isfile(nomeArquivoConfiguracao) == True:
            print u'aviso: arquivo já existe, sobre escrevendo'
        else:
            print u'aviso: criando arquivo'
    else:
        print u'aviso: nada para fazer aqui'
        return 0

    configuracao = ConfigParser.RawConfigParser()

    #----------------------------------------------------------------
    configuracao.add_section('sistema')
    configuracao.set('sistema', 'prompt', sistemaVar['prompt'])
    configuracao.set('sistema', 'unidadeHaste', sistemaVar['unidadeHaste'])
    configuracao.set('sistema', 'limpaTelaInicial', sistemaVar['limpaTelaInicial'])
    configuracao.set('sistema', 'debugAterramento', sistemaVar['debugAterramento'])

    #----------------------------------------------------------------
    configuracao.add_section('estratificacao')
    configuracao.set('estratificacao', 'p1LimSuperior', sistemaVar['p1LimSuperior'])
    configuracao.set('estratificacao', 'p1LimInferior', sistemaVar['p1LimInferior'])

    configuracao.set('estratificacao', 'kLimSuperior', sistemaVar['kLimSuperior'])
    configuracao.set('estratificacao', 'kLimInferior', sistemaVar['kLimInferior'])

    configuracao.set('estratificacao', 'h1LimSuperior', sistemaVar['h1LimSuperior'])
    configuracao.set('estratificacao', 'h1LimInferior', sistemaVar['h1LimInferior'])

    #----------------------------------------------------------------
    configuracao.add_section('projMalha')
    configuracao.set('projMalha', 'dir', sistemaVar['arqMalha'])

    configuracao.add_section('tabela')
    configuracao.set('tabela', 'dir', sistemaVar['arqTabela'])

    with open(nomeArquivoConfiguracao, 'wb') as configfile:
        configuracao.write(configfile)

def lerArquivoConfiguracao(arquivo = 'configuracoes.cfg'):
    global sistemaVar

    if not isfile(arquivo):
        print u'erro: arquivo de configuração não existe'
        return -1

    configuracao = ConfigParser.ConfigParser()

    try:
        configuracao.read(arquivo)

        sistemaVar['prompt'] = configuracao.get('sistema', 'prompt')
        sistemaVar['limpaTelaInicial'] = configuracao.get('sistema', 'limpaTelaInicial')
        sistemaVar['debugAterramento'] = configuracao.get('sistema', 'debugAterramento')
        sistemaVar['unidadeHaste'] = configuracao.get('sistema', 'unidadeHaste')
        sistemaVar['arqMalha'] = configuracao.get('projMalha', 'dir')
        sistemaVar['arqTabela'] = configuracao.get('tabela', 'dir')

        sistemaVar['p1LimSuperior'] = configuracao.getfloat('estratificacao', 'p1LimSuperior')
        sistemaVar['p1LimInferior'] = configuracao.getfloat('estratificacao', 'p1LimInferior')

        sistemaVar['kLimSuperior'] = configuracao.getfloat('estratificacao', 'kLimSuperior')
        sistemaVar['kLimInferior'] = configuracao.getfloat('estratificacao', 'kLimInferior')

        sistemaVar['h1LimSuperior'] = configuracao.getfloat('estratificacao', 'h1LimSuperior')
        sistemaVar['h1LimInferior'] = configuracao.getfloat('estratificacao', 'h1LimInferior')

    except:
        return -1

    atualizaLimitesOtimizacao()

    if fDebug():
        print sistemaVar

def atualizaArquivoConf(arquivo = 'configuracoes.cfg'):
    if not isfile(arquivo):
        print u'erro: arquivo de configuração não existe'
        print u'      não foi possível atualizar o mesmo' 
        return -1

    print u'aviso: atualizando o arquivo de configuração'

    configuracao = ConfigParser.RawConfigParser()

    #----------------------------------------------------------------
    configuracao.add_section('sistema')
    configuracao.set('sistema', 'prompt', sistemaVar['prompt'])
    configuracao.set('sistema', 'unidadeHaste', sistemaVar['unidadeHaste'])
    configuracao.set('sistema', 'limpaTelaInicial', sistemaVar['limpaTelaInicial'])
    configuracao.set('sistema', 'debugAterramento', sistemaVar['debugAterramento'])

    #----------------------------------------------------------------
    configuracao.add_section('estratificacao')
    configuracao.set('estratificacao', 'p1LimSuperior', sistemaVar['p1LimSuperior'])
    configuracao.set('estratificacao', 'p1LimInferior', sistemaVar['p1LimInferior'])

    configuracao.set('estratificacao', 'kLimSuperior', sistemaVar['kLimSuperior'])
    configuracao.set('estratificacao', 'kLimInferior', sistemaVar['kLimInferior'])

    configuracao.set('estratificacao', 'h1LimSuperior', sistemaVar['h1LimSuperior'])
    configuracao.set('estratificacao', 'h1LimInferior', sistemaVar['h1LimInferior'])

    #----------------------------------------------------------------
    configuracao.add_section('projMalha')
    configuracao.set('projMalha', 'dir', sistemaVar['arqMalha'])

    configuracao.add_section('tabela')
    configuracao.set('tabela', 'dir', sistemaVar['arqTabela'])

    with open(nomeArquivoConfiguracao, 'wb') as configfile:
        configuracao.write(configfile)

    atualizaLimitesOtimizacao()

def atualizaLimitesOtimizacao():

    estratificacao.limites = [ (sistemaVar['p1LimInferior'], sistemaVar['p1LimSuperior']), \
                               (sistemaVar['kLimInferior'], sistemaVar['kLimSuperior']), \
                               (sistemaVar['h1LimInferior'], sistemaVar['h1LimSuperior'])]

def alteraLimitesOtimizacao():

    try:
        print u'Limite superior de p1: ',
        p1s = input()
        print u'Limite inferior de p1: ',
        p1i = input()

        print u'Limite superior de k: ',
        ks = input()        
        print u'Limite inferior de k: ',
        ki = input()        

        print u'Limite superior de h1: ',
        h1s = input()        
        print u'Limite inferior de h1: ',
        h1i = input()        
    except:
        print u'erro: entrada inválida'
        return -1

    sistemaVar['p1LimSuperior'] = p1s
    sistemaVar['p1LimInferior'] = p1i
    sistemaVar['kLimSuperior'] = ks
    sistemaVar['kLimInferior'] = ki
    sistemaVar['h1LimSuperior'] = h1s
    sistemaVar['h1LimInferior'] = h1i

    atualizaArquivoConf()

def plotPhoH():
    if verificaVariaveisProfResi():
        return -1
        
    #plt.subplot(211)
    plt.plot(profundidade, resistividadeMedia)
    plt.xlabel('Profundidade [m]')
    plt.ylabel('Resistividade Media [ohm*m]')
    plt.title('Curva de Resistividade')
    plt.grid(True)


    plt.savefig(dirCurvas+ajudante.separador()+'curvadeResistividade_'+idPlanilha+'_'+formataHora()+'_.png')
    print 'aviso: arquivo png da figura salvo na pasta <curvas>'
    
    #plt.show()
    #s = UnivariateSpline(profundidade, resistividadeMedia, s=1)
    #xs = linspace(0, profundidade[len(profundidade)-1], 1000)
    #ys = s(xs)
    #plt.subplot(212)
    #plt.plot(xs, ys)

    plt.show()
    
def plotCurvaTeorica2Camadas():
    global sistemaResultados

    if verificaVariaveisProfResi(silencioso = 1):
        if lerTabelaExcel(silencioso = 1):
            return -1

    if sistemaResultados['fEstratificacao'] == 0:
        print u'Iniciar o processo de estratificação em 2 camadas[S/n]?',
        if raw_input() != 'n':
            estratificacao.pho = resistividadeMedia
            estratificacao.es = profundidade

            [sistemaResultados['p1'],  \
             sistemaResultados['k'],  \
             sistemaResultados['h']] = estratificacao.estratifica2Camadas()

            sistemaResultados['fEstratificacao'] = 1
        else:
            print u'erro: é necessário iniciar a estratificação'
            return -1

    print sistemaResultados

    a = arange(1e-3, profundidade[len(profundidade)-1], 1e-2)
    p = []
    for i in a:
        p.append(estratificacao.funResistividade2Camadas(i, \
                 sistemaResultados['p1'], \
                 sistemaResultados['k'], \
                 sistemaResultados['h']))

    plt.xlabel('Profundidade [m]')
    plt.ylabel('Resistividade Media [ohm*m]')
    plt.title('Curva teoria e medida')
    plt.plot(a, p, profundidade, resistividadeMedia)
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
            return -1

        rnHorizontais.mostraEquacao(v)

    elif tipo == 'r1':
        r1haste.mostraEquacao()

def projetoMalha():
    global sistemaVar

    a = 0
    if len(sistemaVar['arqMalha']) > 0:
        print u'usar o último arquivo[S/n]?',
        if raw_input() == 'n':       
            a = 1
    else:
        a = 1

    if a == 1:
        try:
            mainTkinter = Tk()
            sistemaVar['arqMalha'] = askopenfilename()
            mainTkinter.destroy() 
            if len(sistemaVar['arqMalha']) > 0:
                print 'usando,'
                print sistemaVar['arqMalha']
                atualizaArquivoConf()
            else:
                print u'erro: erro na seleção do arquivo'
                return -1
        except:
            print u'erro: no arquivo de configuração do projeto'
            return -1

    try:
        malhaAterramento.lerArquivoProjeto(sistemaVar['arqMalha'], debug = fDebug())
        #malhaAterramento.mostraDadosProjeto()
        malhaAterramento.projetaMalhaAterramento(debug = fDebug())
        malhaAterramento.exibeResultados()
    except:
        print u'erro: problema no projeto da malha'

def testaLatex():

    conteudo = r'''\documentclass{article}
\begin{document}
...
\textbf{\huge %(school)s \\}
\vspace{1cm}
\textbf{\Large %(title)s \\}
...
\end{document}
'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--course', default = 'engenharia')
    parser.add_argument('-t', '--title', default = 'aqui')
    parser.add_argument('-n', '--name', default = 'felipe')
    parser.add_argument('-s', '--school', default = 'My U')

    args = parser.parse_args()
    a = conteudo%args.__dict__

    print a
    print args.__dict__    

def preparaRelatorioEstratificacaoLatex():
    #print docLatex%dicRelatorioEstratificacaoLatex

    with open(dirResultados+'\\'+nomeRelatorioEstratificacao, 'w') as f:
        f.write(relatorioEstratificacao.docLatex%dicRelatorioEstratificacaoLatex)

def geraRelatorioLatex():
    print u'Deseja gerar relatório para a estratificação[S/n]?',
    if raw_input() != 'n':    
        cmdPdfLatex = r'pdflatex .\resultados\%s -output-directory .\resultados' % (nomeRelatorioEstratificacao)

        #arquivoLatex = open(dirResultados+'\\'+nomeRelatorioEstratificacao, 'wb')
        #arquivoLatex.write(relatorioEstratificacao.docLatex)
        #arquivoLatex.close()

        #call([cmdPdfLatex, argPdfLatex], shell = True)
        #call(r"pdflatex .\resultados\relatorio_estratificacao.tex -output-directory .\resultados", shell = True)

        preparaRelatorioEstratificacaoLatex()

        try:
            a = subprocess.call(cmdPdfLatex , shell = True)
        except:
            print u'erro: não foi possivel gerar o arquivo de relatório'

        limpaTela()

        fRelatorioGerado = 1
    else:
        fRelatorioGerado = 0

    if fRelatorioGerado:
        print u'aviso: relatório gerado com sucesso'
        print u'       use <ver relatorio> para ver o resultado'
        return 0
    else:
        return -1

def verRelatorio():
    cmdPdfLatex = r'.\%s\%s.pdf' % (ndirResultados, nomeRelatorioEstratificacao[:-4])
    if not isfile(cmdPdfLatex):
        print u'erro: é de extrema importância a geração do relatório antes de sua visualização'
        print u'      use <relatorio> para a geração do mesmo'
    else:
        subprocess.call(cmdPdfLatex, shell = True)

def chamaIpython():
    embed()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLE DO PROGRAMA
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def exterminaPrograma(): 
    print 'saindo...'
    sys.exit()

def nada():
    # ESPECIAL ;)
    hal9000()

def inicializacao():
    #print u'aviso: carregando arquivo de configuração'

    if lerArquivoConfiguracao(nomeArquivoConfiguracao):
        criaArquivoConfiguracao(True)

    if fDebug():
        print u'arquivo de inicialização lido com sucesso'

    try:
        mkdir(dirCurvas)
    except Exception, e:
        if fDebug():
            print u'aviso: não foi possivel criar diretório para as curvas, talvez ele já exista'        

    try:
        mkdir(dirResultados)
    except:
        if fDebug():
            print u'aviso: não foi possivel criar diretório para os resultados, talvez ele já exista'

    if fDebug():
        print u'aviso: inicialização finalizada'

# def artMain():
#     m, u, ln, oo, k0, c0, km1, km2, km3, cm1, cm2, cm3, d0, a, N= symbols('m, u, ln, oo, k0, c0, km1, km2, km3, cm1, cm2, cm3, d0, a, N')
#     f = 1 + Sum((u**m*(km1/cm1 + (2*km2)/cm2 + km3/cm3))/(ln(16*a/d0) + k0/c0),(m, 1, oo))
#     pprint(f)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def limpaTela():
    return system(ajudante.cmdLimpaTela())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def login():
    try:
        f = open('.s.pa', 'r')
        p = f.readline()
        f.close()
    except:
        print 'erro: impossivel ler arquivo'
        return -1
    u = hashlib.sha512(getpass.getpass('senha: ')+SAL+str(get_mac())).hexdigest()
    if u != p:
        print 'senha incorreta'
        return -1
    else:
        return 0

def mensagemInicial():
    print u'Cálculos para sistemas de aterramento , v.', versao
    print u'Felipe Bandeira, junho/2013, Fortaleza-CE'
    print
    print u'digite <ajuda> para mais informações'

################################################################################################
# COMANDOS CADASTRADOS
################################################################################################

dicionarioComandos = {  
    'h' : ajudaBasica,
    'ajuda' : ajudaCompleta,

    'o' : sistema, 
    'sistema' : sistema,

    's' : exterminaPrograma, 
    'sair' :  exterminaPrograma, 

    'c' : calculosResistividade,
    'topologias' : calculosResistividade,

    'k' : curvaK,
    'curvak' : curvaK,

    'e' : estratificacaoSolo,
    'estratificacao' : estratificacaoSolo,

    'a' : lerTabelaExcel,
    'excel' : lerTabelaExcel,

    'relatorio' : geraRelatorioLatex,

    'ver relatorio' :  verRelatorio,

    'p' : plotPhoH,
    'plothp' : plotPhoH,

    'pt' : plotCurvaTeorica2Camadas,

    'n' : mostraEquacoes, 
    'equacoes' : mostraEquacoes,

    'm' : projetoMalha,
    'malha' : projetoMalha,

    'cls' : limpaTela,

    'lerconf' : lerArquivoConfiguracao,

    'ipython' : chamaIpython,

    'tl' : testaLatex,

    'pl' : preparaRelatorioEstratificacaoLatex,
}

# interpreta os comandos do usuário
def cmds(cmd): 
    return dicionarioComandos.get(cmd, nada)()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# MAIN
loginComSenha = False
habilitaCodificacao = False
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if __name__ == '__main__':

    if habilitaCodificacao:
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
        charVga = codecs.getwriter('cp850')
        sys.stdout = charVga(sys.stdout)

    if loginComSenha:
        limpaTela()
        if login():
            sys.exit(0)

    if len(sys.argv) > 1:
        print sys.argv
        sys.exit(0)
    else:
        limpaTela()

        mensagemInicial()
        inicializacao()
        #ajudaBasica()

        if sistemaVar['limpaTelaInicial'] == 'sim':
            limpaTela()
        else:
            print

        while True:
            entrada = raw_input(sistemaVar['prompt'])
            
            if entrada == "":
                continue

            cmds(entrada.lower())
