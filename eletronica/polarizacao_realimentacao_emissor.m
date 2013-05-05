% Polarização por fontes simetricas
% Entrada:
% rb - resistor da base
% rc - resistor do coletor
% re - resistor do emissor
% bcc - ganho do transistor
% vcc - tensão de alimentação do circuito
% vbe - tensão base emissor, geralmente 0.6 ~ 0.7 Volts
% Exemplo:
% polarizacao_realimentacao_emissor(430e3, 100, 910, 15, 100, 0.7)
function saida = polarizacao_realimentacao_emissor(rb, re, rc, vcc, bcc, vbe)

if nargin == 0
    img = imread('fig_realimentacao_emissor.png');
    imshow(img);
    return;
end

ic = (vcc-vbe)/(re + rb/bcc);
vc = vcc - ic*rc;
ve = ic*re;
vce = vc-ve;

saida.ic = ic;
saida.vc = vc;
saida.ve = ve;
saida.vce = vce;

end
