from scipy.integrate import quad, romberg
from scipy.special import jn
from numpy import arange
import matplotlib.pyplot as plt
from math import pi

def exemploMathWorks(grafico = False):
	passo = .2
	z = arange(0, 1+passo, passo)
	j = jn(1, z)

	print z
	print j

	if grafico:
		plt.plot(z, j)
		plt.grid(True)
		plt.show()

def Hs(h): 
	sum(h)

def HN1(h):
	s = 0
	for i in range(len(h)-1):
		s+=h[i]
	return s

def pN(p):
	return p[len(p)-1]

def k(pm, pn1):
	return (pn1-pn)/(pn1+pn)

def eqTakahashiKawase():
	l = 30
	r = .007
	p1 = 1
	p2 = 100
	a = .03
	N = 2

	s = 2

	h = [1, 1]
	p = [p1, p2]kk

	ac = 0
	for i in range(0, N):
		ac += h[i]/p[i]

	ac += 1/((k-HN1(h))/pN(p)) # fim da parte A

	for s in range(1, N+1):
		for i in range(0, s-1):
			(1-k(p[i], p[i+1]))*romberg(quad(), H, Hs(h))


	

if __name__ == '__main__':

	exemploMathWorks()
	eqTakahashiKawase()
