% Imped�ncia do indutor
% entrada:
% - c = indut�ncia
% - w = frequ�ncia angular
% sa�da:
% - z = imped�ncia
function z = zl(l, w)

z = 1i*w*l;
