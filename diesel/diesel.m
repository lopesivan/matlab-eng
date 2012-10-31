% Ciclo Diesel
% Felipe Bandeira
%
% Entrada:
% p1(MPa) - press�o no processo de compress�o
% t1(�C) - temperatura no processo de compress�o
% qh(kJ/kg) - calor transferido
% r - rela��o de compress�o
%
% Exemplo 9.12
% Um ciclo-padr�o de ar Diesel apresenta rela��o de compress�o iqual a 18 e
% o calor transferido ao fluido de trabalho, por ciclo, � 1800 kJ/kg. 
% Sabendo que no inicio do processo de compress�o, a press�o � iqual a 
% 0.1 MPa e a temperatura � de 15�C, determine:
% 1. a press�o e temperatura em cada ponto do ciclo
% 2. o rendimento t�rmico
% 3. a press�o m�dia efetiva

function saida = diesel(p1, t1, qh, r)

% constantes tabeladas
k = 1.4;
Rg = .287;
cp = 1.0035;
cv = .7165;

% convers�o para Kelvin
t1 = t1+273.15;

v1 = Rg*t1/(p1*1000); % m^3/kg

v2 = v1/18; % m^3/kg

t2 = t1*r^(k-1); % K

p2 = p1*r^k; % MPa

t3 = qh/cp + t2; % K

v3 = v2*t3/t2; % m^3/kg

t4 = inv(1/t3*(v1/v3)^(k-1)); % K

ql = abs(cv*(t1-t4)); % kJ/kg

wlig = qh - ql; % kJ/kg

n = wlig/qh; 

pme = wlig/(v1-v2); % kPa

fprintf('v1= %0.4f\n', v1);
fprintf('v2= %0.4f\n', v2);
fprintf('t2= %0.4f\n', t2);
fprintf('p2= %0.4f\n', p2);
fprintf('t3= %0.4f\n', t3);
fprintf('v3= %0.4f\n', v3);
fprintf('t4= %0.4f\n', t4);
fprintf('ql= %0.4f\n', ql);
fprintf('n= %0.4f\n', n);
fprintf('pme= %0.4f\n', pme);
