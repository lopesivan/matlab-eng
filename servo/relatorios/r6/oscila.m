% Verifica se o sistema oscila durante o seu período transitório
% entrada:
% - sistema criado com o comnado tf

function saida = oscila(fun)

    osc = 0;
    if estabilidade(fun) == 1
        % valor final
        y = step(fun);
        if max(y) > y(length(y))
            % o sistema oscila 
            osc = 1;
        end 
    end

    saida = osc;

end

