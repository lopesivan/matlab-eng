% Admitância do capacitor
% entrada:
% c = capacitância
% w = frequência angular
% saida:
% z = admitância
function Y = yc(c, w)

Y = 1/zc(c, w);
