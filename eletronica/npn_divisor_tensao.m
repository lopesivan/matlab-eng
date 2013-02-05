% divisor de tensão clássico
% entrada:
% R1 - resistor superior do divisor de tensão
% R2 - resistor inferior do divisor de tensão
% RC - resistor do coletor
% RE - resistor do emissor
% VCC - tensão de alimentação

function subterfugio = npn_divisor_tensao(R1, R2, RC, RE, VCC)

% constantes
VBE = 0.7;

% corrente na base
I = VCC/(R1+R2);
% valor considerado pequeno
IBp = I/20;
% tensão na base
VB = R2*I;
% tensão no emissor
VE = VB - VBE;
% corrente no emissor
IE = VE/RE;
% tensão no coletor
IC = IE;
VC = VCC - IC*RC;
% tensão coletor-emissor
VCE = VC - VE;
% ganho de corrente de entrada(base) e corrente saída(coletor)
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
