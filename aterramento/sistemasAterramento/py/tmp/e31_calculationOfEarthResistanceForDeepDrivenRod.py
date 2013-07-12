from scipy.integrate import quad
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

def Hs(hs): sum(hs)

def eqTakahashiKawase():
	l = 30
	r = .007
	p1 = 1
	p2 = 100
	a = .03
	
	pass

if __name__ == '__main__':

	exemploMathWorks()