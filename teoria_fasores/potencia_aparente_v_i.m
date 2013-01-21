% potência aparente entre dois fasores
% V = tensão
% I = corrente
function pa = potencia_aparente_v_i(V, I)
pa = (abs(V)*abs(I))/2;
