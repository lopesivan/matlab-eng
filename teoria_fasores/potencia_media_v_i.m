% potência média entre dois fasores
% V = tensão
% I = corrente
function pm = potencia_media_v_i(V, I)
pm = 0.5*abs(V)*abs(I)*cos(angle(V) - angle(I));
