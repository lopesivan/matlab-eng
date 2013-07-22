# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica
#
#-------------------------------------------------------------------------------
# Cáculos para condutores enterrados horizontalmente
#-------------------------------------------------------------------------------

from __future__ import division
import r1haste
from math import sqrt, pi, log
#from sympy import symbols, pprint

def condutorUnico(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = comprimento do condutor[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(2*pi*l))*(log((2*(l**2))/(r*p)) - 2 + (2*p)/l - (p/l)**2 + (1/2)*((p/l)**4))

def doisCondutoresAngReto(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = tamanho de cada segmento retilíneo a partir da conexão[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(2*pi*l))*(log((l**2)/(2*r*p)) - 0.2373 + 0.8584*(p/l) + 1.656*((p/l)**2) - 10.85*((p/l)**4))

def estrela3Pontas(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = tamanho de cada segmento retilíneo a partir da conexão[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(3*pi*l))*(log((l**2)/(2*r*p)) + 1.077 - 0.836*p/l + 3.808*((p/l)**2) - 13.824*((p/l))**4)

def estrela4Pontas(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = tamanho de cada segmento retilíneo a partir da conexão[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(4*pi*l))*(log((l**2)/(2*r*p)) + 2.912 - 4.284*p/l + 10.32*((p/l)**2) - 37.12*((p/l)**4))

def estrela6Pontas(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = tamanho de cada segmento retilíneo a partir da conexão[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(6*pi*l))*(log((l**2)/(2*r*p)) + 6.851 - 12.512*p/l + 28.128*((p/l)**2) - 125.4*((p/l)**4))

def estrela8Pontas(pa, p, l, r):
	"""
	pa = resistividade aparente do solo[ohm*m]
	p = profundidade em que está enterrado o condutor[m]
	l = tamanho de cada segmento retilíneo a partir da conexão[m]
	r = raio equivalente do condutor[m]
	"""
	return (pa/(8*pi*l))*(log((l**2)/(2*r*p)) + 10.98 - 22.04*p/l + 52.16*((p/l)**2) - 299.52*((p/l)**4))

def mostraEquacao(eq = 'condutorUnico'):
	pa, p, l, r, log, pi = symbols('pa p l r log pi')

	print 'equacao ',

	if eq == 'condutorUnico' or eq == 0:

		print 'condutorUnico'
		#pprint((pa/(2*pi*l))*(log((2*(l**2))/(r*p)) - 2 + (2*p)/l - (p/l)**2 + (1/2)*((p/l)**4)))

	elif eq == 'doisCondutoresAngReto' or eq == 1:

		print 'doisCondutoresAngReto'
		#pprint((pa/(2*pi*l))*(log((l**2)/(2*r*p)) - 0.2373 + 0.8584*(p/l) + 1.656*((p/l)**2) - 10.85*((p/l)**4)))

	elif eq == 'estrela3Pontas' or eq == 2:

		print 'estrela3Pontas'
		#pprint((pa/(3*pi*l))*(log((l**2)/(2*r*p)) + 1.077 - 0.836*p/l + 3.808*((p/l)**2) - 13.824*((p/l))**4))

	elif eq == 'estrela4Pontas' or eq == 3:

		print 'estrela4Pontas'
		#pprint((pa/(4*pi*l))*(log((l**2)/(2*r*p)) + 2.912 - 4.284*p/l + 10.32*((p/l)**2) - 37.12*((p/l)**4)))

	elif eq == 'estrela6Pontas' or eq == 4:

		print 'estrela6Pontas'
		#pprint((pa/(6*pi*l))*(log((l**2)/(2*r*p)) + 6.851 - 12.512*p/l + 28.128*((p/l)**2) - 125.4*((p/l)**4)))

	elif eq == 'estrela8Pontas' or eq == 5:

		print 'estrela8Pontas'
		#pprint((pa/(8*pi*l))*(log((l**2)/(2*r*p)) + 10.98 - 22.04*p/l + 52.16*((p/l)**2) - 299.52*((p/l)**4)))

if __name__ == "__main__":
	print 'Testando as formulas para condutores enterrados horizontalmente'
	pa = 1000
	p = .6
	l = 60
	r = .006/2

	print '1 fio, ', condutorUnico(pa, p, l, r)
	print '2 fios em angulo reto, ', doisCondutoresAngReto(pa, p, l/2, r)
	print 'Estrela 3 pontas, ', estrela3Pontas(pa, p, l/3, r)
	print 'Estrela 4 pontas, ', estrela4Pontas(pa, p, l/4, r)
	print 'Estrela 6 pontas, ', estrela6Pontas(pa, p, l/6, r)
	print 'Estrela 8 pontas, ', estrela8Pontas(pa, p, l/8, r)

	for i in range(5):
		mostraEquacao(i)

	a = raw_input('[ENTER] para sair')
