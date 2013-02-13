% divisor de tensão clássico
function dados = npn_divisor_tensao(r1, r2, re, rc, vcc, bcc)

% poxa nada? sério?!
if nargin == 0
    img = imread('fig_npn_divisor_tensao.png');
    imshow(img);
    return;
end

vbe = 0.7; % silício

is = vcc/(rc+re);               % corrente de saturação
vth = (r2*vcc)/(r1+r2);         % tensão na base
rth = (r1*r2)/(r1+r2);          % resistência vista pelo terminal da base
ie = (vth-vbe)/re;              % corrente no emissor
ic = ie;                        % corrente no coletor
vc = vcc - ic*rc;               % tensão no coletor
ve = vth - vbe;                 % tensão no emissor
vce = vc-ve;                    % tensão coletor emissor
ib = (vth-0.7)/(rth+re+re*bcc); % corrente na base

%% saída

dados.is = is;
dados.vth = vth;
dados.rth = rth;
dados.ie = ie;
dados.ic = ic;
dados.vc = vc;
dados.ve = ve;
dados.vce = vce;
dados.ib = ib;
