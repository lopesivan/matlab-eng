%% CRIADOR de números complexos
function z = criador
    disp('criador, 01/2013. v1');

    % LOOP PRINCIPAL
    while 1
        % entrada do comando e seus possíveis argumentos
        disp(' ');
        arg = input('criador>> ', 's');

        % sistema polar ativo por padrão
        modo.polar = 1;
        % ângulo em graus por padrão
        modo.graus = 1;

        % finaliza o criador
        if strcmp(arg, 's') || strcmp(arg, 'sair')

            % livra o workspace de bobagens...
            %clearvars modo arg p_angulo p_raio;
            
            lista = who('*_cz');
            
            %a = struct([]);
            z = struct([]);
            
            % começa a criação da struct z com todos os números criados
            for c = 1:length(lista)
                % ler o valor do número
                eval(['valor=' char(lista(c))]);
                
                a = struct(char(lista(c)), valor);
                % une as estrututas
                z = catstruct(z, a);
            end

            disp('aviso: criador finalizado');

            return;

        % ajuda
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

        % cria um novo número complexo
        elseif strcmp(arg, 'z') || strcmp(arg, 'cria')

            nome = input('nome(+_cz): ', 's');

            % padrão de criação
            nome = strcat(nome, '_cz');

            %eval(['global ', nome]);

            if modo.polar == 0

                p_real = input('parte real: ');
                p_ima = input('parte imaginaria: ');

                % cria uma variável no workspace atual
                eval([nome, '=p_real + i * p_ima']);

            elseif modo.polar == 1

                p_raio = input('raio: ');

                if modo.graus == 1

                    p_angulo= input('ângulo(graus): ');
                    eval([nome, '=z_polar_graus_cart(p_raio, p_angulo)']);

                else

                    p_angulo = input('ângulo(radianos): ');
                    eval([nome, '=z_polar_cart(p_raio, p_angulo)']); 

                end

            end
            
            %eval(['nome']);
            
            %eval(['a =' nome]);
            %eval(['z = struct(nome,a)']);

        % configura o modo de operação
        elseif strcmp(arg, 'c') || strcmp(arg, 'modo')

            modo.polar = input('sistema polar [1/0]?');
            modo.graus = input('radiano[0] ou graus[1] ?');

        % estado do modo de operação
        elseif strcmp(arg, 'e') || strcmp(arg, 'estado')

            disp('polar:');
            disp(modo.polar);

            disp('graus:');
            disp(modo.graus);

        % deleta todos os números existentes(padrão "_cz")
        elseif strcmp(arg, 'd') || strcmp(arg, 'deleta tudo')

            clearvars *_cz;

            disp('todos os números criados foram deletados');

        % lista os números criados ou existentes
        elseif strcmp(arg, 'l') || strcmp(arg, 'lista')

            disp('lista: ');
            lista = who('*_cz');
            disp(lista);

        elseif strcmp(arg, 'v') || strcmp(arg, 'ver')

            disp('lista: ');
            lista = who('*_cz');
            disp(lista);

            nome = input('qual número? ', 's');

            eval(nome);

        else

            disp('erro: comando não reconhecido');

        end

    end

end
