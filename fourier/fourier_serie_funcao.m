% Fourier para um sinal contínuo
% - entrada:
% ft = função em relação a t
% T = periodo da função
% w0 = freqüência fundamental
% N = número de interações
% - saída
% a0 = coeficiente de fourier
% an = coeficiente de fourier
% bn = coeficiente de fourier
% sf = função construida para a série
% f = função inline
function subterfugio = fourier_serie_funcao(ft, T, w0, N)

syms t n;

% calculando os coeficientes
a0 = (2/T)*int(ft, t, 0, T);
an = (2/T)*int(ft*cos(n*w0*t), t, 0, T);
bn = (2/T)*int(ft*sin(n*w0*t), t, 0, T);
% série de Fourier
sf = a0 + symsum(an*cos(n*w0*t)+bn*sin(n*w0*t), n, 1, N);
% cria uma função para  manipulação
f = @(a) subs(sf, t, a);

%% saída

subterfugio.a0 = a0;
subterfugio.an = an;
subterfugio.bn = bn;
subterfugio.sf = sf;
subterfugio.f = f;
