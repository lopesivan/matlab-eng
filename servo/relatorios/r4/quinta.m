%Quinta questão
clear all

f1 = tf([1], [1 1]);

k = [1 2 3 4 5];

tempo = 0:0.01:3;

for i=1:length(k)
    [y(:,i), t] = step(feedback(f1, k(i)), tempo);
end

plot(t, y)

