% pot�ncia m�dia entre dois fasores
% V = tens�o
% I = corrente
function pm = potencia_media_v_i(V, I)
pm = 0.5*abs(V)*abs(I)*cos(angle(V) - angle(I));
