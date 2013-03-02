% Introdução ao estudo dos conversores CC-CA, Ivo Barbi
% capitulo 1:
% Seja o circuito da Fig1.5, onde R=15 Ohms, E=30 V, f=50 Hz. Determine o:
% a) Valor máximo de tensão e corrente na carga
% b) Valor máximo de tensão e corrente na chave S1
% c) Tempo de condução das chaves controladas
function subterfugio = onda_quadrada_carga_r(resistencia_carga, tensao_barramento, frequencia)

% para o item a
% O valor máximo da tensão na carga pe obtido quando as chaves S1, S4 ou
% S2, S3 estão em condução, logo:
Vrmax = tensao_barramento;
Irmax = Vrmax/resistencia_carga;

% para o item b
% A tensão máxima na chave S1 ocorre quando S3 está em condução.
Vs1_max = Vrmax;
Is1_max = Vs1_max / resistencia_carga;

% para o item c
% cada chave conduz por um espaço de tempo iqual a T/2. Então:
Tcond = 1/(2*frequencia);

% saída
subterfugio.Vrmax = Vrmax;
subterfugio.Irmax = Irmax;
subterfugio.Vs1_max = Vs1_max;
subterfugio.Is1_max = Is1_max;
subterfugio.Tcond = Tcond;

