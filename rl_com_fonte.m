% Circuito RL com fonte
% Felipe Bandeira
%
% Entrada:
% t = tempo (Segundos)
% io = corrente inicial (Amperes)
% vs = tensão de alimentação (Volts)
% r = resistência vista por L (Ohms)
% l = indutância (Henrys)

function saida = rl_com_fonte(t, io, vs, r, l)
% para t > 0
f = @(t) (vs/r)+(io-(vs/r))*exp(-t/(l/r));

% corrente no regime permanente
rp = vs/r;

%% Busca os tempos para cada porcentagem

% função para 25% da corrente total
f25 = @(t) (vs/r)+(io-(vs/r))*exp(-t/(l/r)) - rp*0.25;
% função para 50% da corrente total
f50 = @(t) (vs/r)+(io-(vs/r))*exp(-t/(l/r)) - rp*0.50;
% função para 95% da corrente total
f95 = @(t) (vs/r)+(io-(vs/r))*exp(-t/(l/r)) - rp*0.95;

t25 = fzero(f25, [0, rp]); % define o intervalo de busca
t50 = fzero(f50, [0, rp]);
t95 = fzero(f95, [0, rp]);

%% Atualiza a saida

saida.i = f(t);
saida.f = f;

saida.t25 = t25;
saida.t50 = t50;
saida.t95 = t95;
