% Pot�ncia complexa de uma sistema de 2 cargas em paralelos
% entrada:
% potn = pot�ncia em Watts
% fpn = fator de pot�ncia, se negativa = adiantada ou positiva = atrasada.
function potencia = potencia_2_cargas(pot1, fp1, pot2, fp2, vrms)

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
   Irms = conj(pc/vrms); 
end

%% sa�da
potencia.complexa = pc;
potencia.aparente_total = at;
potencia.real_total = rt;

if nargin >= 5
    potencia.corrente = Irms;
end

potencia.angulo = angulo;
potencia.angulo_graus = angulo_graus;
potencia.fator_potencia = fator_potencia;
