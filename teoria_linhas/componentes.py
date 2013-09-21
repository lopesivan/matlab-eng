# -*- coding: cp1252 -*-

from math import pi

# parametros da linha
z = 5.39+25.60*1j
y = 324.2e-6*1j
f = 60
# tensão e corrente no receptor
vr = 342.4e3-8.741e3*1j
ir = 200.0-47.60*1j

zr = vr/ir

print '----'
print 'Valores da carga,'
print 'Resistor [ohm]:', zr.real
print 'Reatancia [ohm]:', zr.imag

if zr.imag > 0:
	print 'Indutancia [henry]:', zr.imag/(2*pi*f)
elif zr.imag < 0:
	print 'Capacitancia [faraday]:', 1/(zr.imag*2*pi*f)

print '----'
print 'Valores para a linha,'
print 'Resistor [ohm]:', z.real
print 'Reatancia, indutiva [ohm]:', z.imag
print 'Supceptancia, capacitiva [mho]:', y.imag
print 'Indutancia [henry]:', z.imag/(2*pi*f)
zy = 1/y
print 'Capacitancia [faraday]:', 1/(abs(zy.imag)*2*pi*f)
