% Polarização por fontes simetricas
% Entrada:
% rb - resistor da base
% rc - resistor do coletor
% re - resistor do emissor
% bcc - ganho do transistor
% vcc - tensão de alimentação do circuito
% vbe - tensão base emissor, geralmente 0.6 ~ 0.7 Volts
% Exemplo:
% polarizacao_fontes_simetricas(1e3, 4.7e3, 10e3, 180, 12, 0.7)
function variaveis = polarizacao_fontes_simetricas(rb, rc, re, bcc, vcc, vbe)

if nargin == 0
    img = imread('fig_polarizacao_fontes_simetricas.png');
    imshow(img);
    return;
end

% malha do rb com vbe e re
ie = (vcc - vbe)/(rb/bcc + re);
ib = ie/bcc;
vce = vcc*2 - rc*ie - re*ie;
ic_sat = vcc*2/(rc+re);

% curva de carga
x = [0, vce, vcc*2];
y = [ic_sat, ie, 0];
% plot(x, y);

variaveis.ie = ie;          % corrente no emissor
variaveis.ib = ib;          % corrente na base
variaveis.vce = vce;        % tensão coletor emissor
variaveis.ic_sat = ic_sat;  % corrente de saturação
variaveis.curva = [x, y];   % curva de carga
end
