# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica
#
#-------------------------------------------------------------------------------
# Dimensionamento de uma malha de aterramento
#
# Teoria, Kindermann:
# Dimensionar uma malha de terra é verificar se potenciais que surgem na superfície 
# do solo, quando da ocorreência do máximo defeito à terra, são inferiores aos 
# máximos potenciais de passo e toque que uma pessoa pode suportar sem a ocorrência
# de fibrilação ventricular. Além disso, deve ser dimensionado o condutor da malha, de
# forma a suportar os esforços mecânicos e térmicosa que estarão sujeitos ao longo de
# sua vida útil. É fundamental também, levar-se em conta que o valor da resistência de
# terra da malha deve ser compatível com a sensibilidade da proteção. Isto é, o relé de
# sobrecorrente de neutro deve atuar adequadamente para o nível de corrente de curto
# circuito à terra no final do trecho protegido. Deve-se ressaltar que o dimensionamento
# de uma malha de terra é um processo iterativo. Parte-se de uma malha inicial e
# verificam se os potenciais, na superfície do solo, quando do máximo defeito à terra, 
# são inferiores aos valores máximo suportáveis por um ser humano.
#
# Itens necessários ao Projeto:
# 1 - Medições pelo método de Wenner, a fim de se obter a estratificação do solo.
# 2 - O uso de brita aumenta a segurança para o ser humano e mantem o solo com suas
# propriedades, normalmente a resistividade do solo é ps = 3000 ohm.m, caso não exista
# brita adotar ps = p1, onde p1 é a resisitividade da primeira camada.
# 3 - Corrente de curto-circuito máxima entre fase e terra no local da malha de terra
# Imaximo = 3*I0.
# 4 - Percentual da corrente de curto-circuito máxima que realmente escoa pela malha.
# 5 - Tempo de defeito para a máxima corrente de curto-circuito fase-terra
# 6 - Área da malha pretendida
# 7 - Valor máximo da resitência de terra de modo a ser compatível com a sensibilidade da
# proteção.
#-------------------------------------------------------------------------------
#

from __future__ import division
from math import sqrt, log, pi
import estratificacao
import potenciais
import ConfigParser
from os import getcwd, mkdir
from os.path import isdir, isfile
#from decimal import *

pastaTrabalho = getcwd()+'\\tabelas'
nomeArquivoProjeto = 'projetoMalha.cfg'
nomeArquivoProjetoCompleto = pastaTrabalho+'\\'+nomeArquivoProjeto

projetoMalha = {
	# configurações do solo
	'peq' : 0,
	'pn1' : 0, 
	'deq' : 0,

	# configurações da brita
	'psBrita' : 0,
	'hsBrita' : 0,

	# configurações da malha de terra
	'mLargura' : 0,
	'mComprimento' : 0,
	'mProfundidade' : 0,

	# informações sobre o curto
	'iCurtoMaximo' : 0,
	'iMalha' : 0,
	'tDefeito' : 0,

	# informações sobre o tipo de ligação
	'condutorMalha' : '',
	'condutorLigacoes' : ''
} 

projetoResultado = {
	
}

def formulaOnderdonk(scobre, tDefeito, oa, om= 0, conexao = 'outra'):
	"""Dimensionamento térmico de um condutor do tipo cobre a suportar 
 	corrente de curto

 	Entrada:
 	scobre = seccão do condutor de cobre da malha de terra em mm^2
 	tDefeito = duração do defeito em segundos
 	oa = temperatura ambiente em graus
 	om = temperatura máxima permissivel em graus
 	conexao = 'pressao', 'solda', 'brasagem', 'exotermica', 'outra'
 		se outra foi escolhida o valor de om deve ser especificado

 	OBSERVAÇÕES:
 	- conexão cavilhada com juntas de bronze, por pressão, om = 250 graus
 	- solda convencional feita com elétrodos revestidos, maquina de solda, om = 450 gruaus
 	- brasagem com liga de Foscoper, maçarico, om = 550 graus
 	- solda exotérmica, fusão, om = 850 graus

 	Saída:

 	iDefeito = corrente de defeito em Amperes, através do condutor
	"""

	if conexao == 'pressao':
		print 'aviso: conexao pressao'
		om = 250

	elif conexao == 'solda':
		print 'aviso: conexao solda'
		om = 450

	elif conexao == 'brasagem':
		print 'aviso: conexao brasagem'
		om = 550

	elif conexao == 'exotermica':
		print 'aviso: conexao exotermica'
		om = 850

	elif conexao == 'outra':
		print 'aviso: conexao diferente'

	else:
		print 'erro: conexao desconhecida'
		return

	iDefeito = 226.53*scobre*sqrt((1/tDefeito)*log((om-oa)/(234+oa)+1))
	return iDefeito


