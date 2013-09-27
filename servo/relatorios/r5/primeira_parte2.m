% parte 2, primeira questão

clear all

zeta = [0 0.4 0.6 0.8 1 1.4];
wn = 5;
t = 0:0.001:4;
cor = ['b', 'g', 'r', 'c', 'm', 'y'];

for c = 1:length(zeta)
    gs = tf([wn^2], [1 2*zeta(c)*wn wn^2]);
    [y(c,:)] = step(gs, t);
    hold on;
    plot(t, y(c,:), cor(c));

    grid on;
end

xlabel('tempo segundos');


