% Converte um n�mero na forma polar para a forma retangular.
% Entrada:
% - raio
% - �ngulo ( em graus )
% Sa�da:
% n�mero complexo na forma retangular
function z_cart = z_polar_graus_cart(raio, angulo)

x = raio*cosd(angulo);
y = raio*sind(angulo);

z_cart = x+y*1i;
