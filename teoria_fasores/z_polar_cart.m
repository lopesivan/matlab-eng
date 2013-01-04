% converte um n�mero na forma polar para a forma cartesiana
% entrada:
% raio do n�mero
% �ngulo do n�mero em radianos
% saida:
% n�mero complexo completo

function z_cart = z_polar_cart(raio, angulo)

x = raio*cos(angulo);
y = raio*sin(angulo);

z_cart = x+y*1i;
