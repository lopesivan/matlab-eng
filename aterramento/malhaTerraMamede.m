%malhaTerraMamede('subestacaoMamede.xlsx')
function saida = malhaTerraMamede(axls)

dadosMedidos = xlsread(axls);
[linhaTamanho, colunaTamanho] = size(dadosMedidos);
mediaResistividade = [];
media = 0;
maximoValor = 0;
minimoValor = dadosMedidos(1, 2);

% Resistividade m�dia ( Ohm * m )
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

disp('Resistividade M�dia:');
for L = 1:linhaTamanho
    fprintf('Dist�ncia= %d -> Resistividade m�dia= %f\n', dadosMedidos(L, 1), mediaResistividade(L));
end

plot(dadosMedidos(:,1), mediaResistividade)
grid on;
xlabel('dist�ncia entre os eletrodos(m)');
ylabel('resistividade m�dia(ohm m)');

% calculando a resistividade m�dia do solo
p1 = mediaResistividade(1);
p2 = mediaResistividade(linhaTamanho);

r1= p2/p1;
disp('Valor de p2/p1:');
disp(r1);

% interpola��o para a tabela do fator de multiplica��o
tabelaFatorMultiplicacao = xlsread('fatorMultiplicacao.xlsx');
K1 = interp1(tabelaFatorMultiplicacao(:, 1), tabelaFatorMultiplicacao(:, 2), r1);

% resistividade m�dia
pm = K1*p1;
% �rea da malha
S = 57 * 41;
% profundidade
R = sqrt(S/pi);
% dist�ncia m�dia
Hm = interp1(mediaResistividade, dadosMedidos(:,1), pm);
K2 = R/Hm;

disp('K1:');
disp(K1);
disp('K2:');
disp(K2);
disp('Area da malha:');
disp(S);
disp('pm');
disp(pm);
disp('Profundidade m�dia');
disp(Hm);
end