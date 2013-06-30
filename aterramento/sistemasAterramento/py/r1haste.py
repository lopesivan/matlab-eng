# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from __future__ import division
from math import pi, log
from sympy import symbols, pprint

def r1haste(pa, l, d):
	"""
	Entrada:
	pa = resistividade aparente do solo
	l = comprimento da haste
	d = diametro da haste

	Saída:
	resistencia de uma unica haste
	"""

	return pa/(2*pi*l) * log(4*l/d)

def mostraEquacao():
	pa, l, d, log, pi = symbols('pa l d log pi')
	pprint(pa/(2*pi*l) * log(4*l/d))


if __name__ == '__main__':
	
	try:
		pa = input('resistividade(ohm*m): ')
		l = input('comprimento(m): ')
		d = input('diametro da haste(m): ')		
	except Exception, e:
		pa = 1e3
		l = 32
		d = 0.015
	else:
		pass
	finally:
		pass


	r = r1haste(pa, l, d)

	print 'resistencia: ', r

	saida = raw_input('ENTER] para sair')

