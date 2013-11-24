% Felipe Bandeira
% segunda questão
clear all
% função de malha aberta
fMalhaAberta = tf([1], [1 4 5 0]);
rlocus(fMalhaAberta);
sgrid([0.5 0.707], [0.5 1 2]);