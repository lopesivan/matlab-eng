function subterfugio = amplificador_ac_divisor_tensao (R1, R2, RC, RE, VCC, RG, frequencia_base, tensao_max_sinal)

dados = npn_divisor_tensao(R1, R2, RC, RE, VCC);

% resitência vista pelo capacitor
rth_cap = paralelos([R1, R2]) + RG;

% cálculo do capacitor de acoplamento para 
% freqüência de quina(frequencia base) usando a regra do 1:10
C = 1/(2*pi*rth_cap*frequencia_base*(1/10));

% resitência do emissor
re = dados.IE

subterfugio.C = C;

