% Entrada:
% R - resist�ncia (ohm)
% L - indut�ncia (henry)
% C - capacit�ncia (faraday)
% rf - resposta for�ada (apenas constantes)
% i0 - condi��o inicial para a equa��o i(t)
% i1 - 2� condi��o inicial para a equa��o i'(t)

function saida = rlc_serie_forcada(R, L, C, rf,  i0, i1, DEBUG)

% coeficiente de amortecimento
alfa = R/(2*L);
% frequ�ncia de resson�ncia
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
    
    disp('raizes, s1 e s2:');
    disp(s1);
    disp(s2);
    
    f1 = rf+(A1*exp(s1*t)+A2*exp(s2*t))-i0;
    % encontra a derivada da fun��o principal e substitui t por 0
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0);
    % resolve para A1, A2
    sol = solve(f1, f2, A1, A2);
    % tenta simplificar a equa��o
    f = simplify(rf+(sol.A1*exp(s1*t)+sol.A2*exp(s2*t)));
    
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
    
    f1 = rf+(A2+A1*t)*exp(-alfa*t)-i0;
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0); 
    sol = solve(f1, f2, A1, A2);
    f = simplify(rf+(sol.A2+sol.A1*t)*exp(-alfa*t));
    
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
    
    disp('wd:');
    disp(wd);
    
    f1 = rf+(exp(-alfa*t)*(A1*cos(wd*t)+A2*sin(wd*t)))-i0;
    f2 = subs(diff(f1, t)-i1, t, 0);
    f1 = subs(f1, t, 0);
    sol = solve(f1, f2, A1, A2);
    f = simplify(rf+exp(-alfa*t)*(sol.A1*cos(wd*t)+sol.A2*sin(wd*t)));
    
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
    