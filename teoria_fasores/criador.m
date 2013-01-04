%% CRIADOR de n�meros complexos
function z = criador
    disp('criador, 01/2013. v1');

    % LOOP PRINCIPAL
    while 1
        % entrada do comando e seus poss�veis argumentos
        disp(' ');
        arg = input('criador>> ', 's');

        % sistema polar ativo por padr�o
        modo.polar = 1;
        % �ngulo em graus por padr�o
        modo.graus = 1;

        % finaliza o criador
        if strcmp(arg, 's') || strcmp(arg, 'sair')

            % livra o workspace de bobagens...
            %clearvars modo arg p_angulo p_raio;
            
            lista = who('*_cz');
            
            %a = struct([]);
            z = struct([]);
            
            % come�a a cria��o da struct z com todos os n�meros criados
            for c = 1:length(lista)
                % ler o valor do n�mero
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
            disp('z = cria um n�mero complexo, resultado no workspace atual');
            disp('c = configura a forma que n�mero � inserido,');
            disp('     em polar: 1 = polar, 0 = retangular');
            disp('     em graus: 1 = graus, 0 = radianos');
            disp('e = estado da configura��o');
            disp('d = deleta todos os n�meros existentes');
            disp('l = lista todos os n�meros existentes');

        % cria um novo n�mero complexo
        elseif strcmp(arg, 'z') || strcmp(arg, 'cria')

            nome = input('nome(+_cz): ', 's');

            % padr�o de cria��o
            nome = strcat(nome, '_cz');

            %eval(['global ', nome]);

            if modo.polar == 0

                p_real = input('parte real: ');
                p_ima = input('parte imaginaria: ');

                % cria uma vari�vel no workspace atual
                eval([nome, '=p_real + i * p_ima']);

            elseif modo.polar == 1

                p_raio = input('raio: ');

                if modo.graus == 1

                    p_angulo= input('�ngulo(graus): ');
                    eval([nome, '=z_polar_graus_cart(p_raio, p_angulo)']);

                else

                    p_angulo = input('�ngulo(radianos): ');
                    eval([nome, '=z_polar_cart(p_raio, p_angulo)']); 

                end

            end
            
            %eval(['nome']);
            
            %eval(['a =' nome]);
            %eval(['z = struct(nome,a)']);

        % configura o modo de opera��o
        elseif strcmp(arg, 'c') || strcmp(arg, 'modo')

            modo.polar = input('sistema polar [1/0]?');
            modo.graus = input('radiano[0] ou graus[1] ?');

        % estado do modo de opera��o
        elseif strcmp(arg, 'e') || strcmp(arg, 'estado')

            disp('polar:');
            disp(modo.polar);

            disp('graus:');
            disp(modo.graus);

        % deleta todos os n�meros existentes(padr�o "_cz")
        elseif strcmp(arg, 'd') || strcmp(arg, 'deleta tudo')

            clearvars *_cz;

            disp('todos os n�meros criados foram deletados');

        % lista os n�meros criados ou existentes
        elseif strcmp(arg, 'l') || strcmp(arg, 'lista')

            disp('lista: ');
            lista = who('*_cz');
            disp(lista);

        elseif strcmp(arg, 'v') || strcmp(arg, 'ver')

            disp('lista: ');
            lista = who('*_cz');
            disp(lista);

            nome = input('qual n�mero? ', 's');

            eval(nome);

        else

            disp('erro: comando n�o reconhecido');

        end

    end

end
