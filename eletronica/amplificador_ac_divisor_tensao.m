% Amplificador cl�ssico usando transistor bipolar, teoria Malvino.
% paginas: ~403
% - entrada:
% r1, r2, re, rc, rf = em ohms
% vcc = tens�o de alimenta��o do circuito
% bcc = ganho minimo do transistor
% - exemplo:
% amplificador_ac_divisor_tensao(r1, r2, re, rc, vcc, vin, bcc, rf, rl)
% amplificador_ac_divisor_tensao(10e3, 2.2e3, 1e3, 3.6e3, 10, 1e-3, 100, 600, 10e3)
function dados = amplificador_ac_divisor_tensao(r1, r2, re, rc, vcc, vin, bcc, rf, rl)

if nargin == 0
    img = imread('fig_amplificador_ac_divisor_tensao.png');
    imshow(img);
    return;
end

npn_dados = npn_divisor_tensao(r1, r2, re, rc, vcc, bcc);

% todos os c�lculos utilizam o modelo de Moll do transistor bipolar para
% corrente alternada.

vbe_moll = 25e-3;   % tens�o de moll para o c�lculo do ganho

re = vbe_moll/npn_dados.ie;             % resist�ncia do emissor
zbase = re*bcc;                         % imped�ncia da base
zent = 1/(1/r1 + 1/r2 + 1/(bcc*re));    % imped�ncia de entrada
% calculando o ganho
vb = (vin*zent)/(rf+zent);              % tens�o ac na base
ib = vb / zbase;                        % corrente na base
ic = bcc*ib;                            % a corrente no coletor depende da corrente na base
rc_ac = 1/(1/rc + 1/rl);                % imped�ncia de sa�da
vc = rc_ac*ic;
ganho_bc = vc/vb;                       % ganho base - coletor
% alternativamente
ie = vb/re;
ganho_bc_2 = rc_ac/re;

ganho_es = vc/vin;          % ganho entrada(sem divisor tens�o) - sa�da

%% sa�da

dados.re = re;
dados.zbase = zbase;
dados.zent = zent;
dados.vb = vb;
dados.ib = ib;
dados.ic = ic;
dados.ie = ie;
dados.rc_ac = rc_ac;
dados.vc = vc;
dados.ganho_bc = ganho_bc;
dados.ganho_bc_2 = ganho_bc_2;
dados.ganho_es = ganho_es;
