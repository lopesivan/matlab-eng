% Verifica a resposta estacionário de um servo sistema
% entrada:
% - função de transferência, criada com o comando tf
% saída:
% yss - valor em regime permanente(estacionário)
% ess - erro em regime permanente(estacionário)

function [yss, ess, info] = estacionario(fun)

yss = 0;
ess = 0;
info = 0;

if estabilidade(fun) == 1
    info = 1;
    [y] = step(fun);
    % valor em regime estacionário
    yss = y(length(y));
    % erro em regime estacionário
    ess = abs(1-yss);
else
    info = 0;
end

end

