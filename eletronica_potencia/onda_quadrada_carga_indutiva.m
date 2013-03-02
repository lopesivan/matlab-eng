% Introdu��o ao estudo dos conversores CC-CA, Ivo Barbi
% capitulo 1:
% O conversor CC-CA da fig 1.9, apresenta os seguintes dados: L=200mH,
% E=300V. Considerando que a freq��ncia de sa�da seja 50Hz, determine o:
% a) Tempo de condu��o de cada chave controlada e cada diodo
% b) Valor m�ximo de tens�o e corrente na carga
% c) Valor m�ximo de tens�o e corrente na chave S1
function subterfugio = onda_quadrada_carga_indutiva(indutor, tensao_barramento, frequencia)

% para uma carga puramente indutiva, o tempo de condu��o de cada chave
% controlada � iqual ao tempo de condu��o de cada diodo, dado por T/4.
% Assim:
Tscond = 1/(4*frequencia);

% a tens�o m�ximo na carga � obtida quando S1, S4 ou S2, S3 conduzem.
% Assim:
Vomax = tensao_barramento;

% considerando a carga puramente indutiva e que o tempo de condu��o de cada
% chave controlada � de T/4
Iomax = tensao_barramento/(4*indutor*frequencia);

% o valor m�ximo de tens�o nos terminais da chave S1 ocorre quando S3 ou D3
% est�o em condu��o. Logo:
Vs1_max = tensao_barramento;

% o valor m�ximo de corrente na chave S1 � o mesmo valor m�ximo de corrente
% na carga. Desse modo:
Is1_max = Iomax;

%% sa�da

subterfugio.Tscond = Tscond;
subterfugio.Vomax = Vomax;
subterfugio.Iomax = Iomax;
subterfugio.Vs1_max = Vs1_max;
subterfugio.Is1_max = Is1_max;
