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

tr = 0;
tp = 0;
Mp = 0;
ts = 0;


if estabilidade(fun) == 0
    disp('sistema instável');
    return
end

[zeta, wn, wd, info] = parametros(fun);

%f = @(t) 1-exp(-zeta*wn*t)*(cos(wd*t)+ (zeta/sqrt(1-zeta^2))*sin(wd*t));
%f = @(t) 1 - (exp(-zeta*wn*t)/sqrt(1-zeta^2))*sin(wd*t + atan(sqrt(1-zeta^2)/zeta));

ezplot(f);
beta = atan(wd/(zeta*wn))
tr = (pi-beta)/wd
tp = pi/wd
Mp = (f(tp) - f(1e100))/f(1e100)


if tol == 2
    ts = 4/wd
else if tol == 5
    ts = 3/wd
end

end

