% Potência complexa de um sistema de n cargas em paralelos
% -- entrada:
% potn = vetor com as potência das cargas
% fpn = fator de potência das cargas
%
% -- exemplo:
% Problema 12.31 Johnson
% Duas carga em paralelo consomem respectivamente 210W com um fator de
% potência de 0.6(adiantado) e 40W com um fator de potência de
% 0.8(atrasado). Se a tensão através da associação em paralelo é Vg =
% 50/15º V eficazes, calcule a corrente I entregue pela fonte.
%
% resolvendo:
% do problema temos duas cargas, logo o vetor potn deve ser
% p = [210, 40]
% para o fator de potência deve ser levado em consideração a sua posição,
% atrasada é positiva e adiantada é negativa
% fp = [-0.6, 0.8]
% colocando tudo no programa temos
% potencia_n_cargas([210, 40], [-0.6, 0.8], 50)
% nos levando a corrente entrege a fonte:
% I = 5+j5
function potencia = potencia_n_cargas(potn, fpn, vrms)
%% processamento da entrada

if length(potn) ~= length(fpn)
    disp('erro: dimensões não são compatíveis');
    return;
end

dimensao = length(potn);
fprintf('processando %u cargas\n', dimensao);

qn = zeros(1);
for posicao = 1:dimensao
    sn = potn(posicao)/fpn(posicao);    % calcúlo da aparente
    ang = acos(fpn(posicao));           % ângulo da carga    
    qn(posicao) = sn*sin(ang);          % potência reativa
end


%% calcúlos para a potência

pt = sum(potn);
qt = sum(qn);       

% potência complexa total
pc = pt + 1i * qt;

rt = real(pc);  % potência real total
at = abs(pc);   % potência aparente total

angulo = angle(pc); % fator resultante das duas cargas
angulo_graus = radtodeg(angulo);

% fator de potência visto pela fonte
fator_potencia = cos(angulo);

% com a tensão eficaz sobre as cargas é possivel obter a corrente
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

% tipo de carga e tipo de fator de potência
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

%% saída

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
