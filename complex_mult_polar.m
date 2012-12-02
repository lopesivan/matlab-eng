% Multiplicação de 2 números complexos na forma polar
% z = z1*z2
%
% Felipe Bandeira, Fortaleza-CE, 01/12/2012
%
%
% entrada:
% r1 - modulo do número 1
% t1 - ângulo do número 1
% r2 - modulo do número 2
% t2 - ângulo do número 2
%
% saida:
% r - modulo final
% theta - ângulo final

function res = complex_mult_polar(r1, t1, r2, t2)

if nargin ~= 4
    disp('erro: argumentos');
    return;
end

r = r1*r2;
theta = t1+t2;

res.r = r;
res.theta = theta;