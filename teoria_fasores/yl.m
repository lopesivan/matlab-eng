% Admitância do indutor
% entrada:
% - c = indutância
% - w = frequência angular
% saída:
% - z = admitância
function Y = yl(l, w)

Y = 1/zl(l, w);

