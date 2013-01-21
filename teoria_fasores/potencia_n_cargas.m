% Pot�ncia complexa de um sistema de n cargas em paralelos
% entrada:
% potn = vetor com as pot�ncia das cargas
% fpn = fator de pot�ncia das cargas
function potencia = potencia_n_cargas(potn, fpn, vrms)
%% processamento da entrada

if length(potn) ~= length(fpn)
    disp('erro: dimens�es n�o s�o compat�veis');
    return;
end

dimensao = length(potn);
fprintf('processando %u cargas\n', dimensao);

qn = zeros(1);
for posicao = 1:dimensao
    sn = potn(posicao)/fpn(posicao);    % calc�lo da aparente
    ang = acos(fpn(posicao));           % �ngulo da carga    
    qn(posicao) = sn*sin(ang);          % pot�ncia reativa
end


%% calc�los para a pot�ncia

pt = sum(potn);
qt = sum(qn);       

% pot�ncia complexa total
pc = pt + 1i * qt;

rt = real(pc);  % pot�ncia real total
at = abs(pc);   % pot�ncia aparente total

angulo = angle(pc); % fator resultante das duas cargas
angulo_graus = radtodeg(angulo);

% fator de pot�ncia visto pela fonte
fator_potencia = cos(angulo);

% com a tens�o eficaz sobre as cargas � possivel obter a corrente
% S = (1/2)*V*conj(I)
% ou
% S = Vrms * conj(Irms)
% Irms = conj(S/Vrms)

if nargin >= 3
    % corrente total
    irms = conj(pc/vrms); 
   
    % carga total
    Zt = vrms/irms;
end

% tipo de carga e tipo de fator de pot�ncia
if qt == 0
    tipo_carga = 'resistiva';
    tipo_fator = 'nada';
elseif qt > 0
    tipo_carga = 'indutiva';
    tipo_fator = 'atrassada';
else
    tipo_carga = 'capacitiva';
    tipo_fator = 'adiantada';
end

%% sa�da

potencia.complexa = pc;
potencia.aparente_total = at;
potencia.real_total = rt;

if nargin >= 3
    potencia.corrente = irms;
    potencia.carga = Zt;
end

potencia.tipo_carga = tipo_carga;

potencia.angulo = angulo;
potencia.angulo_graus = angulo_graus;
potencia.fator_potencia = fator_potencia;
potencia.fator_tipo = tipo_fator;
