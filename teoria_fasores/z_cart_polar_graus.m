% converte um número complexo na forma retangular para a forma polar
% entrada:
% - z = número complexo, a+b*i
% ou
% - z = raio
% - ang = ângulo
% saida:
% - raio
% - ângulo

function num = z_cart_polar_graus(z, ang)

if nargin == 1
    raio = abs(z);
    angulo = radtodeg(angle(z));
elseif nargin == 2
    raio = z;
    angulo = ang;
end

num.raio = raio;
num.angulo = angulo;
