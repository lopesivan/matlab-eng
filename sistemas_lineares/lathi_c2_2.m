% Considere um sistema LCIT especificado pela equação diferencial
% (D2+4D+k)*y(t) = (3D + 5)*x(t)
% usando as condições iniciais y0(0)=3 e Dy(0)=-7, determine a componente
% de entrada nula da resposta para três valores de k:
% (a) k = 3
% (b) k = 4
% (c) k = 40
% -- solução:

y_0 = dsolve('D2y+4*Dy+3*y = 0', 'y(0)=3', 'Dy(0)=-7', 't');
disp(['(a) k = 3; y_0 =', char(y_0)]);

y_1 = dsolve('D2y+4*Dy+4*y = 0', 'y(0)=3', 'Dy(0)=-7', 't');
disp(['(b) k = 4; y_0 =', char(y_1)]);

y_2 = dsolve('D2y+4*Dy+40*y = 0', 'y(0)=3', 'Dy(0)=-7', 't');
disp(['(c) k = 40; y_0 =', char(y_2)]);