% potência média
% definição matemática para a potência média, onde:
% função da potência dependente do tempo t com um período
% exemplo:
% > syms t; f = 2000*t^2; potencia_media(f, 0, 1)
function P = potencia_media(funcao, t1, periodo)
syms t;
P = (1/periodo)*int(funcao, t, t1, t1+periodo);
