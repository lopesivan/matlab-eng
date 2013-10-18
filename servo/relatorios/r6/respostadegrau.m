% Resposta ao degrau
% entrada:
% - sistema de transferência, criado com tf
% - tolerância, 2% - 2, 5% - 5
% saída:
% tr - tempo de subida
% tp - tempo de pico
% Mp - Máximo sobre-sinal percentual
% ts - tempo de acomodação

function [tr, tp, Mp, ts] = respostadegrau(fun, tol)

ts = 0;
tp = 0;
Mp = 0;
ts = 0;

if estabilidade(fun) == 0
    disp('sistema instável');
    return

[zeta, wn, wd, info] = parametros(fun);

beta = atan(wd/(zeta*wn));
tr = (pi-beta)/wd;
tp = pi/wd;

end

