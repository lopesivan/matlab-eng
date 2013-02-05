% retificador em ponte com diodo ideal
% - entrada:
% vs = tensão rms na entrada do circuito retificador
% carga = resistência da carga
% freq = freqüência da fonte
% ond = ondulação
% - saída:
% vpico = tensão de pico na carga
% vcc = tensão média na carga
% icc = corrente da carga
% io = corrente direta nos diodos
% piv = tensão reversa sobre diodos
% cap = capacitor para filtro
function dados = retificador_em_ponte(vrms, carga, freq, ond)

vpico = vrms*sqrt(2);
vsaida = vpico;
vcc = (2*vpico)/pi;
icc = vcc/carga;            % corrente nos diodos
io = icc/2;                 % corrente direta através de cada diodo
piv = vpico;                % tensão reversa sobre o diodo
% capacitor necessário para a ondulação especificada
cap = icc/(2*freq*ond);     % freqüência é o dobro da entrada

%% saída
dados.vpico = vpico;
dados.vsaida = vsaida;
dados.vcc = vcc;
dados.icc = icc;
dados.io = io;
dados.piv = piv;
dados.cap = cap;
