% divisor de tens�o cl�ssico
% entrada:
% R1 - resistor superior do divisor de tens�o
% R2 - resistor inferior do divisor de tens�o
% RC - resistor do coletor
% RE - resistor do emissor
% VCC - tens�o de alimenta��o

function subterfugio = npn_divisor_tensao(R1, R2, RC, RE, VCC)

% constantes
VBE = 0.7;

% corrente na base
I = VCC/(R1+R2);
% valor considerado pequeno
IBp = I/20;
% tens�o na base
VB = R2*I;
% tens�o no emissor
VE = VB - VBE;
% corrente no emissor
IE = VE/RE;
% tens�o no coletor
IC = IE;
VC = VCC - IC*RC;
% tens�o coletor-emissor
VCE = VC - VE;
% ganho de corrente de entrada(base) e corrente sa�da(coletor)
ganho = IC/I;

subterfugio.I = I;
subterfugio.IBp = IBp;
subterfugio.VB = VB;
subterfugio.VE = VE;
subterfugio.IE = IE;
subterfugio.IC = IC;
subterfugio.VC = VC;
subterfugio.VCE = VCE;
subterfugio.ganho = ganho;
