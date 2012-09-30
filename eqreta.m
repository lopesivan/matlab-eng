% Equacao de uma reta
% Felipe Bandeira
% 30/09/2012 - 09:45

function saida = eqreta(p1, p2)
f = 'y=a*x+b';

% substitui os valores
f1 = subs(f, {'x', 'y'}, {p1(1), p1(2)});
f2 = subs(f, {'x', 'y'}, {p2(1), p2(2)});

% resolve o sistema
sol = solve(f1, f2);

% retorna a função
saida = subs(f, {'a', 'b'}, {sol.a, sol.b});
