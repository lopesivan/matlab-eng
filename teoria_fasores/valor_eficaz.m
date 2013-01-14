% valor eficaz ou rms de uma onda períodica
% onde:
% função períodica depedente do tempo t e um período.
% exemplo:
% > syms t; f = 10*cos(t); valor_eficaz(f, 2*pi)
function eficaz = valor_eficaz(funcao, periodo)
syms t; 
eficaz = sqrt(1/periodo * int(funcao^2, t, 0, periodo));