def formulaOnderdonkScobre(iDefeito, tDefeito, oa, om= 0, conexao = 'outra'):
	"""Dimensionamento térmico de um condutor do tipo cobre a suportar 
 	corrente de curto

 	Entrada:
 	scobre = seccão do condutor de cobre da malha de terra em mm^2
 	tDefeito = duração do defeito em segundos
 	oa = temperatura ambiente em graus
 	om = temperatura máxima permissivel em graus
 	conexao = 'pressao', 'solda', 'brasagem', 'exotermica', 'outra'
 		se outra foi escolhida o valor de om deve ser especificado

 	OBSERVAÇÕES:
 	- conexão cavilhada com juntas de bronze, por pressão, om = 250 graus
 	- solda convencional feita com elétrodos revestidos, maquina de solda, om = 450 gruaus
 	- brasagem com liga de Foscoper, maçarico, om = 550 graus
 	- solda exotérmica, fusão, om = 850 graus

 	Saída:

 	scobre = seccão do condutor de cobre em mm^2
	"""

	if conexao == 'pressao':
		print 'aviso: conexao pressao'
		om = 250

	elif conexao == 'solda':
		print 'aviso: conexao solda'
		om = 450

	elif conexao == 'brasagem':
		print 'aviso: conexao brasagem'
		om = 550

	elif conexao == 'exotermica':
		print 'aviso: conexao exotermica'
		om = 850

	elif conexao == 'outra':
		print 'aviso: conexao diferente'

	else:
		print 'erro: conexao desconhecida'
		return

	scobre = iDefeito/(226.53*sqrt((1/tDefeito)*log((om-oa)/(234+oa) + 1)))

	if recomedacaoCondutor(scobre):
		print 'aviso projeto: mudando para 35 mm^2'
		scobre = 35
	return scobre

def recomedacaoCondutor(scobre):
	if scobre < 35:
		print 'aviso projeto: aconselha-se a utilizar um condutor de 35 mm^2 por razoes mecanicas'
		print '               secao atual do condutor = ', scobre		
		return 1

	return 0

def diametroCondutor(area):
	"""Diametro do condutor
	Entrada:
	area = em mm^2

	Saída:
	d = diâmetro em mm
	"""
	d = 2*sqrt((area*10**-6)/pi)

	return d

def numeroCondutores(a, b, eb, ea):
	"""
	Entrada:
	a = comprimento da malha [m]
	b = largura da malha [m]
	eb = espaçamento em b entre dois condutores [m]
	ea = espaçamento em a entre dois condutores [m]

	Saída:
	Na = número de condutores no eixo x
	Nb = número de condutores no eixo y
	lCabo = comprimento minimo para os cabos da malha
	"""

	Na = a/ea + 1
	Nb = b/eb + 1

	# comprimento total de condutores da malha
	lCabo = a*Nb+b*Na

	return [Na, Nb, lCabo]

def espacamentoEntreCondutores(N, a):
	"""
	Entrada:
	N = número de condutores
	a = tamanho total em um eixo

	Saída:
	e = espaçamento entre dois condutores
	"""
	e = a/(N-1)

	return e

def resistenciaMalhaSverak(pa, lTotal, aMalha, h):
	"""Aproximação da resistência da malha pela fórmula de Sverak
	Está resistência da malha representa a resistência elétrica da malha até o 
	infinito. Seu valor deverá ser menor do que a máxima resistência limite da
	sensibilidade(ajuste) do relé de neutro.

	Entrada:
	pa = resistividade aparente do solo
	aMalha = área ocupada pela malha [m^2]
	lTotal = comprimento total dos cabos e hastes que formam a malha
	h = profundidade da malha [m], 0.25 <= h <= 2.5 m

	Saída:
	resistencia de aterramento da malha
	"""

	if h < 0.25 or h > 2.5:
		print 'erro: Valores de profundidade da malha nao satisfaz a equacao'
		return 1e6

	rMalha = pa*(1/lTotal + (1/sqrt(20*aMalha)*(1 + 1/(1 + h*sqrt(20/aMalha)))))

	return rMalha

def correcaoProfundidade(h, h0 = 1):
	kh = sqrt(1 + h/h0)
	return kh

def nCondutoresMalha(Na, Nb):
	"""
	A malha retangular é transformada numa malha quadrada com N condutores paralelos
	em cada lado
	"""

	N = sqrt(Na*Nb)

	return N

