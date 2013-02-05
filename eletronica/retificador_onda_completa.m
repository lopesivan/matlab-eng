% retificador onda completa com diodo ideal
% - entrada:
% vs = tens�o rms na entrada do circuito retificador
% carga = resist�ncia da carga
% freq = freq��ncia da fonte
% ond = ondula��o
% - sa�da:
% vpico = tens�o de pico na carga
% vcc = tens�o m�dia na carga
% icc = corrente da carga
% io = corrente direta nos diodos
% piv = tens�o reversa sobre diodos
% cap = capacitor para filtro
function dados = retificador_onda_completa(vrms, carga, freq, ond)
%% contas

vpico = vrms*sqrt(2);       % tens�o de pico
% deriva��o central
vsaida = vpico/2;           % tens�o de pico retificada
vcc = (1/2)*((2*vpico)/pi); % tens�o m�dia
icc = vcc/carga;            % corrente nos diodos
io = icc/2;                 % corrente direta atrav�s de cada diodo
piv = vpico;                % tens�o reversa sobre o diodo
% capacitor necess�rio para a ondula��o especificada
cap = icc/(2*freq*ond);     % freq��ncia � o dobro da entrada

%% sa�da

dados.vpico = vpico;
dados.vsaida = vsaida;
dados.vcc = vcc;
dados.icc = icc;
dados.io = io;
dados.piv = piv;
dados.cap = cap;
