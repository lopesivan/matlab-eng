% divisor de tens�o cl�ssico
function dados = npn_divisor_tensao(r1, r2, re, rc, vcc, bcc)

% poxa nada? s�rio?!
if nargin == 0
    img = imread('fig_npn_divisor_tensao.png');
    imshow(img);
    return;
end

vbe = 0.7; % sil�cio

is = vcc/(rc+re);               % corrente de satura��o
vth = (r2*vcc)/(r1+r2);         % tens�o na base
rth = (r1*r2)/(r1+r2);          % resist�ncia vista pelo terminal da base
ie = (vth-vbe)/re;              % corrente no emissor
ic = ie;                        % corrente no coletor
vc = vcc - ic*rc;               % tens�o no coletor
ve = vth - vbe;                 % tens�o no emissor
vce = vc-ve;                    % tens�o coletor emissor
ib = (vth-0.7)/(rth+re+re*bcc); % corrente na base

%% sa�da

dados.is = is;
dados.vth = vth;
dados.rth = rth;
dados.ie = ie;
dados.ic = ic;
dados.vc = vc;
dados.ve = ve;
dados.vce = vce;
dados.ib = ib;
