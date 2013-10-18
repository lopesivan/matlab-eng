% testa tudo
clear all
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% primeira questão

fun1 = tf([1], [1 2 3 4 5]);    % item a
fun2 = tf([1], [1 3 3 2 1]);    % item b

disp('********************************************************************************');
disp('primeira questão');
disp('-item a');
fprintf('Retorno do comando: %d\n', estabilidade(fun1));
disp('-item b');
fprintf('Retorno do comando: %d\n', estabilidade(fun2));
disp(' ');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% segunda questão

disp('********************************************************************************');
disp('segunda questão');

fun1 = tf([50], [2 4 50]);
fun2 = tf([1], [1 3 2]);
fun3 = tf([1], [1 -5 6]);

disp('-item a');
[zeta, wn, wd, info] = parametros(fun1);
if info == 1
    fprintf('zeta: %f\n', zeta);
    fprintf('wn  : %f\n', wn);
    fprintf('wd  : %f\n', wd);
else
    disp('sistema instável');
end

disp('-item b');
[zeta, wn, wd, info] = parametros(fun2);
if info == 1
    fprintf('zeta: %f\n', zeta);
    fprintf('wn  : %f\n', wn);
    fprintf('wd  : %f\n', wd);

else
    disp('sistema instável');
end

disp('-item c');
[zeta, wn, wd, info] = parametros(fun3);
if info == 1
    fprintf('zeta: %f\n', zeta);
    fprintf('wn  : %f\n', wn);
    fprintf('wd  : %f\n', wd);
    
else
    disp('erro: sistema instável');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% terceira questão

disp('********************************************************************************');
disp('terceira questão');

fun1 = tf([1], [1 4 1]);
fun2 = tf([0.5], [1 1]);
fun3 = tf([1], [1 2 3 4 5]);

disp('-item a');
[yss, ess, info] = estacionario(fun1);
if info == 1
    fprintf('yss: %f\n', yss);
    fprintf('ess: %f\n', ess);
else
    disp('erro: sistema instável');
end

disp('-item b');
[yss, ess, info] = estacionario(fun2);
if info == 1
    fprintf('yss: %f\n', yss);
    fprintf('ess: %f\n', ess);
else
    disp('erro: sistema instável');
end

disp('-item c');
[yss, ess, info] = estacionario(fun3);
if info == 1
    fprintf('yss: %f\n', yss);
    fprintf('ess: %f\n', ess);
else
    disp('erro: sistema instável');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% quarta questão