def coeficienteMalha(e, h, d, kh, N, kii = 1):
	"""
	e = espaçamento entre condutores paralelos ao longo do lado da malha [m]
	h = profundidade da malha[m]
	d = diâmetro do condutor da malha [m]
	N
	kii = 1,  para malha com hastes cravadas ao longo do perímetro ou nos
		cantos da malha ou ambos

	kh = correção de profundidade é calculado
	"""

	if N > 25:
		print 'erro: limitacao de N para menor 25'
		return

	if d >= (0.25*h):
		print 'erro: limitacao de d para menor ', 0.25*h
		return

	if e < 2.5:
		print 'erro: espacamento menor que 2.5 [m]'
		return

	if h > 2.5 or h < .25:
		print 'erro: pronfudidade limitada de 0.25 a 2.5'
		return

	km = (1/(2*pi))*(log((e**2)/(16*h*d)+((e+2*h)**2)/(8*e*d)-h/(4*d))+(kii/kh)*log(8/(pi*(2*N-1))))
	
	return km

def Kii(N):
	return 1/((2*N)**(2/N))

def coeficienteIrregularidade(N):

	ki = 0.656 + 0.172*N

	return ki

def potencialMalha(pa, km, ki, iMalha, lTotal):
	"""Potência de malha máximo se encontra nos cantos da malha
	
	Entrada:
	pa = resistividade aparente do solo
	km = coeficiente de malha
	ki = coeficiente de irregularidade
	iMalha = parcela da corrente máxima de falta que realmente escoa da malha
		para a terra
	lTotal = comprimento total dos condutores da malha
	"""

	vMalha = (pa*km*ki*iMalha)/lTotal

	return vMalha

def comprimentoTotal15(lCabo, lHastes):
	"""No caso de malhas onde são colocadas hastes cravadas nos cantos e/ou 
	no perímetro, as correntes têm maior facilidade de escoar mais profundamente
	no solo, alterando, portanto, o potencial de malha.
	comprimento virtual ponderado em 15%   do total
	"""
	lTotal = lCabo + 1.15*lHastes

	return lTotal

def potencialPasso(pa, kp, ki, iMalha, lTotal):
	"""
	pa = resistividade aparente
	kp = coeficiente do maior potencial entre dois pontos distanciados de 1m
	"""
	vps = (pa*kp*ki*iMalha)/lTotal

	return vps

def coeficienteKp(h, e, N):
	kp = (1/pi) * ( 1/(2*h) + (1/(e+h)) + (1/e)*(1 -  (0.5**(N-2))  ))
	return kp

def kCoeficienteReflexao(p1, p2):
	k = (p1 - p2)/(p1 + p2)
	return k

def comprimentoMinimoCondutor(pa, km, ki, iMalha, vToqueMaximo):
	lMinimo = (pa*km*ki*iMalha)/vToqueMaximo

	return lMinimo

def exemploKindermann():
	# print estratificacao.curvaEndrenyi(1.15, 401.85, 1726.46)
	# print estratificacao.curvaEdnrenyiBeta(2.6, .138)
	# pa = estratificacao.resistividadeAparente2CamadasMalha(580, 80, 12, 2000, 64.03)
	# print pa

	# Exemplo proposto pelo Kindermann no livro Aterramento Elétrico
	#
	# Projetar uma malha de terra com os seguintes dados pré-definidos:
	# I curto maximo = 3000 A
	# I malha = 1200 A
	# Tempode abertura da proteção para a corrente de defeito é tdefeito = 0.6 seguintes
	# Dimensões da malha,
	# largura 50 m
	# largura  = 40 m
	# profundidade .6 m a partir da base do solo
	# Caracteristicas do solo,
	# ps = pbrita = 3000 ohm*m com uma camada de 20cm colocada na superficie do solo
	# deq  =12 m
	# peq = 580 ohm*m
	# pn+1 = 80 ohm*m

	# determinação de pa, vista pela malha

	print 'Resistividade aparente vista pela malha'

	largura = 40
	comprimento = 50
	area = largura*largura
	dimensao = sqrt(largura**2 + comprimento**2)
	r = area/dimensao

	deq = 12
	pn1 = 80
	peq = 580

	alfa = r/deq
	beta = pn1/peq

	#N = estratificacao.curvaEdnrenyiBeta(alfa, beta)
	#print 'N, ', N
	N = estratificacao.endrenyi1963(beta, alfa, r)
	print 'N, ', N

	#pa = .71*580
	pa = N*580

	print 'largura, ', largura
	print 'comprimento, ', comprimento
	print 'area, ', area
	print 'dimensao, ', dimensao
	print 'r, ', r
	print 'alfa, ', alfa
	print 'beta, ', beta
	print 'pa, ', pa

	print '-'*80

	# cálculando a corrente de defeito

	print 'Calculando a seccao dos condutores'

	iCurtoMaximo = 3000
	iDefeito = .6*iCurtoMaximo
	tDefeito = 0.6

	print 'corrente de curto, ', iCurtoMaximo
	print 'corrente de defeito, ', iDefeito

	scobre = formulaOnderdonkScobre(iDefeito, tDefeito, 30, conexao = 'solda')

	print 'seccao do condutor de cobre, ', scobre

	# calculando a bitola do cabo de ligacao
	# conexão é feita utilizando pressão
	scobreCabo = formulaOnderdonkScobre(iCurtoMaximo, tDefeito, 30, conexao = 'pressao')

	print 's cabo de ligacao, ', scobreCabo

	print '-'*80

	# valores dos potenciais maximos admissiveis

	print 'valores dos potenciais maximos admissiveis'

	pbrita = 3000
	hs = .2
	k = kCoeficienteReflexao(pa, pbrita)

	print 'k, ', k 

	cs = potenciais.fatorCorrecaoBrita(hs, pa, pbrita)
	print 'fator de correcao, ', cs

	vToqueMaximo = potenciais.potencialMaximoToqueCS(pbrita, tDefeito, cs)
	print 'V toque maximo, ', vToqueMaximo

	vPassoMaximo = potenciais.potencialMaximoPassoCS(pbrita, tDefeito, cs)
	print'V passo maximo, ', vPassoMaximo

	print '-'*80

	
