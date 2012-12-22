% converte um n�mero complexo da forma cartesiana para a forma polar
% entrada: 
% x = parte real
% y = parte imaginaria
% sa�da:
% num.raio = raio ou m�dulo
% num.�ngulo = angulo do numero(radianos)
function num = z_cart_polar(x, y)

raio = abs(x^2+y^2);
angulo = atan(y/x);

num.raio = raio;
num.angulo = angulo;
