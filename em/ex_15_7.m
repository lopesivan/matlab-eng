% Solu��o da equa��o de laplace por elementos finitos para problemas
% bidimensionais usando elementos triangulares
% ND = N� de n�s
% NE = N� de elementos
% NP = N� de n�s fixos(onde o potencial � preestabelecido)
% NDP(I) = N� do n� com potencial preestabelecido, I = 1, 2, ... NP
% VAL(I) = Valor do potencial preestabelecido no n� NDP(I)
% NL(I, J) = Lista dos n�s para cada elemento I, onde J = 1, 2, 3 refere-se
% ao n�mero do n� local
% CE(I, J) = Matriz de coeficientes do elemento
% C(I, J) = Matriz de rigidez global
% B(I) = Matriz do lado direito no sistem de equa��es simult�neas
% X(I), Y(I) = Coordenadas globais do n� I
% XL(J), YL(J) = Coordenadas locais do n� J= 1, 2, 3
% V(I) = Potencial no n� I
% Matrizes P(I) e Q(I) est�o definidas na equa��o

%clear
%input('Arquivo de dados')

B = zeros(ND, 1);
C = zeros(ND, ND);

for I=1:NE
    K = NL(I, [1:3]);
    XL = X(K);
    YL = Y(K);
    
    P = zeros(3, 1);
    Q = zeros(3, 1);
    
    P(1) = YL(2) - YL(3);
    P(2) = YL(3) - YL(1);
    P(3) = YL(1) - YL(2);
    
    Q(1) = XL(3) - XL(2);
    Q(2) = XL(1) - XL(3);
    Q(3) = XL(2) - XL(1);
    
    AREA = 0.5*abs(P(2)*Q(3) - Q(2)*P(3));
    
    % Determina��o da matriz de coeficientes para o elemento I
    CE = (P*P'+Q*Q')/(4*AREA);
    
    for J=1:3
        IR = NL(I, J);
        IFLAG1 = 0;
        
        % verifica��o da correspond�ncia entre a linha da matriz e um n�
        % fixo 
        for K = 1:NP
            if(IR == NDP(K))
                C(IR, IR) = 1;
                B(IR) = VAL(K);
                
                IFLAG1 = 1;
                
            end
        end % fim para k = 1:NP
        
        if(IFLAG1 == 0)
            for L=1:3
                IC = NL(I, L);
                IFLAG2 = 0;
                
                % verifica��o da correspond�ncia entre a coluna da matriz e
                % um n� fixo
                for K = 1:NP
                    if(IC == NDP(K)),
                        B(IR) = B(IR) - CE(J, L)*VAL(K);
                        IFLAG2 = 1;
                    end
                end
                
                if(IFLAG2 == 0)
                    C(IR, IC) = C(IR, IC) + CE(J, L);
                end
            end
        end
    end
end

V = inv(C)*B;
V = V';

diary ex157.out
[ND, NE, NP]
[[1:ND]' X' Y' V']
diary off
