% Divisor de tensão
% ------
% |    R1
% V    |
% |    R2
% ------

function saida = div_tensao(v, r1, r2)

i = v/(r1+r2);
vr1 = i * r1;
vr2 = i * r2;

saida.i = i;
saida.vr1 = vr1;
saida.vr2 = vr2;
