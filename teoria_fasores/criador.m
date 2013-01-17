%% CRIADOR de números complexos
% dependências:
% - catstruct.m

function z = criador()

    global modo;
    
    disp('------------------------------------------------------------');    

    disp('criador, jan/2013');
    
    lista_numeros = cell(0);           
    contador_numeros = 0;

    % sistema polar ativo por padrão
    modo.polar = 1;
    % ângulo em graus por padrão
    modo.graus = 1;    

    % LOOP PRINCIPAL
    while 1
        % entrada do comando e seus possíveis argumentos
        disp(' ');
        arg = input('criador>> ', 's');

        %% finaliza o criador
        if strcmp(arg, 's') || strcmp(arg, 'sair')
            
            z = struct([]);
            
            % começa a criação da struct z com todos os números criados
            for c = 1:contador_numeros
                
                % ler o valor do número
                eval(['valor= ' char(lista_numeros(c)) ';']);
                
                a = struct(char(lista_numeros(c)), valor);
                
                % une as estrututas
                z = catstruct(z, a);
                
            end

            disp('aviso: criador finalizado');

            return;

        %% ajuda
        elseif strcmp(arg, 'a') || strcmp(arg, 'ajuda')

            disp('ajuda para o, criador');
            disp(' ');
            disp('comandos:');
            disp('s = encerra o programa');
            disp('a = ajuda');
            disp('z = cria um número complexo, resultado no workspace atual');
            disp('c = configura a forma que número é inserido,');
            disp('     em polar: 1 = polar, 0 = retangular');
            disp('     em graus: 1 = graus, 0 = radianos');
            disp('e = estado da configuração');
            disp('d = deleta todos os números existentes');
            disp('l = lista todos os números existentes');

        %% cria um novo número complexo
        elseif strcmp(arg, 'z') || strcmp(arg, 'cria')

            disp(' ');
            
            while 1
            
                nome = input('nome: ', 's');
                
                nome_repetido = 0;
                
                for c = 1:contador_numeros
                   if strcmp(nome, lista_numeros(c))
                       disp('erro: esse nome já existe... minha bitch');
                       nome_repetido = 1;
                   end
                end
                
                if nome_repetido == 1
                    continue;
                end

                if strcmp(nome, '-s')
                   break; 
                end

                contador_numeros = 1 + contador_numeros;

                lista_numeros(contador_numeros) = cellstr(nome);

                if modo.polar == 0

                    p_real = input('parte real: ');
                    p_ima = input('parte imaginaria: ');

                    % cria uma variável no workspace atual
                    eval([nome, '=p_real + i * p_ima;']);

                elseif modo.polar == 1

                    p_raio = input('raio: ');

                    if modo.graus == 1

                        p_angulo= input('ângulo(graus): ');
                        eval([nome, '=z_polar_graus_cart(p_raio, p_angulo);']);

                    else

                        p_angulo = input('ângulo(radianos): ');
                        eval([nome, '=z_polar_cart(p_raio, p_angulo);']); 

                    end

                end

                eval(['valor =' nome ';']);
                mostra_numero(valor);
                disp(' ');
                disp('------------------------------------------------------------');   
            
            end

        %% configura o modo de operação
        elseif strcmp(arg, 'c') || strcmp(arg, 'modo')

            modo.polar = input('sistema polar [1/0]?');
            modo.graus = input('radiano[0] ou graus[1] ?');

        %% estado do modo de operação
        elseif strcmp(arg, 'e') || strcmp(arg, 'estado')
            
            fprintf('\npolar = %u', modo.polar);
            fprintf('\ngraus = %u', modo.graus);

        %% deleta todos os números existentes
        elseif strcmp(arg, 'd') || strcmp(arg, 'deleta tudo')
            
            if contador_numeros > 0
                
                for a=1:contador_numeros
                   clearvars lista_numeros(a) 
                end

                lista_numeros = cell(0);
                contador_numeros = 0;

                disp('todos os números criados foram deletados');
                
            else
                
                disp('erro: nada para deletar');
            
            end

        %% lista os números criados ou existentes
        elseif strcmp(arg, 'l') || strcmp(arg, 'lista')

            if contador_numeros > 0
                disp(lista_numeros);
            else
                disp('erro: nenhum número criado');
            end

        elseif strcmp(arg, 'v') || strcmp(arg, 'ver')

            if contador_numeros > 0
                
                disp('números cadastrados: ');
                disp(lista_numeros);

                nome = input('qual número? ', 's');                              

                if strcmp(nome, 't') || strcmp(nome, 'todos')
                    
                    for c = 1:contador_numeros
                        
                        disp(' ');
                        disp('------------------------------------------------------------');   
                        fprintf('número: %s', char(lista_numeros(c)));
                        
                        eval(['valor= ' char(lista_numeros(c)) ';']);
                        
                        mostra_numero(valor);
                        
                    end  
                    
                    disp(' ');
                    disp('------------------------------------------------------------');   
                                       
                else
                    
                    try
                        eval(['valor =' nome ';']);
                    catch
                        disp('erro: número não existe');                       
                        continue;
                    end     
                    
                   mostra_numero(valor);
                   
                   disp(' ');
                
                end
                
            else
                disp('erro: crie um número...');
            end

        else

            disp('erro: comando não reconhecido');

        end

    end

end

function mostra_numero(valor)

    global modo;

    if modo.polar == 1
        
        if modo.graus == 1

            num = z_cart_polar_graus(valor);

            fprintf('\nraio          : %f', num.raio);
            fprintf('\nângulo(graus) : %f', num.angulo);

        elseif modo.graus == 0

            num = z_cart_polar(valor);

            fprintf('\nraio          : %f', num.raio);
            fprintf('\nângulo(rad) : %f', num.angulo);

        end

    elseif modo.polar == 0

        fprintf('\nreal : %f', real(valor));
        fprintf('\nimag : %f', imag(valor));

    end
    
end
