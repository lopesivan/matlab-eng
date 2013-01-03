% CRIADOR de n�meros complexos

% LOOP PRINCIPAL
while 1
    % entrado do comando e seus possiveis argumentos
    disp(' ');
    arg = input('criador>> ', 's');

    % sistema polar ativo por padr�o
    modo.polar = 1;
    % �ngulo em graus por padr�o
    modo.graus = 1;

    if strcmp(arg, '-f') || strcmp(arg, 'sair')

        % livra o workspace de bobagens...
        clearvars modo arg;

        disp('aviso: criador finalizado');

        return;

    % ajuda
    elseif strcmp(arg, '-a') || strcmp(arg, 'ajuda')

        disp('Ajuda, criador');
        disp('comandos:');
        disp('-f = encerra o programa');
        disp('-a = ajuda');
        disp('-z = cria um n�mero complexo, resultado no workspace atual');
        disp('-c = configura a forma que n�mero � inserido,');
        disp('     em polar: 1 = polar, 0 = retangular');
        disp('     em graus: 1 = graus, 0 = radianos');
        disp('-d = deleta todos os n�meros existentes');
        disp('-l = lista todos os n�meros existentes');

    % cria um novo n�mero complexo
    elseif strcmp(arg, '-z') || strcmp(arg, 'cria')

        nome = input('nome: ', 's');

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

    % configura o modo de opera��o
    elseif strcmp(arg, '-c') || strcmp(arg, 'modo')

        modo.polar = input('sistema polar [1/0]?');
        modo.graus = input('radiano[0] ou graus[1] ?');

    % estado do modo de opera��o
    elseif strcmp(arg, '-c e') || strcmp(arg, 'estado')

        disp('polar:');
        disp(modo.polar);

        disp('graus:');
        disp(modo.graus);

    % deleta todos os n�meros existentes(padr�o "_cz")
    elseif strcmp(arg, '-d') || strcmp(arg, 'deleta tudo')

        clearvars *_cz;

        disp('todos os n�meros criados foram deletados');

    % lista os n�meros criados
    elseif strcmp(arg, '-l') || strcmp(arg, 'lista')

        who *_cz

    else

        disp('erro: comando n�o reconhecido');

    end

end
