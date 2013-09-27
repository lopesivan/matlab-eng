% primeira questão

zeta = 0.4;
wn = [10 5 1];
t = 0:0.01:10;

cor = ['b', 'g', 'r']

for c = 1:length(wn)
    gs = tf([wn(c)^2], [1 2*zeta*wn(c) wn(c)^2]);
    [y(c,:)] = step(gs, t);
    hold on;
    plot(t, y(c,:), cor(c));

    grid on;
end

xlabel('tempo segundos');

%print -depsc q1ia.eps
