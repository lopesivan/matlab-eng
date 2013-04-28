% Problema Johnson 
% 12.27 Calcule o fator de potência visto pelos terminais da fonte e a
% reatância necessária a ser conectada em paralelo com a fonte para mudar o
% fator de potência para a unidade.

% Impedância vista pela fonte
zth = 3+4j;
% tensão da fonte
vrms = 10/sqrt(2);
% fator de potência da carga
fp = cos(angle(zth));
% frequência da fonte
freq = 8/(2*pi);
% Potência ativa da carga
carga = potencia_carga_tensao(vrms, zth);

correcao_fp_via_potencia(vrms, freq, 1, real(carga.complexa), fp)
