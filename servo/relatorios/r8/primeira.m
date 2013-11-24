% Felipe Bandeira
% primeira questão

% função
num = [1 3];
den = conv([1 1 0], [1 4 16]);
f1 = tf(num, den);

% plotando o LR
rlocus(f1);