% retificador em ponte com diodo ideal
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
function dados = retificador_em_ponte(vrms, carga, freq, ond)

vpico = vrms*sqrt(2);
vsaida = vpico;
vcc = (2*vpico)/pi;
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