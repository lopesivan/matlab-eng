% Teoria do amplificador diferencial
% OBS: os transistores s�o iguais e a alimenta��o tamb�m
% -entrada:
% VEE = tens�o de alimenta��o nivel positivo
% Bcc = ganho do transistor
% RE = resistor comum dos dois transistores
% RC = resistor do coletor
% RB = resistor da base dos dois transistores
function dados = amplificador_diferencial(VEE, Bcc, RE, RC, RB)

if nargin == 0
    img = imread('fig_amplificador_diferencial_classico.png');
    imshow(img);
    disp('erro: nenhum comando');
    return;
end
 
% primeira aproxima��o
It = VEE/RE; % corrente de cauda
Ie = 0.5*It; % corrente no emissor
Vout = VEE - Ie*RC; % tens�o no coletor
% segunda aproxima��o
It2 = (VEE-0.7)/RE;
Ie2 = 0.5*It2;
Vout2 = VEE - Ie2*RC;
% aproxima��o quase exata
It3 = (VEE-0.7)/(RE+RB/(2*Bcc));
Ie3 = 0.5*It3;
Vout3 = VEE - Ie3*RC;
Ib = Ie/Bcc; % corrente na base
Vb = -Ib*RB; % tens�o na base

%% sa�da

dados.It = It;
dados.Ie = Ie;
dados.Vout = Vout;
dados.It2 = It2;
dados.Ie2 = Ie2;
dados.Vout2 = Vout2;
dados.It3 = It3;
dados.Ie3 = Ie3;
dados.Vout3 = Vout3;
dados.Ib = Ib;
dados.Vb = Vb;
