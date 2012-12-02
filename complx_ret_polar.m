% Felipe Bandeira, Fortaleza-CE, 01/12/2012
% convers�o de um numero complexo da forma retangular para a forma polar
%
% entrada:
% x - parte real
% y - parte imaginaria
%
% saida:
% r - modulo
% theta - �ngulo em graus

function saida = complx_ret_polar(x, y)

z = x+1i*y; % 1i = j = i

r = abs(z);

theta = radtodeg(angle(z)); % �ngulo em graus

saida.r = r;
saida.theta = theta;