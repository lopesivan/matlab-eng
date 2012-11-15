% Circuito RLC s�rie, resposta natural
% Felipe Bandeira
% 15/nov/2012, Fortaleza-CE
%
% Entrada:
% t - tempo (segundo)
% R - resist�ncia (ohm)
% L - indut�ncia (henry)
% C - capacit�ncia (faraday)
% i0 - condi��o inicial para a equa��o i(t)
% i1 - 2� condi��o inicial para a equa��o i'(t)
%
% Saida:
% i - corrente em um dado tempo(t)
% ei - equa��o da corrente no loop
% alfa - frequ�ncia de amortecimento
% w0 - frequ�ncia de resson�ncia
% wd - frequ�ncia amortecida
% 
% Exemplos:
% caso superamortecida:
% - rlc_serie_natural(0, 30, 3, 1/27, 0, -16/3)
% caso criticamente amortecida:
% - rlc_serie_natural(0, 100, 2.5, 1e-3, 0, -9.6)
% caso subamortecida:
% - rlc_serie_natural(0, 1, 1, 1, 1, 1)

function saida = rlc_serie_natural(t, R, L, C, i0, i1, DEBUG)

alfa = R/(2*L);
w0 = 1/sqrt(L*C);

if DEBUG == 1
    disp('alfa:');
    disp(alfa);
    disp('w0:');
    disp(w0);
end

syms t A1 A2;

% caso superamortecida
if alfa > w0
   
    fprintf('caso superamortecida\n');
    
    s1 = -alfa+sqrt(alfa^2-w0^2);
    s2 = -alfa-sqrt(alfa^2-w0^2);
    
    f1 = (A1*exp(s1*t)+A2*exp(s2*t))-i0;
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0);

    sol = solve(f1, f2, A1, A2);
    f = simplify((sol.A1*exp(s1*t)+sol.A2*exp(s2*t)));
    
    if DEBUG == 1
        disp('equa��es:');
        disp(f1);
        disp(f2);
        
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2); 
        disp('fun��o final:');
        pretty(f);         
    end    

%caso criticamente amortecida    
elseif alfa == w0

    fprintf('caso criticamente amortecida\n');
    
    f1 = (A2+A1*t)*exp(-alfa*t)-i0;
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0);
    
    sol = solve(f1, f2, A1, A2);
    f = simplify((sol.A2+sol.A1*t)*exp(-alfa*t));
    
    if DEBUG == 1
        disp('equa��es:');
        disp(f1);
        disp(f2);
        
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2);    
    
        disp('fun��o final:');
        pretty(f);          
    end
    
% caso subamortecida    
else

    disp('caso subamortecida');
    
    wd = sqrt(w0^2-alfa^2); % frequ�ncia amortecida
    
    f1 = (exp(-alfa*t)*(A1*cos(wd*t)+A2*sin(wd*t)))-i0;
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0);
    
    sol = solve(f1, f2, A1, A2);
    f = simplify(exp(-alfa*t)*(sol.A1*cos(wd*t)+sol.A2*sin(wd*t)));
    
    if DEBUG == 1    
        disp('equa��es:');
        disp(f1);
        disp(f2);
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2); 
        disp('fun��o final:');
        pretty(f);
            
    end
    
end

saida.f = f;

end
    