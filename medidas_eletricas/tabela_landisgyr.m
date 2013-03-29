% tabela_landisgyr('Esm-JIMR1.xls')

function medidas = tabela_landisgyr(tab_xls)

% carrega a tabela
[num, txt, raw] = xlsread(tab_xls);

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
col_sh = 10;
col_sr = 11;
col_fator_potencia = 12;
col_dcr = 13;
col_ufer = 14;

correcao_horario = 260.4167e-003; % 06:15 / 24h
correcao_data = datenum('30-Dec-1899');

% quantidade de registros
s = size(num);
q_reg = s(1)-linha_inicial_valores+1;

disp('quantidade de registros:');
disp(q_reg);

%% identificação dos dias

% di = dia inicio
di = num(linha_inicial_valores, col_data_registrada);

for c = linha_inicial_valores:s(1)
    
    if num(c, col_data_registrada) ~= di
        di = linha_inicial_valores;
        df = c-1; % df = dia final
        
%        disp(di);
%        disp(df);
        
        %% detectando finais de semana
        cd = num(df, col_data_registrada) + correcao_data;
        d = weekday(cd);
        
        if d == 1 || d == 7
            disp('final de semana');
            disp(df);
            
        end
     
    end
end

