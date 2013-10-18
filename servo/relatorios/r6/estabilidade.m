% Verifica a estabilidade de um sistema
% entrada:
% - função de transferência em malha fechada, criado com comando tf
% saída:
% - 0 para sistema instável
% - 1 para sistema estável

function saida = estabilidade(fun)

[polos] = pzmap(fun);

estabilidade = 1;
for R=1:length(polos)
    % analisa a posição do polo, caso a parte real seja positiva o sistema é instável
    if real(polos(R)) > 0
        % condição de instabilidade aceita
        estabilidade = 0;
        break;
    end
end

% atualiza o saída
saida = estabilidade;

end

