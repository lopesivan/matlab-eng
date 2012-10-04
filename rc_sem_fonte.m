% Processo de descarga de um capacitor
% Felipe Bandeira
% 
%      R
% |---\/\/---|
% |         --- C
% |         ---
% |----------|
%
% Entrada:
% t = tempo
% vo = tensão inicial
% res = resistência vista pelo capacitor
% cap = capacitância
%
% Exemplo:
% rc_sem_fonte(1, 10, 10e3, 1e-6)

function saida = rc_sem_fonte(t, vo, res, cap)

f = @(t) vo*exp(-t/(res*cap));

% constante de tempo
c1 = res*cap;
c2 = 2*c1;
c3 = 3*c1;

% tensão em um instante de tempo
saida.v = f(t);

% f em função apenas do tempo
saida.f = f;

saida.c1 = c1; % tempo quando a tensão atinge 36.79% do total
saida.c2 = c2; % tempo quando a tensão atinge 13.53% do total
saida.c3 = c3; % tempo quando a tensão atinge 04.98% do total
