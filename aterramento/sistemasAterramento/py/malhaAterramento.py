# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica
#
#-------------------------------------------------------------------------------
# Dimensionamento de uma malha de aterramento
#-------------------------------------------------------------------------------
#

from __future__ import division
from math import sqrt, log, pi
import estratificacao
import potenciais

def formulaOnderdonk(scobre, tDefeito, oa, om= 0, conexao = 'outra'):
	"""
 	Dimensionamento térmico de um condutor do tipo cobre a suportar 
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
	"""
 	Dimensionamento térmico de um condutor do tipo cobre a suportar 
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

	scobre = iDefeito/(226.53*sqrt((1/tDefeito)*log((om-oa)/(234+oa) + 1)))

	recomedacaoCondutor(scobre)
	return scobre

def recomedacaoCondutor(scobre):
	if scobre < 35:
		print 'aviso: aconselha-se a utilizar um condutor de 35 mm^2 por razoes mecanicas'
		print '       secao atual do condutor = ', scobre

def numeroCondutores(a, b, eb, ea):
	"""
	Entrada:
	a = comprimento da malha [m]
	b = largura da malha [m]
	eb = espaçamento em b entre dois condutores [m]
	ea = espaçamento em a entre dois condutores [m]
	"""

	Na = a/ea + 1
	Nb = b/eb + 1

	# comprimento total de condutores da malha
	lCabo = a*Nb+b*Na

	return [Na, Nb, lCabo]

def resistenciaMalhaLaurent(pa, lTotal, aMalha, h):
	"""
	Aproximação da resistência da malha

	Entrada:
	pa = resistividade aparente do solo
	aMalha = área ocupada pela malha [m^2]
	lTotal = comprimento total dos cabos e hastes que formam a malha
	h = profundidade da malha [m], 0.25 <= h <= 2.5 m

	Saída:
	resistencia de aterramento da malha
	"""

	rMalha = pa*(1/lTotal + (1/sqrt(20*aMalha)*(1 + 1/(1 + h*sqrt(20/aMalha)))))

	return rMalha

def correcaoProfundidade(h, h0 = 1):
	kh = sqrt(1 + h/ho)
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

	km = (1/(2*pi))*(log((e**2)/(16*h*d)+((e+2*h)**2)/(8*e*d)+(kii/kh)*log(8/(pi*(2*N-1)))))
	return km

def coeficienteIrregularidade(N):

	ki = 0.656 + 0.172*N

	return ki

def potencialMalha(pa, km, ki, iMalha, lTotal):
	"""
	Potência de malha máximo se encontra nos cantos da malha
	Entrada:
	pa = resistividade aparente do solo
	km = coeficiente de malha
	ki = coeficiente de irregularidade
	iMalha = parcela da corrente máxima de falta que realmente escoa da malha
		para a terra
	lTotal = comprimento total dos condutores da malha
	"""
	vMalha = (pa*km*ki*iMalha)/lTotal

def comprimentoTotal15(lCabo, lHastes):
	"""
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

if __name__ == '__main__':
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
	# altura  = 40 m
	# profundidade .6 m a partir da base do solo
	# Caracteristicas do solo,
	# ps = pbrita = 3000 ohm*m com uma camada de 20cm colocada na superficie do solo
	# deq  =12 m
	# peq = 580 ohm*m
	# pn+1 = 80 ohm*m

	# determinação de pa, vista pela malha

	print 'Resistividade aparente vista pela malha'

	altura = 40
	largura = 50
	area = altura*largura
	dimensao = sqrt(altura**2 + largura**2)
	r = area/dimensao

	deq = 12
	pn1 = 80
	peq = 580

	alfa = r/deq
	beta = pn1/peq

	N = estratificacao.curvaEdnrenyiBeta(alfa, beta)
	print 'N, ', N

	pa = .71*580

	print 'altura, ', altura
	print 'largura, ', largura
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

	saida = raw_input('[ENTER] para sair')
