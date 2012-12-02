% Felipe Bandeira, Fortaleza-CE, 01/12/2012
% conversão de um numero complexo da forma retangular para a forma polar
%
% entrada:
% x - parte real
% y - parte imaginaria
%
% saida:
% r - modulo
% theta - ângulo em graus

function saida = complx_ret_polar(x, y)

z = x+1i*y; % 1i = j = i

r = abs(z);

theta = radtodeg(angle(z)); % ângulo em graus

saida.r = r;
saida.theta = theta;