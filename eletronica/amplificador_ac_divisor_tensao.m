% Amplificador clássico usando transistor bipolar, teoria Malvino.
% - entrada:
% r1, r2, re, rc, rf = em ohms
% vcc = tensão de alimentação do circuito
% bcc = ganho minimo do transistor
% - exemplo:
% amplificador_ac_divisor_tensao(10e3, 2.2e3, 1e3, 3.6e3, 10, 1e-3, 150, 1e3, 1.5e3)
function dados = amplificador_ac_divisor_tensao(r1, r2, re, rc, vcc, vin, bcc, rf, rl)

if nargin == 0
    img = imread('fig_amplificador_ac_divisor_tensao.png');
    imshow(img);
    return;
end

npn_dados = npn_divisor_tensao(r1, r2, re, rc, vcc, bcc);

% todos os cálculos utilizam o modelo de Moll do transistor bipolar para
% corrente alternada.

vbe_moll = 25e-3;

re = vbe_moll/npn_dados.ie;             % resistência do emissor
A = -rc/re;                             % ganho
zent = 1/(1/r1 + 1/r2 + 1/(bcc*re));    % impedância de entrada
vout_th = A*(vin*zent/(zent+rf));       % tensão thévenin de saída
vout = (vout_th*rl)/(rl+rc);            % tensão na carga rl

%% saída

dados.re = re;
dados.ganho = A;
dados.vout = vout;
dados.zent = zent;
