% c�lculo para a corre��o do fator de pot�ncia
% entrada:
% fp - fator de pot�ncia desejado
% R - resist�ncia
% X - Reat�ncia
% w - frequ�ncia angular em radianos por segundo
% sa�da:
% X1 = valor da reat�ncia, negativa = reat�ncia capactiva ou
% positiva = reat�ncia indutiva.
% tipo = {capacitor, indutor, desconhecido}
% C = valor do capacitor ou L = valor do indutor
% 
% circuito el�trico do problema:
% |------|------|
% |+     |      |
% V     Zl      Z1
% |-     |      |
% |------|------|
% Zl = carga, Z1 = o corretor, V = fonte.
function componente = correcao_fator_potencia(fp, R, X, w)

X1 = (R^2+X^2)/(R*tan(acos(fp))-X);
componente.X1 = X1;

if X1 < 0
    C = -1/(w*X1);
    componente.tipo = 'capacitor';
    componente.C = C;
elseif X1 > 0
    L = X1/w;
    componente.tipo = 'indutor';
    componente.L = L;
else
    componente.tipo = 'desconhecido';
end
