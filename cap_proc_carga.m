% Processo de carregamento de um capacitor
% Felipe Bandeira
%
%      R
% ----/\/\----
% |          |
% + VS      --- C
% -         ---
% |          |
% ------------
%
% Entrada:
% t = tempo (segundos)
% vs = tens�o da fonte (volts)
% res = resistor (ohms)
% cap = capacitor (faraday)
%
% Exemplo:
% cap_proc_carga(1, 10, 1e6, 1e-6)

function saida = cap_proc_carga(t, vs, res, cap)

f = @(t) vs*(1-exp(-t/(res*cap)));

%% Busca as porcentagens em determinados tempos

f25 = @(t) vs*(1-exp(-t/(res*cap))) - vs*0.25;
f50 = @(t) vs*(1-exp(-t/(res*cap))) - vs*0.50;
f95 = @(t) vs*(1-exp(-t/(res*cap))) - vs*0.95;

t25 = fzero(f25, 0);
t50 = fzero(f50, 0);
t95 = fzero(f95, 0);
%% Atualiza a sa�da
saida.v = f(t);  % tens�o em um determinado instante
saida.f = f;     % f em fun��o apenas do tempo

saida.t25 = t25; % tempo quando a tens�o esta 25% do total(vs)
saida.t50 = t50; % tempo quando a tens�o esta 50% do total(vs)
saida.t95 = t95; % tempo quando a tens�o esta 95% do total(vs)
