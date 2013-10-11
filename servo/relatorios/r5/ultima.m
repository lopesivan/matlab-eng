% quarta questão

% encontrando a equação de transferencia,

clear all

K = [1 4 6 10 25 400];
t = 0:0.01:5;
cor = ['b', 'g', 'r', 'c', 'm', 'k'];

for c = 1:length(K)
    gs = tf([K(c)], [1 4 K(c)]);
    [y(c,:)] = step(gs, t);
    hold on;
    plot(t, y(c,:), cor(c));
    grid on;
end

xlabel('tempo segundos');


