% retificador_meia_onda com diodo ideal
% - entrada:
% vs = tensão rms na entrada do circuito retificador
% carga = resistência da carga
% freq = freqüência da fonte
% ond = ondulação
% - saída:
% vpico = tensão de pico na carga
% vcc = tensão média na carga
% icc = corrente nos diodos
% cap = capacitor para filtro
function dados = retificador_meia_onda(vrms, carga, freq, ond)
%% contas

vpico = vrms*sqrt(2);   % v = vpico*sin(a*t+p)
vcc = vpico/pi;         % tensão média
icc = vcc/carga;        % corrente no diodo
cap = icc/(freq * ond); % capacitor necessário para a ondulação especificada

%% saída

dados.vpico = vpico;
dados.vcc = vcc;
dados.icc = icc;
dados.cap = cap;
