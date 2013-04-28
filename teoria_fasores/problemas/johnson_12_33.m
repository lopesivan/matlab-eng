% Problema Johnson
% 12.33 Uma carga � alimentada da pot�ncia complea S = 6+8j VA por uma
% fonte de tens�o de 10cos(100t) V. Calcule a capacit�ncia que deve ser
% conectada em paralelo com a carga para que o fator de pot�ncia visto pela
% fonte seja (a) unit�rio e (b) 0.8 (atrasado)

% para o item (a)
vrms = 10/sqrt(2);
carga = 6+8j;
fp = cos(angle(carga));
freq = 100/(2*pi);

disp('item a');
correcao_fp_via_potencia(vrms, freq, 1, real(carga), fp)

% para o item (b)
disp('item b');
correcao_fp_via_potencia(vrms, freq, .8, real(carga), fp)