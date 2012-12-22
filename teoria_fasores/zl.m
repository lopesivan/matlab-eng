% Impedância do indutor
% entrada:
% c = indutância
% w = frequência angular
% saida:
% z = impedância
function z = zl(l, w)

z = 1i*w*l;
