% Circuito RL sem fonte(processo de descarga)
% Felipe Bandeira
%
% Entrada:
% t = tempo (Segundos)
% io = corrente inicial (Amperes)
% res = resistência vista pelo indutor (Ohms)
% ind = indutância (Henry)
%
% Exemplo:
% rl_sem_fonte(0, 1, 100e3, 1)

function saida = rl_sem_fonte(t, io, res, ind)

% cria a função
f = @(t) io*exp(-(res*t)/ind);

% calculo das constantes de tempo
c1 = ind/res;
c2 = 2*c1;
c3 = 3*c1;

% plotagem
% ezplot(f, [0, c3]);

%% f em função do tempo
saida.f = f;

% corrente i em um instante
saida.i = f(t);

saida.c1 = c1; % tempo quando a tensão atinge 36.79% do total
saida.c2 = c2; % tempo quando a tensão atinge 13.53% do total
saida.c3 = c3; % tempo quando a tensão atinge 04.98% do total
