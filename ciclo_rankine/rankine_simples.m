% Ciclo simples de rankine
%
% Felipe Bandeira, felipeband18@gmail.com
%
% entrada:
% - palta = pressao alta, em MPa
% - pbaixa = pressao baixa, em MPa
function saida = rankine_simples(palta, pbaixa)

if nargin ~= 2, saida = NaN; return, end

fprintf('--------------------------------------------------\n');

fprintf('\nciclo simples de rankine\n\n');

% conversao MPa -> bar
palta_bar = palta*10;
pbaixa_bar = pbaixa*10;

fprintf('pressões de entrada:\n');
fprintf('alta: %d MPa= %d bar\n', palta, palta_bar);
fprintf('baixa: %d MPa= %d bar\n', pbaixa, pbaixa_bar);

% liquido saturado
% calculo da entalpia
h1 = XSteam('hL_p', pbaixa_bar);
% calculo da temperatura do liquido saturado
t1 = XSteam('T_ph', pbaixa_bar, h1);
% calculo da entropia
s1 = XSteam('sL_p', pbaixa_bar);
% volume
v1 = XSteam('vL_p', pbaixa_bar);

% vapor saturado na parte 3
h3 = XSteam('hV_p', palta_bar);

% entropia para o vapor saturado
s3 = XSteam('sV_p', palta_bar);


fprintf('\nvolume de controle da bomba:\n');
fprintf('considerações:\n');
fprintf('estado de entrada: p1 conhecida, líquido saturado, estado determinado\n');
fprintf('estado de saida: p2 conhecida\n');

fprintf('\n--------------------------------------------------\n');

fprintf('\nh1 = %d\n', h1);
fprintf('t1 = %d\n', t1);
fprintf('s1 = %d\n', s1);
fprintf('v1 = %d\n', v1);

fprintf('\n--------------------------------------------------\n');

fprintf('\nadmitindo que o liquido seja incompressivel.\n\n');

% calculo do trabalho da bomba, em kJ/kg
wb = v1*(palta - pbaixa);
% h2
h2 = h1 + wb;

fprintf('trabalho da bomba: %d\n', wb);
fprintf('h2: %d\n', h2);

fprintf('\n--------------------------------------------------\n');

fprintf('\np2, h2 conhecidas, estado determinado\n');
fprintf('p3 conhecidas, vapor saturado, estado determinado\n');

% calor da caldeira
qh = h3 - h2;

fprintf('\nh3 = %d\n', h3);
fprintf('qh = %d\n', qh);

fprintf('\n--------------------------------------------------\n');

fprintf('\nestado 3 conhecido\n');
fprintf('p4 conhecida\n');

% calculos da turbina

sv = XSteam('sV_p', pbaixa_bar); 

x4 = (s1 - s3)/(s1 - sv);

hv = XSteam('hV_p', pbaixa_bar);

h4 = (1-x4)*h1+x4*hv;

% trabalho da turbina
wt = h3 - h4;

fprintf('\nx4 = %d\n', x4);
fprintf('h4 = %d\n', h4);
fprintf('wt = %d\n', wt);


fprintf('\n--------------------------------------------------\n');

% calculo do condensador
fprintf('\ncondensador\n');

ql = h4 - h1;

fprintf('\nql = %d\n', ql);

fprintf('\n--------------------------------------------------\n');

% calculos do rendimento

nr = (wt - wb)/qh;

fprintf('\nrendimento do ciclo: %d\n', nr);


% saida

saida.h1 = h1;
saida.t1 = t1;
saida.s1 = s1;
saida.v1 = v1;

saida.h2 = h2;

saida.h3 = h3;
saida.s3 = s3;

saida.h4 = h4;
saida.x4 = x4;

saida.wb = wb;
saida.wt = wt;

saida.qh = qh;
saida.ql = ql;

saida.sv = sv;
saida.hv = hv;

saida.nr = nr;
