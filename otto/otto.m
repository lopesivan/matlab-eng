% Ciclo Otto
% Felipe Bandeira
%
% entrada:
% p1(MPa) - press�o de entrada
% t1(�C) - temperatura na compress�o
% qh(kJ/kg) - transfer�ncia de calor
% r - rela��o de compressao
%
% Exemplo 9.11
% A rela��o de compress�o num ciclo a ar Otto � de 8. No inicio do curso
% compress�o a press�o � iqual a 0.1 MPa e a temperatura � de 15�C. 
% Sabendo que a transfer�ncia de calor ao ar por ciclo, � iqual a
% 1800 kJ/kg de ar, determine:
% 1. A press�o e a temperatura no estado final de cado processo do ciclo
% 2. O rendimento termico
% 3. A press�o m�dia efetiva
%
% otto(0.1, 15, 1800, 8)

function saida = otto(p1, t1, qh, r)

% constantes tabeladas
k = 1.4;
cv = .7165;

% convers�o para Kelvin
t1 = t1+273.15;

v1 = 0.287*t1/(p1*1000); % m^3/kg

t2 = t1*r^(k-1); % K

p2 = p1*r^k; % MPa

v2 = 0.287*t2/(p2*1000);

t3 = qh/cv + t2;

p3 = t3/t2*p2;

t4 = 1/(8^(k-1)/t3);

p4 = 1/(1/p3*8^k);

% calculo do rendimento
n = 1-1/r^(k-1);

% calculo do pme
q41 = abs(cv*(t1-t4));

n2 = 1-q41/qh; % segundo rendimento

wliq = qh-q41;

fprintf('v1= %0.5f\n', v1);
fprintf('p2= %0.5f\n', p2);
fprintf('t2= %0.5f\n', t2);
fprintf('v2= %0.5f\n', v2);
fprintf('n= %0.5f\n', n);
fprintf('t3= %0.5f\n', t3);
fprintf('t4= %0.5f\n', t4);
fprintf('p4= %0.5f\n', p4);
fprintf('q41= %0.5f\n', q41);
fprintf('wliq= %0.5f\n', wliq);
fprintf('n2= %0.5f\n', n2);

