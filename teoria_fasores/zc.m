% Imped�ncia do capacitor
% entrada:
% - c = capacit�ncia
% - w = frequ�ncia angular
% sa�da:
% - z = imped�ncia
function z = zc(c, w)

z = 1/(1i*w*c);
