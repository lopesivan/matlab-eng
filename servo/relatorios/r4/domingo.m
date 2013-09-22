% continuação da questão 7
clear all

f1 = tf([1], [1 1]);

k = [1 10 100];

tempo = 0:0.01:1;

for i=1:length(k)
    [y(:,i), t] = step(feedback(f1*k(i), 1), tempo);
end

%plot(t, y)

plot(t, ones(length(t),3)-y)

