% Resolva:
% (D2 + 2D)y0(t) = 0

y_0 = dsolve('D2y+2*Dy = 0', 'y(0)=1', 'Dy(0)=4', 't');
disp(['y0 =', char(y_0)]);