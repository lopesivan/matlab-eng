% Polarização via realimentação do coletor e emissor de um transistor npn
% Entrada:
% rb - resistor da base
% re - resistor do emissor
% rc - resistor do coletor
% Bcc - ganho do transistor
% vcc - tensão de alimentação do circuito
% vbe - tensão base emissor, geralmente 0.6 ~ 0.7 Volts
% Exemplo:
% polarizacao_coletor_emissor(200e3, 100, 1e3, 100, 15, 0.7)
function estados = polarizacao_coletor_emissor(rb, re, rc, Bcc, vcc, vbe)

if nargin == 0
    img = imread('fig_polarizacao_coletor_emissor.png');
    imshow(img);
    return;
end

% malha do lado esquerdo, envolvendo rb, re, rb, vbe, vcc
ic = (vcc - vbe)/(rc +  re + rb/(Bcc+1));
% tensão em relação a terra
vc = vcc - ic*rc;
vce = vc - ic*re;
ib = ic/Bcc;

estados.ic = ic;
estados.vc = vc;
estados.vce = vce;
estados.ib = ib;

end
