% Retorna os parâmetros coeficiente de amortecimento, frequência amortecida
% frequência não amortecida de um sistema de segunda ordem.
% entrada:
% - função de transferência em malha fechada, criado com comando tf
% saída:
% - zeta
% - wn
% - wd
% - info: 0 - sistema não é estável, 1 - sistema é estável

function [zeta, wn, wd, info] = parametros(fun)

zeta = 0;
wn = 0;
wd = 0;
info = 0;

if estabilidade(fun) == 0
    % sistema instável
    info = 0;
    return;
else
    % sistema estável
    info = 1;

    [num, den] = tfdata(fun, 'v');

    if length(den) > 3
        disp('erro: função é de ordem maior que 2');
        return
     end

    % normaliza o denominador
    nden = den/den(1);
    wn = sqrt(nden(3));
    zeta = nden(2)/(2*wn);
    wd = wn*sqrt(1-zeta^2);

end

end

