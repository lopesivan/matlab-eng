% conversão de um numero complexo da forma retangular para a forma polar
%
% Felipe Bandeira, Fortaleza-CE, 01/12/2012
%
%
% entrada:
% x - parte real
% y - parte imaginaria
%
% saída:
% r - modulo
% theta - ângulo em graus

function saida = complex_ret_polar(x, y)

if nargin ~= 2
    disp('erro: argumentos');
    return;
end

z = x+1i*y; % 1i = j = i

r = abs(z);

theta = radtodeg(angle(z)); % ângulo em graus

saida.r = r;
saida.theta = theta;
