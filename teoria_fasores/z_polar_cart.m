% converte um n�mero na forma polar para a forma cartesiana
function z_cart = z_polar_cart(raio, angulo)

x = raio*cos(angulo);
y = raio*sin(angulo);

z_cart = x+y*1i;
