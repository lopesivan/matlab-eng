% Processo de carregamento do capacitor
% Felipe Bandeira
%
% Entrada:
% t = tempo (segundos)
% vs = tensão da fonte (volts)
% res = resistor (ohms)
% cap = capacitor (faraday)
%
% Exemplo:
% cap_proc_carga(1, 10, 1e6, 1e-6)

function saida = cap_proc_carga(t, vs, res, cap)

f = @(t) vs*(1-exp(-t/(res*cap)));

t1 = 0;
ind = 1; % indice para o vetor com os tempo
por = 0.25;
while ind < 4
   v1 = f(t1);
   % verifica qual o tempo em que a tensão atigem n%
   if v1 > vs*por
       tp(ind) = t1;
       ind = ind + 1;    % muda o indice
       por = por + 0.25; % aumenta a porcentagem em passos de 25%
   end
   t1 = t1 + 0.001;      % aumenta o tempo em passo de 1ms
end

% tensão em um determinado tempo
saida.v = f(t);       

% função em função apenas do tempo
saida.f = f;    

saida.t25 = tp(1); % tempo quando a tensão é 25% do total
saida.t50 = tp(2); % tempo quando a tensão é 50% do total
saida.t90 = tp(3); % tempo quando a tensão é 75% do total
