% Determine a resposta h(t) ao impulso para um sistema LCIT especificado
% pela equação diferencial:
% (D2+3D+2)y(t) = Dx(t)
% Este é um sistema de segunda ordem com b0 = 0. Inicialmente, determinamos
% a componente de entrada nula para as condições iniciais y(0-) = 0 e
% Dy(0-)= 1. Como P(D) = D, a resposta a entrada nula é diferenciável e a
% resposta é imediatamente obtida.

y_n = dsolve('D2y+3*Dy+2*y=0', 'y(0)=0', 'Dy(0)=1', 't');
Dy_n = diff(y_n);
disp(['h(t) = (', char(Dy_n), ') u(t)']);
