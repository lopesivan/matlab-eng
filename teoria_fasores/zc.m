% Impedância do capacitor
% entrada:
% - c = capacitância
% - w = frequência angular
% saída:
% - z = impedância
function z = zc(c, w)

z = 1/(1i*w*c);
