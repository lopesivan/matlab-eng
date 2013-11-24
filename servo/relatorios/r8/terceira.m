% Felipe Bandeira
% terceira questão
clear all
% função de malha aberta
fMalhaAberta = tf([1], [1 4 5 0]);
rlocus(fMalhaAberta);
sgrid([0.5 0.707], [0.5 1 2]);
[K, r] = rlocfind(fMalhaAberta);
% Após posicionar o cursor no devido local para o ZETA = 0.5
% os valores de K e r são atualizados, e são,
% K =
%   4.3259
% r = 
%  -2.7551 + 0.0000i
%  -0.6225 + 1.0875i
%  -0.6225 - 1.0875i