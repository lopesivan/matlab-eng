% cálculo para a correção do fator de potência
% entrada:
% fp - fator de potência desejado
% R - resistência
% X - Reatância
% w - frequência angular em radianos por segundo
% saída:
% X1 = valor da reatância, negativa = reatância capactiva ou
% positiva = reatância indutiva.
% tipo = {capacitor, indutor, desconhecido}
% C = valor do capacitor ou L = valor do indutor
% 
% circuito elétrico do problema:
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
