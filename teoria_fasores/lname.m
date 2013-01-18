function variaveis = lname(funcao)

sf = char(funcao);

contador_variaveis = 0;
var = cell(0);

inicio = 0;
fim = 0;

sf = tira_espaco_branco(sf);

% disp('string:');
% disp(sf);

for q = 1:length(sf)
    if conjunto_num_inteiros(sf(q)) == 1
        
    elseif conjunto_operacoes(sf(q)) == 1
        
        % a variavel termina com a inicio de uma nova operação
        if inicio > 0
            fim = q-1;
        end
        
    else
        
        if inicio == 0
            inicio = q;
        end
    end
    
    if q == length(sf)
        
        if inicio > 0
            fim = q;
        end
        
    end
    
    if fim > 0
        
        variavel = '';
        
        for w = inicio:fim
           variavel(w-(inicio-1)) = sf(w);
        end
        
        c1 = strfind(variavel, '(');
        c2 = strfind(variavel, ')');
        
        if length(c1) > 0
            
            v = '';
            
            for w = c1(length(c1))+1:c2(1)-1
                v(w-c1(length(c1))) = variavel(w);
            end
            
            variavel = v;
            
        end
        
        inicio = 0;
        fim = 0;
        
%         disp('variavel:');
%         disp(variavel);

        contador_variaveis = contador_variaveis + 1;
        var(contador_variaveis) = cellstr(variavel);
        
    end
end

    variaveis = var;

end

function saida = conjunto_num_inteiros(c)

    numero = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    
    for q = 1:10
        
       if c == char(numero(q))
           
           saida = 1;
           return;
           
       else
           
           saida = 0;
           
       end
       
    end
end

function saida = conjunto_operacoes(c)

    operacoes = {'+', '-', '*', '/'};
    
    for q = 1:4
        
        if c == char(operacoes(q))
            saida = 1;
            return;
            
        else
            
            saida = 0;
            
        end
    end
end

function qw = tira_espaco_branco(sf)

    % tira os espaços em branco
    s = '';
    e = 0;
    
    for q = 1:length(sf)
        
       if sf(q) ~= ' '
           e = e+1;
           s(e) = sf(q);
       end
       
    end
    
    qw = s;
end
