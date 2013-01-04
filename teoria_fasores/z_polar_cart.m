% converte um número na forma polar para a forma cartesiana
% entrada:
% raio do número
% ângulo do número em radianos
% saida:
% número complexo completo

function z_cart = z_polar_cart(raio, angulo)

x = raio*cos(angulo);
y = raio*sin(angulo);

z_cart = x+y*1i;
