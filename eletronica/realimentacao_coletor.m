function dados = realimentacao_coletor(rb, rc, vcc, bcc)

% Orienta��o para o projeto
% rb = bcc*rc, para que o ponto de opera��o seja no meio da reta de Q

if nargin == 0
    img = imread('fig_realimentacao_coletor.png');
    imshow(img);
    return;
end

is = vcc/rc;                        % corrente de satura��o
ic = (vcc - .7)/(rc + (rb/bcc));    % corrente no coletor
vc = vcc - ic*rc;                   % tens�o no coletor, refer�ncia terra
ib = (-.7+vc)/(rc+rb);              % aproxima��o


%% sa�da

dados.is = is;
dados.ic = ic;
dados.vc = vc;
dados.ib = ib;
