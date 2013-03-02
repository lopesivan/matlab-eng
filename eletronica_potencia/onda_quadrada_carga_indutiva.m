% Introdução ao estudo dos conversores CC-CA, Ivo Barbi
% capitulo 1:
% O conversor CC-CA da fig 1.9, apresenta os seguintes dados: L=200mH,
% E=300V. Considerando que a freqüência de saída seja 50Hz, determine o:
% a) Tempo de condução de cada chave controlada e cada diodo
% b) Valor máximo de tensão e corrente na carga
% c) Valor máximo de tensão e corrente na chave S1
function subterfugio = onda_quadrada_carga_indutiva(indutor, tensao_barramento, frequencia)

% para uma carga puramente indutiva, o tempo de condução de cada chave
% controlada é iqual ao tempo de condução de cada diodo, dado por T/4.
% Assim:
Tscond = 1/(4*frequencia);

% a tensão máximo na carga é obtida quando S1, S4 ou S2, S3 conduzem.
% Assim:
Vomax = tensao_barramento;

% considerando a carga puramente indutiva e que o tempo de condução de cada
% chave controlada é de T/4
Iomax = tensao_barramento/(4*indutor*frequencia);

% o valor máximo de tensão nos terminais da chave S1 ocorre quando S3 ou D3
% estão em condução. Logo:
Vs1_max = tensao_barramento;

% o valor máximo de corrente na chave S1 é o mesmo valor máximo de corrente
% na carga. Desse modo:
Is1_max = Iomax;

%% saída

subterfugio.Tscond = Tscond;
subterfugio.Vomax = Vomax;
subterfugio.Iomax = Iomax;
subterfugio.Vs1_max = Vs1_max;
subterfugio.Is1_max = Is1_max;
