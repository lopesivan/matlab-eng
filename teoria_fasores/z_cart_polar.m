% converte um n�mero complexo da forma cartesiana para a forma polar
% entrada: 
% - z = n�mero complexo completo, z = a+b*i
% ou
% - z = parte real
% - y = parte imaginaria
% sa�da:
% - num.raio = raio ou m�dulo
% - num.�ngulo = angulo do numero(radianos)

function num = z_cart_polar(z, y)

%raio = abs(x^2+y^2);
%angulo = atan(y/x);

if nargin == 2
    z = z+y*1i;
end
    
raio = abs(z);
angulo = angle(z);

num.raio = raio;
num.angulo = angulo;
