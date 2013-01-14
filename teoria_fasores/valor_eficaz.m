% valor eficaz ou rms de uma onda per�odica
% onde:
% fun��o per�odica depedente do tempo t e um per�odo.
% exemplo:
% > syms t; f = 10*cos(t); valor_eficaz(f, 2*pi)
function eficaz = valor_eficaz(funcao, periodo)
syms t; 
eficaz = sqrt(1/periodo * int(funcao^2, t, 0, periodo));
