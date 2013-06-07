% filtro

fs = 10e3; %frequencia de amostragem
t = T; % tempo de amostragem

% constantes
[B, A] = butter(2, 20/(fs/2));

% Filtragem
figure
y1 = filter(B, A, Z21);
y2 = filter(B, A, Z31);


plot(t, y1); 
hold on;
plot(t, y2, '-r');
