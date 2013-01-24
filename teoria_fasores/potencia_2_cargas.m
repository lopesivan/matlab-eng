% Pot�ncia complexa de um sistema de 2 cargas em paralelos
% entrada:
% potn = pot�ncia em Watts
% fpn = fator de pot�ncia, se negativa = adiantada ou positiva = atrasada.
% exemplo:
% potencia_2_cargas(2e3, -0.75, 4e3, 0.95, 311.127)
function potencia = potencia_2_cargas(pot1, fp1, pot2, fp2, vrms)
% calculo individual para cada carga

% pot�ncia aparente da carga 1
s1 = pot1/fp1;
% pot�ncia reativa da carga 1
angulo1 = acos(fp1);
q1 = s1*sin(angulo1);

% pot�ncia aparente da carga 2
s2 = pot2/fp2;
% pot�ncia reativa da carga 2
angulo2 = acos(fp2);
q2 = s2*sin(angulo2);

%% calculos para a potencia

pt = pot1+pot2;
qt = q1+q2;        

% pot�ncia complexa total
pc = pt + 1i * qt;

rt = real(pc);  % pot�ncia real total
at = abs(pc);   % pot�ncia aparente total

angulo = angle(pc); % fator resultante das duas cargas
angulo_graus = radtodeg(angulo);

fator_potencia = cos(angulo);

% com a tens�o eficaz sobre as cargas � possivel obter a corrente
% S = (1/2)*V*conj(I)
% ou
% S = Vrms * conj(Irms)
% Irms = conj(S/Vrms)

if nargin >= 5
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

if nargin >= 5
    potencia.corrente = irms;
    potencia.carga = Zt;
end

potencia.tipo_carga = tipo_carga;

potencia.angulo = angulo;
potencia.angulo_graus = angulo_graus;
potencia.fator_potencia = fator_potencia;
potencia.fator_tipo = tipo_fator;

