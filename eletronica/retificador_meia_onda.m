% retificador_meia_onda com diodo ideal
% - entrada:
% vs = tens�o rms na entrada do circuito retificador
% carga = resist�ncia da carga
% freq = freq��ncia da fonte
% ond = ondula��o
% - sa�da:
% vpico = tens�o de pico na carga
% vcc = tens�o m�dia na carga
% icc = corrente nos diodos
% cap = capacitor para filtro
function dados = retificador_meia_onda(vrms, carga, freq, ond)
%% contas

vpico = vrms*sqrt(2);   % v = vpico*sin(a*t+p)
vcc = vpico/pi;         % tens�o m�dia
icc = vcc/carga;        % corrente no diodo
cap = icc/(freq * ond); % capacitor necess�rio para a ondula��o especificada

%% sa�da

dados.vpico = vpico;
dados.vcc = vcc;
dados.icc = icc;
dados.cap = cap;
