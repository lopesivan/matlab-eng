% Conversão D -> Y
% 
% seja a rede Y e D:
% a ------ Zc ------- b
% |                   |
% |-- Z1 --n---- Z2 --|
% |        |          |
% Zb      Z3          Za
% |        |          |
% |------- c ---------|

function subterfugio = conversao_d_y(za, zb, zc)

a = za+zb+zc;

z1 = (zb*zc)/a;
z2 = (zc*za)/a;
z3 = (za*zb)/a;

subterfugio.z1 = z1;
subterfugio.z2 = z2;
subterfugio.z3 = z3;
