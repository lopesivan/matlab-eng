% malhaTerraGeraldo('tabelaExemplo2_12GeraldoKindermann.xlsx')
function saida = desvioRooney(dadosMedidos)

% dadosMedidos = xlsread(axls);
[linhaTamanho, colunaTamanho] = size(dadosMedidos);
mediaResistividade = [];
media = 0;
maximoValor = 0;
minimoValor = dadosMedidos(1, 2);

% Resistividade média ( Ohm * m )
for L = 1:linhaTamanho
    for C = 2:colunaTamanho
        if dadosMedidos(L, C) > maximoValor
            maximoValor = dadosMedidos(L, C);
        end
        if dadosMedidos(L, C) < minimoValor
            minimoValor = dadosMedidos(L, C);
        end
        
        media = media + dadosMedidos(L, C);
    end
    media = media / (colunaTamanho-1);
    mediaResistividade(L) = media;
    
    media = 0;
end

% disp('Resistividade Média:');
% for L = 1:linhaTamanho
%     fprintf('Distância= %d -> Resistividade média= %f\n', dadosMedidos(L, 1), mediaResistividade(L));
% end

%disp(mediaResistividade')
%disp(dadosMedidos(:, 1))
tabelaCalculos = [dadosMedidos(:, 1), mediaResistividade'];

%disp(tabelaCalculos)

q = 0;
media = 0;
resistividadeCorrigida = [];
% determinando os desvios relativos
for L = 1:linhaTamanho
    for C = 2:colunaTamanho
        if (abs(dadosMedidos(L, C)-tabelaCalculos(L, 2))/tabelaCalculos(L, 2)) >= .5
            %disp('Valor com desvio maior que 50%');
            %disp(dadosMedidos(L, C));           
        else
            media = media + dadosMedidos(L, C);
            q = q + 1;
        end
    end  
    % média corrigida
    resistividadeCorrigida(L) = media/q;
    media = 0;
    q = 0;
    
end

%tabelaCalculos = [dadosMedidos(:, 1), mediaResistividade', resistividadeCorrigida'];
tabelaCalculos = [dadosMedidos(:, 1), resistividadeCorrigida'];

%profundidaCravamento = xlsread(axls, 2);

% R = [];
% for Q = 1:size(tabelaCalculos, 1)
%     R(Q) = resistencia(tabelaCalculos(Q, 3), tabelaCalculos(Q, 1), profundidaCravamento);
% end


% tabela com valores
% espaçamento, resistividade com erros, resitividade corrigida, resistência
% média
%tabelaCalculos = [dadosMedidos(:, 1), mediaResistividade', resistividadeCorrigida', R'];

% grafico de resistividade
%plot(tabelaCalculos(:, 1), tabelaCalculos(:, 3));
%grid on;

saida = tabelaCalculos;

end