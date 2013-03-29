% tabela_landisgyr('Esm-JIMR1.xls')

function medidas = tabela_landisgyr(tab_xls)

% carrega a tabela
[num, txt, raw] = xlsread(tab_xls);

%% constantes da tabela
linha_inicial_valores = 7;
col_registro = 1;
col_data_registrada = 2;
col_hora = 3;
col_w = 4;
col_c1 = 5;
col_var_indutiva = 6;
col_c2 = 7;
col_var_capacitiva = 8;
col_c3 = 9;
col_ponta_fora = 10;
col_sr = 11;
col_fator_potencia = 12;
col_dcr = 13;
col_ufer = 14;

correcao_horario = 260.4167e-003; % 06:15 / 24h
correcao_data = datenum('30-Dec-1899');

fator_potencia_multa = 0.92;

%% quantidade de registros
s = size(num);
q_reg = s(1)-linha_inicial_valores+1;
disp('quantidade de registros:');
disp(q_reg);

%% adquirindo os valores, na ponta e fora da ponta
maxima_demanda_ponta = 0;
maxima_demanda_fora_ponta = 0;
consumo_ponta = 0;
consumo_fora_ponta = 0;
ufer_ponta = 0;
ufer_fora_ponta = 0;
ufdr_ponta = 0;
ufdr_fora_ponta = 0;

cont1 = 0;
cont2 = 0;

ca = 0;
ca2 = 0;
cr = 0;
cr2 = 0;

fp_ponta = 0;
fp_fora_ponta = 0;

%% loop principal
for t = linha_inicial_valores:s
    %disp(num(t, col_registro));
    
    %% PONTA
    if strcmp(txt(t, col_ponta_fora), 'P')     
        % demanda; ponta
        if num(t, col_w) > maxima_demanda_ponta
            maxima_demanda_ponta = num(t, col_w);
        end
        
        % consumo, .25 h = 15 min
        consumo_ponta = consumo_ponta + num(t, col_w)*.25;
        
        % ufer e ufdr na ponta, indutiva
        if strcmp(txt(t, col_sr), 'L')
            ca = ca + num(t, col_w);
            cr = cr + num(t, col_var_indutiva);
            cont1 = cont1+1;
            if cont1 > 3                    
                % consumo ativo e reativo integralizado em 1 hora
                ca = ca/4;
                cr = cr/4;                
                
                cont1 = 0;
                
                fp = cos(atan(cr/ca));
                
                if fp < fator_potencia_multa
                    ufer_ponta = ufer_ponta + (fator_potencia_multa/fp - 1)*ca;
                    
                    uf = ca*(fator_potencia_multa/fp);
                    if uf > ufdr_ponta
                        ufdr_ponta = uf;
                    end
                end
               
                ca = 0;
                cr = 0;
            end         
        end
    end
    
    %% FORA DA PONTA
    if strcmp(txt(t, col_ponta_fora), 'F')     
        % demanda; fora da ponta
        if num(t, col_w) > maxima_demanda_fora_ponta
            maxima_demanda_fora_ponta = num(t, col_w);
        end
        
        % consumo, .25 h = 15 min
        consumo_fora_ponta = consumo_fora_ponta + num(t, col_w)*.25;

        % ufer fora ponta, indutiva
        if strcmp(txt(t, col_sr), 'L')
            ca2 = ca2 + num(t, col_w);
            cr2 = cr2 + num(t, col_var_indutiva);
            cont2 = cont2+1;
            if cont2 > 3                    
                % consumo ativo e reativo integralizado em 1 hora
                ca2 = ca2/4;
                cr2 = cr2/4;                
                
                cont2 = 0;
                
                fp = cos(atan(cr2/ca2));
                
                if fp < fator_potencia_multa
                    ufer_fora_ponta = ufer_fora_ponta + (fator_potencia_multa/fp - 1)*ca2;
                    
                    uf = ca2*(fator_potencia_multa/fp);
                    if uf > ufdr_fora_ponta
                        ufdr_fora_ponta = uf;
                    end
                end
               
                ca2 = 0;
                cr2 = 0;
            end                       
        end        
    end
    
end

%% valores adquiridos
disp('maxima demanda na ponta (kW):');
disp(maxima_demanda_ponta);
disp('maxima demanda fora da ponta (kW):');
disp(maxima_demanda_fora_ponta);

disp('consumo na ponta (kWh):');
disp(consumo_ponta);
disp('consumo fora da ponta (kWh):');
disp(consumo_fora_ponta);

disp('UFER ponta:');
disp(ufer_ponta);
disp('UFER fora da ponta:');
disp(ufer_fora_ponta);

disp('UFDR ponta:');
disp(ufdr_ponta);
disp('UFDR fora da ponta:');
disp(ufdr_fora_ponta);
