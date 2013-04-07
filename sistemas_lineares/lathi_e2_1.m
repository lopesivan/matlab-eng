% Determine a resposta de entrada nula para um sistema LCIT descrito por
% (D+5)*y(t) = x(t) se a condição inicial for y(0) = 5

y = dsolve('Dy+5*y = 0', 'y(0)=5', 't');
disp(['y = ', char(y)]);