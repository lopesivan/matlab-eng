function dados = realimentacao_coletor(rb, rc, vcc, bcc)

% Orientação para o projeto
% rb = bcc*rc, para que o ponto de operação seja no meio da reta de Q

if nargin == 0
    img = imread('fig_realimentacao_coletor.png');
    imshow(img);
    return;
end

is = vcc/rc;                        % corrente de saturação
ic = (vcc - .7)/(rc + (rb/bcc));    % corrente no coletor
vc = vcc - ic*rc;                   % tensão no coletor, referência terra
ib = (-.7+vc)/(rc+rb);              % aproximação


%% saída

dados.is = is;
dados.ic = ic;
dados.vc = vc;
dados.ib = ib;
