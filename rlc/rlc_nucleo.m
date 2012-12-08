% N�cleo para todos os calculos envolvendo RLC em s�rie ou paralelo.
% Felipe Bandeira, 17/11/2012. Fortaleza-CE
%
% entrada:
% R - resist�ncia
% L - indut�ncia
% C - capacit�ncia
% rf - resposta for�ada, apenas constantes
% f0 - condi��o inicial(t=0) para f(t)
% f1 - segunda condi��o inicial para f'(t)
% serie - informa se o circuito � s�rie ou paralelo
% DEBUG - no modo debug s�o mostrados todos os passos importantes
%
% sa�da:
% retorno.fn - fun��o final
% constantes - retorno.A1
%              retorno.A2
%              retorno.s1
%              retorno.s2
%              retorno.alfa
%              retorno.w0
%              retorno.wd
% tipo de oscila��o - retorno.tipo
%
function retorno = rlc_nucleo(R, L, C, rf, f0, f1, serie, DEBUG)

if nargin ~= 8
    disp('erro: sem argumentos validos');
    return;
end

% -------------------------------------------------------------------------

% c�lcula o coeficiente de amortecimento
if serie == 1
    alfa = R/(2*L);
elseif serie == 2
    alfa = 1/(2*R*C);
else
    disp('erro: padr�o rlc desconhecido');
    return;
end

% frequ�ncia de resson�ncia
w0 = 1/sqrt(L*C);

% frequ�ncia amortecida
wd = 0;

if DEBUG == 1
    disp('alfa:');
    disp(alfa);
    disp('w0:');
    disp(w0);
end

s2 = 0;
s1 = 0;

syms t A1 A2;

% -------------------------------------------------------------------------

if alfa > w0
    
    disp('--------------------');
    disp('caso superamortecida');
    disp('--------------------');
    
    tipo = 'superamortecida';
    
    s1 = -alfa+sqrt(alfa^2-w0^2);
    s2 = -alfa-sqrt(alfa^2-w0^2);
    
    fn = A1*exp(s1*t)+A2*exp(s2*t);
    
    % encontra os valores das constantes A1 e A2
    sol = solve_eq_dif(fn, f0, f1, rf, DEBUG);
    
    % tenta simplificar a equa��o
    f = simplify(rf+(sol.A1*exp(s1*t)+sol.A2*exp(s2*t)));
    
    if DEBUG == 1        
        disp('raizes, s1 e s2:');
        disp(s1);
        disp(s2);
        
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2); 
        
        disp('fun��o final:');
        pretty(f);
            
    end
    
% -------------------------------------------------------------------------

elseif alfa == w0

    disp('----------------------------');
    disp('caso criticamente amortecida');
    disp('----------------------------');
    
    tipo = 'criticamente amortecida';
    
    fn = (A2+A1*t)*exp(-alfa*t);
    
    sol = solve_eq_dif(fn, f0, f1, rf, DEBUG);
    
    f = simplify(rf+(sol.A2+sol.A1*t)*exp(-alfa*t));
    
    if DEBUG == 1
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2);    
    
        disp('fun��o final:');
        pretty(f);          
    end

% -------------------------------------------------------------------------

else
    
    disp('------------------');
    disp('caso subamortecida');
    disp('------------------');
    
    tipo = 'subamortecida';
    
    wd = sqrt(w0^2-alfa^2); % frequ�ncia amortecida
    
    fn = exp(-alfa*t)*(A1*cos(wd*t)+A2*sin(wd*t));
    
    sol = solve_eq_dif(fn, f0, f1, rf, DEBUG);
    
    f = simplify(rf+exp(-alfa*t)*(sol.A1*cos(wd*t)+sol.A2*sin(wd*t)));
    
    if DEBUG == 1            
        disp('wd:');
        disp(wd);        
        
        disp('constantes:');
        disp(sol.A1);
        disp(sol.A2);
        
        disp('fun��o final:');
        pretty(f);
            
    end

end

% -------------------------------------------------------------------------

% solu��o
retorno.f = f;

% equa��o caracter�stica
retorno.fn = fn;

% constantes
retorno.A1 = sol.A1;
retorno.A2 = sol.A2;
retorno.s1 = s1;
retorno.s2 = s2;

retorno.alfa = alfa;
retorno.w0 = w0;
retorno.wd = wd;

% tipo de oscila��o
retorno.tipo = tipo;
