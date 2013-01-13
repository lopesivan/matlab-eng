function angulo = defasagem(f1, f2, frequencia)

% w = 120*pi;
% 
% o1 = pi/2;
% o2 = pi/3;
% 
% f1 = @(t) cos(w*t+o1);
% f2 = @(t) cos(w*t+o2);
% 
% disp('fun��o 1:'); 
% disp(f1);
% 
% disp('fun��o 2:'); 
% disp(f2);

zero_f1 = fzero(f1, 0);
zero_f2 = fzero(f2, 0);

disp('zero da fun��o 1:');
disp(zero_f1);

disp('zero da fun��o 2:');
disp(zero_f2);

disp('diferen�a:');
diferenca = zero_f2 - zero_f1;
disp(diferenca);

disp('�ngulo:(graus)');
graus = radtodeg((diferenca*2*pi)/(1/frequencia));
disp(graus);

angulo.radiano = degtorad(graus);
angulo.graus = graus;
