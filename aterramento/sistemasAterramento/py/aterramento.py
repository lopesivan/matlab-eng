# -*- coding: cp1252 -*-
import r1haste
import rnhastes
from pylab import arange, plot, show
from tkFileDialog import askopenfilename
from Tkinter import Tk
import estratificacao
import configuracoes

versao = '0.1beta'

#variaveis de controle do sistema
usaValoresArquivo = 1

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

    plot(numeroHastes, res)
    show()
        
    
def curvaK():
    en = entradaHastesLinha()
    fim = input('quantidade final de hastes: ')
    passo = input('passo: ')

    levantaCurvaK(en[0], en[1], en[2], en[3], en[4], fim, passo)
    

def calculosResistividade():
    
    print '[0] - calculo para 1 haste'
    print '[1] - calculo para n hastes em paralelo(linha)'
    print '[2] - quadrado cheio'
    print '[3] - triangulo'
    print '[4] - circunferencia'
    
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
    print 'resistencia calculada:', res

def planilhaExcel(p = None, debug = True):

    global profundidade, resisitividadeMedia

    if p == None:
        mainTkinter = Tk()
        planilha = askopenfilename()
        mainTkinter.destroy()
        if debug:
            print planilha    
    else:
        planilha = p

    mDados = estratificacao.lerPlanilha(planilha)
    [profundidade, resisitividadeMedia] = estratificacao.resistividadeMediaPlanilha(mDados)        

    if debug:
        print 'Valores disponiveis da tabela,'
        print mDados
        print 'profundidade | resisitividade media'
        for i in range(len(profundidade)):
            print profundidade[i], resisitividadeMedia[i]

    print 'aviso: valores de profundidade e resistivdade foram atualizados'

def estratificacaoSolo():
    # print estratificacao.pho
    # print estratificacao.es
    # print estratificacao.chuteInicial

    # estratificacao.pho = [320, 245, 182, 162, 168, 152]
    # estratificacao.es = [2.5, 5, 7.5, 10, 12.5, 15]
    # estratificacao.chuteInicial = [0, 0, 0]    

    # print estratificacao.pho
    # print estratificacao.es
    # print estratificacao.chuteInicial

    # print estratificacao.estratifica2Camadas()

    try:
        estratificacao.pho = resisitividadeMedia;
        estratificacao.es = profundidade;
        estratificacao.chuteInicial = [0, 0, 0]
    except:
        print "erro: nao e' possivel encontrar os valores de resisitivdade e profundidade"
        return

    [p1, k, h] = estratificacao.estratifica2Camadas()    
    print 'Resistividade primeira camada, ', p1
    print 'Indice de reflexao, ', k
    print 'Profundidade da primeira camada, ', h

    pass

def lerCSV():
    pass

def ajudaBasica():
    print 'lista de comandos disponiveis:'
    print '[h] - ajuda'
    print '[o] - sistema de calculos'
    print '[s] - extermina o programa'
    print '[c] - inicia os calculos para sistema aterramento'
    print '[k] - levanta a curva K de uma malha'
    print '[e] - inicia o processo de estratificacao do solo'
    print '[a] - ler uma planilha de dados'
    print '[q] - ler um arquivo csv'
    print 

def sistema():
    global usaValoresArquivo
    global profundidade, resisitividadeMedia

    print 'Controle do sistema,'
    print 'Usa variaveis adquiridas apartir de um arquivo, @', usaValoresArquivo

    if raw_input('mostrar variaveis[s/N]?') == 's':
        try:
            if len(profundidade)>0 and len(resisitividadeMedia):
                print 'profundidade | resisitividade media'
                for i in range(len(profundidade)):
                    print profundidade[i], resisitividadeMedia[i]
        except:
            print 'aviso: nada para mostrar'
            print 'carregue um arquivo antes desta acao'

    if raw_input('carregar o arquivo de configuracao[s/N]?') == 's':
        try:
            print configuracoes.arquivoExcel
            planilhaExcel(configuracoes.arquivoExcel, debug = None)
        except:
            pass

def exterminaPrograma(): exit()
def nada(): pass

dicionarioComandos = {  'h' : ajudaBasica,
                        'o' : sistema, 
                        's' : exterminaPrograma, 
                        'c' : calculosResistividade,
                        'k' : curvaK,
                        'e' : estratificacaoSolo,
                        'a' : planilhaExcel,
                        'q' : lerCSV
                    }

def cmds(cmd): return dicionarioComandos.get(cmd, nada)()

if __name__ == '__main__':

    print 'Calculos para sistemas de aterramento'
    print 'Felipe Bandeira, 22/06/2013'
    print 

    ajudaBasica()

    while True:
        cmds(raw_input('>>'))       
