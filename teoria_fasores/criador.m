%% CRIADOR de n�meros complexos
% depend�ncias:
% - catstruct.m

function z = criador()

    global modo;
    
    disp('------------------------------------------------------------');    

    disp('criador, jan/2013');
    
    lista_numeros = cell(0);           
    contador_numeros = 0;

    % sistema polar ativo por padr�o
    modo.polar = 1;
    % �ngulo em graus por padr�o
    modo.graus = 1;    

    % LOOP PRINCIPAL
    while 1
        % entrada do comando e seus poss�veis argumentos
        disp(' ');
        arg = input('criador>> ', 's');

        %% finaliza o criador
        if strcmp(arg, 's') || strcmp(arg, 'sair')
            
            z = struct([]);
            
            % come�a a cria��o da struct z com todos os n�meros criados
            for c = 1:contador_numeros
                
                % ler o valor do n�mero
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
            disp('z = cria um n�mero complexo, resultado no workspace atual');
            disp('c = configura a forma que n�mero � inserido,');
            disp('     em polar: 1 = polar, 0 = retangular');
            disp('     em graus: 1 = graus, 0 = radianos');
            disp('e = estado da configura��o');
            disp('d = deleta todos os n�meros existentes');
            disp('l = lista todos os n�meros existentes');

        %% cria um novo n�mero complexo
        elseif strcmp(arg, 'z') || strcmp(arg, 'cria')

            disp(' ');
            
            while 1
            
                nome = input('nome: ', 's');
                
                nome_repetido = 0;
                
                for c = 1:contador_numeros
                   if strcmp(nome, lista_numeros(c))
                       disp('erro: esse nome j� existe... minha bitch');
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

                    % cria uma vari�vel no workspace atual
                    eval([nome, '=p_real + i * p_ima;']);

                elseif modo.polar == 1

                    p_raio = input('raio: ');

                    if modo.graus == 1

                        p_angulo= input('�ngulo(graus): ');
                        eval([nome, '=z_polar_graus_cart(p_raio, p_angulo);']);

                    else

                        p_angulo = input('�ngulo(radianos): ');
                        eval([nome, '=z_polar_cart(p_raio, p_angulo);']); 

                    end

                end

                eval(['valor =' nome ';']);
                mostra_numero(valor);
                disp(' ');
                disp('------------------------------------------------------------');   
            
            end

        %% configura o modo de opera��o
        elseif strcmp(arg, 'c') || strcmp(arg, 'modo')

            modo.polar = input('sistema polar [1/0]?');
            modo.graus = input('radiano[0] ou graus[1] ?');

        %% estado do modo de opera��o
        elseif strcmp(arg, 'e') || strcmp(arg, 'estado')
            
            fprintf('\npolar = %u', modo.polar);
            fprintf('\ngraus = %u', modo.graus);

        %% deleta todos os n�meros existentes
        elseif strcmp(arg, 'd') || strcmp(arg, 'deleta tudo')
            
            if contador_numeros > 0
                
                for a=1:contador_numeros
                   clearvars lista_numeros(a) 
                end

                lista_numeros = cell(0);
                contador_numeros = 0;

                disp('todos os n�meros criados foram deletados');
                
            else
                
                disp('erro: nada para deletar');
            
            end

        %% lista os n�meros criados ou existentes
        elseif strcmp(arg, 'l') || strcmp(arg, 'lista')

            if contador_numeros > 0
                disp(lista_numeros);
            else
                disp('erro: nenhum n�mero criado');
            end

        elseif strcmp(arg, 'v') || strcmp(arg, 'ver')

            if contador_numeros > 0
                
                disp('n�meros cadastrados: ');
                disp(lista_numeros);

                nome = input('qual n�mero? ', 's');                              

                if strcmp(nome, 't') || strcmp(nome, 'todos')
                    
                    for c = 1:contador_numeros
                        
                        disp(' ');
                        disp('------------------------------------------------------------');   
                        fprintf('n�mero: %s', char(lista_numeros(c)));
                        
                        eval(['valor= ' char(lista_numeros(c)) ';']);
                        
                        mostra_numero(valor);
                        
                    end  
                    
                    disp(' ');
                    disp('------------------------------------------------------------');   
                                       
                else
                    
                    try
                        eval(['valor =' nome ';']);
                    catch
                        disp('erro: n�mero n�o existe');                       
                        continue;
                    end     
                    
                   mostra_numero(valor);
                   
                   disp(' ');
                
                end
                
            else
                disp('erro: crie um n�mero...');
            end

        else

            disp('erro: comando n�o reconhecido');

        end

    end

end

function mostra_numero(valor)

    global modo;

    if modo.polar == 1
        
        if modo.graus == 1

            num = z_cart_polar_graus(valor);

            fprintf('\nraio          : %f', num.raio);
            fprintf('\n�ngulo(graus) : %f', num.angulo);

        elseif modo.graus == 0

            num = z_cart_polar(valor);

            fprintf('\nraio          : %f', num.raio);
            fprintf('\n�ngulo(rad) : %f', num.angulo);

        end

    elseif modo.polar == 0

        fprintf('\nreal : %f', real(valor));
        fprintf('\nimag : %f', imag(valor));

    end
    
end