def criarArquivoProjeto(novo = False, debug = False):

	if debug:
		print 'criando arquivo de configuracao, '

	if isfile(nomeArquivoProjetoCompleto) == True:

		if debug:
			print 'aviso: arquivo ja existe'

		if novo == False:
			return
		else:
			if debug:
				print 'aviso: sobrescrevendo'

	if isdir(pastaTrabalho) == False:
		if debug:
			print 'aviso: criando pasta <tabelas>'
		mkdir(pastaTrabalho)	

	projeto = ConfigParser.RawConfigParser()

	projeto.add_section('solo')
	projeto.set('solo', 'peq', '580')
	projeto.set('solo', 'pn1', '80')
	projeto.set('solo', 'deq', '12')

	projeto.add_section('brita')
	projeto.set('brita', 'ps', '3000')
	projeto.set('brita', 'hs', '.2')

	projeto.add_section('malha')
	projeto.set('malha', 'largura', '40')
	projeto.set('malha', 'comprimento', '50')
	projeto.set('malha', 'profundidade', '.6')

	projeto.add_section('curto')
	projeto.set('curto', 'iCurtoMaximo', '3000')	
	projeto.set('curto', 'iMalha', '1200')	
	projeto.set('curto', 'tDefeito', '.6')	

	projeto.add_section('condutores')
	projeto.set('condutores', 'malha', 'solda')	
	projeto.set('condutores', 'ligacao', 'pressao')	

	with open(nomeArquivoProjetoCompleto, 'wb') as configfile:
		projeto.write(configfile)

def lerArquivoProjeto(arquivo, debug = False):

	global projetoMalha

	projeto = ConfigParser.ConfigParser()
	projeto.read(arquivo)


	projetoMalha['peq'] = projeto.getfloat('solo', 'peq')
	projetoMalha['pn1'] = projeto.getfloat('solo', 'pn1')
	projetoMalha['deq'] = projeto.getfloat('solo', 'deq')

	projetoMalha['psBrita'] = projeto.getfloat('brita', 'ps')
	projetoMalha['hsBrita'] = projeto.getfloat('brita', 'hs')

	projetoMalha['mLargura'] = projeto.getfloat('malha', 'largura')
	projetoMalha['mComprimento'] = projeto.getfloat('malha', 'comprimento')
	projetoMalha['mProfundidade'] = projeto.getfloat('malha', 'profundidade')

	projetoMalha['iCurtoMaximo'] = projeto.getfloat('curto', 'iCurtoMaximo')
	projetoMalha['iMalha'] = projeto.getfloat('curto', 'iMalha')
	projetoMalha['tDefeito'] = projeto.getfloat('curto', 'tDefeito')

	projetoMalha['condutorMalha'] = projeto.get('condutores', 'malha')
	projetoMalha['condutorLigacoes'] = projeto.get('condutores', 'ligacao')


	if debug:
		print projetoMalha

def mostraDadosProjeto():
	print 'entrada para o projeto,'
	print projetoMalha

