function saida = diesel(p1, t1, qh, r)

% constantes tabeladas
k = 1.4;
Rg = .287;
cp = 1.0035;
cv = .7165

% conversão para Kelvin
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
