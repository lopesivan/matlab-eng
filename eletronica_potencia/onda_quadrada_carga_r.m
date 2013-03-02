% Introdu��o ao estudo dos conversores CC-CA, Ivo Barbi
% capitulo 1:
% Seja o circuito da Fig1.5, onde R=15 Ohms, E=30 V, f=50 Hz. Determine o:
% a) Valor m�ximo de tens�o e corrente na carga
% b) Valor m�ximo de tens�o e corrente na chave S1
% c) Tempo de condu��o das chaves controladas
function subterfugio = onda_quadrada_carga_r(resistencia_carga, tensao_barramento, frequencia)

% para o item a
% O valor m�ximo da tens�o na carga pe obtido quando as chaves S1, S4 ou
% S2, S3 est�o em condu��o, logo:
Vrmax = tensao_barramento;
Irmax = Vrmax/resistencia_carga;

% para o item b
% A tens�o m�xima na chave S1 ocorre quando S3 est� em condu��o.
Vs1_max = Vrmax;
Is1_max = Vs1_max / resistencia_carga;

% para o item c
% cada chave conduz por um espa�o de tempo iqual a T/2. Ent�o:
Tcond = 1/(2*frequencia);

% sa�da
subterfugio.Vrmax = Vrmax;
subterfugio.Irmax = Irmax;
subterfugio.Vs1_max = Vs1_max;
subterfugio.Is1_max = Is1_max;
subterfugio.Tcond = Tcond;

