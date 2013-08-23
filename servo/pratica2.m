% Pr�tica de laborat�rio 2
% Aluno:
% - Felipe Bandeira da Silva, 1020942-X

%%%%%%%%%%%%%%%%%%%%
% Primeira quest�o %
%%%%%%%%%%%%%%%%%%%%

disp('Primeira quest�o');
disp('Plotando o gr�fico');
t = linspace(0, 10, 1000); 
f = 5*exp(-t).*sin(2*t)+2*exp(-t).*cos(2*t);
g = 2*exp(-t)-exp(-2*t);
plot(t, f, t, g);
title('Primeira quest�o');
xlabel('tempo (s)');

p = input('Proximo item[ENTER]?');

%%%%%%%%%%%%%%%%%%%%
% Segunda quest�o  %
%%%%%%%%%%%%%%%%%%%%

disp('Segunda quest�o');
x = -20:1:20;
f = x.^2-8*x+4;

minimo = f(1);
for I=2:length(f)
    if f(I) < minimo
        minimo = f(I);
        posicao = I;
    end
end

disp('Menor valor:')
disp(minimo)
disp('Posicao:')
disp(posicao)

p = input('Proximo item[ENTER]?');

%%%%%%%%%%%%%%%%%%%%
% Terceira quest�o %
%%%%%%%%%%%%%%%%%%%%

a = [1 3 6 9 11];

figure(2);
for R = 1:length(a)
   y = a(R).*t+1;
   hold on;
   plot(t, y);
end

title('Segunda quest�o');
p = input('Proximo item[ENTER]?');

%%%%%%%%%%%%%%%%%%
% Quarta quest�o %
%%%%%%%%%%%%%%%%%%

t = 0:0.01:10;
f = 3/5 - (3/10)*exp(-t).*sin(2*t)- (3/5)*exp(-t).*cos(2*t);

figure(3);
plot(t, f);

pico = f(1);

for R=2:length(t)
    if f(R) > pico
        pico = f(R);
        tPico = t(R);
    end
end

disp('pico: ');
disp(pico);
disp('em: ');
disp(tPico);

p = input('Proximo item[ENTER]?');

%%%%%%%%%%%%%%%%%%
% Quinta quest�o %
%%%%%%%%%%%%%%%%%%
% s^3+12*s^2+5*s+1
A = [1 12 5 1]
% s^2+1
B = [0 1 0 1]

soma = A+B
produto = conv(A, B)
raizesA = roots(A)
raizesB = roots(B)
valorB212 = polyval(B, 2.12)
