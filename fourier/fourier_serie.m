% S�rie de Fourier cl�ssica
% 
% Felipe Bandeira, 07/12/2012. Fortaleza-CE
%
% Entrada:
% T = per�odo
% ft = valor entre t(t0) e t(t0+1)
% ts = tempo inicial e final do evento ft
% N = n�mero de intera��o do somat�rio
% 
% Sa�da:
% a0 = componente DC
% an = en�sima constante de Fourier
% bn = en�sima constante de Fourier
% sf = fun��o de Fourier(simbolica)
% f = fun��o de Fourier
%
% Exemplo:
%
% fourier_serie(2, [-1 1], [0 1 2 ], 10)
%                   
%   ^ f(t)
%   |
%   |    ------    ------
%   |    |    |    |    |
%------------------------------>
%   |    |    |    |           t
%   ------    ------
%   |t0   t1   t2
%
%   |--- T ---|

function subterfugio = fourier_serie(T, ft, ts, N, DEBUG)

% coment�rios existem?
if nargin ~= 5
    disp('erro: nao ha comentarios suficientes');
    T = 2;
    ft = [2 1];
    ts = [0 1 2];
    N = 10;
end

if length(ft)+1 ~= length(ts)
    disp('erro: quantidade de ft ou ts n�o s�o coerentes');
    subterfugio = NaN;
    return;
end

%try
%    t = DEBUG;
%catch
%    disp('debug [DESLIGADO]');
%    DEBUG = 0;
%end

syms t n;

% frequ�ncia fundamental
w0 = (2*pi)/T;

a0 = 0;
an = 0;
bn = 0;

% construindo as componentes
for a = 1:(length(ts)-2)
   a0 = a0 + (int(ft(a), t, ts(a), ts(a+1)) + int(ft(a+1), t, ts(a+1), ts(a+2)));
   an = an + (int(ft(a)*cos(n*w0*t), t, ts(a), ts(a+1)) + int(ft(a+1)*cos(n*w0*t), t, ts(a+1), ts(a+2)));
   bn = bn + (int(ft(a)*sin(n*w0*t), t, ts(a), ts(a+1)) + int(ft(a+1)*sin(n*w0*t), t, ts(a+1), ts(a+2)));
end

a0 = (1/T)*a0;
an = (2/T)*an;
bn = (2/T)*bn;

% s�rie de Fourier
sf = a0 + symsum(an*cos(n*w0*t)+bn*sin(n*w0*t), n, 1, N);

% cria uma fun��o para  manipula��o
f = @(a) subs(sf, t, a);

% buscando as ham�nicas
An = sqrt(an^2+bn^2);
tn = atan(bn/an);

if DEBUG > 0
    ezplot(f, [0, 10*T]);
end

subterfugio.a0 = a0;
subterfugio.an = an;
subterfugio.bn = bn;
subterfugio.sf = sf;
subterfugio.f = f;
subterfugio.An = An;
subterfugio.tn = tn;
