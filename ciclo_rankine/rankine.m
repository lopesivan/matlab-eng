% Ciclo de Rankine simples
% Felipe Bandeira
%
% entrada:
% pa - pressão alta  (saida da caldeira)
% pb - pressão baixa (condensador)
function saida = rankine(pa, pb)

if nargin ~= 2, saida = NaN; return, end

%% conversão MPa -> bar
pa_bar = pa*10;
pb_bar = pb*10;
%% liquido saturado
h1 = XSteam('hL_p', pb_bar);     % entalpia
t1 = XSteam('T_ph', pb_bar, h1); % temperatura
s1 = XSteam('sL_p', pb_bar);     % entropia
v1 = XSteam('vL_p', pb_bar);     % volume

h3 = XSteam('hV_p', pa_bar);     % vapor saturado na parte 3
s3 = XSteam('sV_p', pa_bar);     % entropia do vapor saturado
%% trabalho na bomba
wb = v1 * (pa*1000 - pb*1000);   % kJ/kg
h2 = h1 + abs(wb);
%% calor na caldeira
qh = h3 - h2;
%% turbina
sv = XSteam('sV_p', pb_bar);
x4 = (s1 - s3)/(s1 - sv);
hv = XSteam('hV_p', pb_bar);
h4 = (1-x4) * h1 + x4 * hv;
wt = h3 - h4;                    % trabalho na turbina
%% condensador
ql = h4 - h1;
%% rendimento
nr = (wt - wb)/qh;
nrp = nr * 100;
%% mensagens

fprintf('--------------------------------------------------\n');
fprintf('Ciclo de Rankine simples\n');
fprintf('trabalho total da turbina = %0.5f kJ/kg\n', wt);
fprintf('trabalho da bomba = %0.5f kJ/kg\n', wb);
fprintf('calor da caldeira = %0.5f kJ/kg\n', qh);
fprintf('rendimento = %0.5f %%\n', nrp);
fprintf('--------------------------------------------------\n');

%% saida
saida = nr;