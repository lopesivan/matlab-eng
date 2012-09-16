% Ciclo de Rankine reaquecido
% Felipe Bandeira
%
% entrada:
% p3 - alta pressão de entrada na turbina (ponto 3)
% t3 - pressão de entrada na turbina (ponto 3)
% p4 - pressão expandida no primeiro processo (ponto 4)
% t5 - temperatura na saida do aquecimento (ponto 5)
% p6 - pressão do condensador (ponto 6)
%
% exemplo 9.3, Fundamentos da Termodinâmica Clássica - Gordon, Richard...
% 4ª edição
%
% Enunciado do exemplo 9.3:
% Considere um ciclo com reaquecimento que utiliza água como fluido. O
% vapor deixa a caldeira e entra na turbina a 4MPa(p3) e 400ºC(t3). Após expansão
% na turbina até 400kPa(p4), o vapor é reaquecido até 400ºC(t5) e então expandido
% na turbina, de baixa pressão, até 10kPa(p6). Determine o rendimento do ciclo.
%
% exemplo:
% - rankine_reaquecido(4, 400, 0.4, 400, 0.010)
function saida = rankine_reaquecido(p3, t3, p4, t5, p6)
% calculos da turbina de alta pressão
% conversão MPa para bar
p3_bar = p3*10;
p4_bar = p4*10;
p6_bar = p6*10;

h3 = XSteam('h_pT', p3_bar, t3);
s3 = XSteam('s_pT', p3_bar, t3);

% calculando o titulo x4

s4e = XSteam('sL_p', p4_bar);
s4v = XSteam('sV_p', p4_bar);

h4e = XSteam('hL_p', p4_bar);
h4v = XSteam('hV_p', p4_bar);

x4 = - (s3 - s4e)/(s4e - s4v);
h4 = (1 - x4) * h4e + x4 * h4v;
%% calculos da turbina de baixa pressão
% nesse ponto p5 = p4
p5_bar = p4_bar;

h5 = XSteam('h_pT', p5_bar, t5);
s5 = XSteam('s_pT', p5_bar, t5);
%% para o calculo do titulo
s6e = XSteam('sL_p', p6_bar); % liquido saturado
s6v = XSteam('sV_p', p6_bar); % vapor saturado

h6e = XSteam('hL_p', p6_bar); % liquido saturado
h6v = XSteam('hV_p', p6_bar); % vapor saturado

% titulo x6 para o calculo de h6
x6 = - (s5 - s6e)/(s6e - s6v);
h6 = (1 - x6)*h6e + x6 * h6v;
%% trabalho total da turbina
wta = h3 - h4;
wtb = h5 - h6;
wt = wta + wtb;
%% calculo da bomba
% nesse ponto a pressão no condensador é iqual a p6
p1_bar = p6_bar;
p1 = p6;

v1 = XSteam('vL_p', p1_bar); % liquido saturado
h1 = XSteam('hL_p', p1_bar);

wb = v1*(p3*1000 - p1*1000); % kJ/kg
h2 = abs(wb) + h1;
%% caldeira
qh = (h3 - h2) + (h5 - h4);
%% rendimento
nr = (wt - wb)/qh;
nrp = nr*100;
%% mensagens

fprintf('--------------------------------------------------\n');

fprintf('Ciclo de Rankine com reaquecimento\n\n');

fprintf('trabalho da turbina de alta potencia = %0.5f kJ/kg\n', wta);
fprintf('trabalho de turbina de baixa potencia = %0.5f kJ/kg\n', wtb);
fprintf('trabalho total da turbina = %0.5f kJ/kg\n', wt);
fprintf('trabalho da bomba = %0.5f kJ/kg', wb);
fprintf('trabalho da bomba = %0.5f kJ/kg\n', wb);
fprintf('calor da caldeira = %0.5f kJ/kg\n', qh);
fprintf('rendimento = %0.5f %%\n', nrp);

fprintf('--------------------------------------------------\n');

%% saida
saida.wta = wta; % trabalho turbina de alta potencia
saida.wtb = wtb; % trabalho turbina de baixa potencia
saida.wb = wb; % trabalho da bomba
saida.qh = qh; % calor da caldeira
saida.nrp = nrp; % rendimento em porcentos