def projetaMalhaAterramento(debug = False):
	largura = projetoMalha.get('mLargura')
	comprimento = projetoMalha.get('mComprimento')
	hMalha = projetoMalha.get('mProfundidade')

	deq = projetoMalha.get('deq')
	pn1 = projetoMalha.get('pn1')	
	peq = projetoMalha.get('peq')

	area = largura*comprimento
	dimensao = sqrt(largura**2 + comprimento**2)
	r = area/dimensao

	alfa = r/deq
	beta = pn1/peq

	N = estratificacao.endrenyi1963(beta, alfa, r)

	pa = peq*N

	if debug:
		print '-'*80
		print 'dimensao, ', dimensao
		print 'raio da malha, ', r
		print 'alfa, ', alfa
		print 'beta, ', beta
		print 'N de Endrenyi, ', N
		print 'resistividade aparente, vista pela malha', pa

	iCurtoMaximo = projetoMalha.get('iCurtoMaximo')
	iDefeito = .6*iCurtoMaximo
	tDefeito = 	projetoMalha.get('tDefeito')

	if debug:
		print '-'*80
		print 'corrente de curto, ', iCurtoMaximo
		print 'corrente de defeito, ', iDefeito

	# calculando a bitola dos cabos da malha
	scobre = formulaOnderdonkScobre(iDefeito, tDefeito, 30, conexao = projetoMalha.get('condutorMalha'))
	# calculando a bitola dos cabos de ligações
	scobreCabo = formulaOnderdonkScobre(iCurtoMaximo, tDefeito, 30, conexao = projetoMalha.get('condutorLigacoes'))

	if debug:
		print '-'*80
		print 's cabo de ligacao, ', scobreCabo
		print 'seccao do condutor de cobre, ', scobre

	psBrita = projetoMalha.get('psBrita')
	hsBrita = projetoMalha.get('hsBrita')

	k = kCoeficienteReflexao(pa, psBrita)
	cs = potenciais.fatorCorrecaoBrita(hsBrita, pa, psBrita)
	vToqueMaximo = potenciais.potencialMaximoToqueCS(psBrita, tDefeito, cs)
	vPassoMaximo = potenciais.potencialMaximoPassoCS(psBrita, tDefeito, cs)

	if debug:
		print '-'*80
		print 'k, ', k 
		print 'V toque maximo, ', vToqueMaximo
		print 'fator de correcao, ', cs
		print'V passo maximo, ', vPassoMaximo

	# valores iniciais para o espaçamento da malha
	ea = 3
	eb = 3
	[Na, Nb, lCabo] = numeroCondutores(comprimento, largura, ea, eb)

	# Número de condutores é um número inteiro
	Na = round(Na, 0)
	Nb = round(Nb, 0)

	# novo espaçamento entre dois condutores
	ea = espacamentoEntreCondutores(Na, comprimento)
	eb = espacamentoEntreCondutores(Nb, largura)

	# calculando a resistência da malha
	rMalha = resistenciaMalhaSverak(pa, lCabo, area, hMalha)

	iMalha = projetoMalha.get('iMalha')

	vToqueMaximoMalha = rMalha * iMalha

	Kh = correcaoProfundidade(hMalha)

	N = nCondutoresMalha(Na, Nb)

	kii = Kii(N) 

	d = diametroCondutor(scobre)

	km = coeficienteMalha(max([ea, eb]), hMalha, d, Kh, N, kii)

	ki = coeficienteIrregularidade(N)

	vMalha = potencialMalha(pa, km, ki, iMalha, lCabo)

	lMinimo = comprimentoMinimoCondutor(pa, km, ki, iMalha, vToqueMaximo)


	if debug:
		print 'numero de condutores Na, ', Na
		print 'numero de condutores Nb, ', Nb
		print 'comprimento do cabo, ', lCabo
		print 'resistencia da malha, ', rMalha
		print 'v toque maximo da malha, ', vToqueMaximoMalha
		if vToqueMaximoMalha > vToqueMaximo:
			print 'erro projeto: tensao de toque ultrapassa os limites'	

		print 'Kh, ', Kh
		print 'Kii, ', kii
		print 'N, ', N
		print 'd, ', d
		print 'km, ', km
		print 'Ki, ', ki

		print 'vMalha, ', vMalha
		if vMalha > vToqueMaximo:
			print 'erro projeto: tensao maxima na malha ultrapassa os limites'

		print 'comprimento minimo condutor, ', lMinimo

if __name__ == '__main__':
	#exemploKindermann()
	
	criarArquivoProjeto(novo = False, debug = True)
	lerArquivoProjeto(nomeArquivoProjetoCompleto, debug = True)
	projetaMalhaAterramento(debug = True)

	#saida = raw_input('[ENTER] para sair')