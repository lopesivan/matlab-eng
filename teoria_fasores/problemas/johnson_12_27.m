% Problema Johnson 
% 12.27 Calcule o fator de pot�ncia visto pelos terminais da fonte e a
% reat�ncia necess�ria a ser conectada em paralelo com a fonte para mudar o
% fator de pot�ncia para a unidade.

% Imped�ncia vista pela fonte
zth = 3+4j;
% tens�o da fonte
vrms = 10/sqrt(2);
% fator de pot�ncia da carga
fp = cos(angle(zth));
% frequ�ncia da fonte
freq = 8/(2*pi);
% Pot�ncia ativa da carga
carga = potencia_carga_tensao(vrms, zth);

correcao_fp_via_potencia(vrms, freq, 1, real(carga.complexa), fp)
