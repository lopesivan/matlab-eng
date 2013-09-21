%sétima questão
clear all

f1 = tf([1], [1 1]);

% item a
[y, t] = step(f1);
plot(t, y, t, ones(length(t), 1))

