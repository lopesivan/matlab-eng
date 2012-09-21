% Divisor de corrente
% |----V----|
% R1       R2
% |---------|

function saida = div_corrente(i, r1, r2)

ir1 = i * r2 / (r1+r2);
ir2 = i * r1 / (r1+r2);
v = i * (r1 * r2)/(r1 + r2);

saida.ir1 = ir1;
saida.ir2 = ir2;
saida.v = v;
