#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

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

