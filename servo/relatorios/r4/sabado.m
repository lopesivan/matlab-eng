%sétima questão
clear all

f1 = tf([1], [1 1]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% item a
%[y, t] = step(f1);

% plotando o grafico da resposta
%plot(t, y, t, ones(length(t), 1))

% plotando o grafico do erro
%plot(t, ones(length(t),1)-y)
%xlabel('tempo')
%ylabel('erro')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% item b

mf = feedback(f1, 1);
[y t] = step(mf);
%plot(t, y, t, ones(length(t), 1))

% plotando o grafico do erro
plot(t, ones(length(t),1)-y)

