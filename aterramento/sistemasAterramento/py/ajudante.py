#!/usr/bin/env python

from platform import system

def osAtual():
	return system

def separador():
	if system() == 'Linux':
		return '/'
	else:
		return '\\'

def cmdLimpaTela():
	if system() == 'Linux':
		return 'clear'
	else:
		return 'cls'

