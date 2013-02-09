% Fourier para um sinal cont�nuo
% - entrada:
% ft = fun��o em rela��o a t
% T = periodo da fun��o
% w0 = freq��ncia fundamental
% N = n�mero de intera��es
% - sa�da
% a0 = coeficiente de fourier
% an = coeficiente de fourier
% bn = coeficiente de fourier
% sf = fun��o construida para a s�rie
% f = fun��o inline
function subterfugio = fourier_serie_funcao(ft, T, w0, N)

syms t n;

% calculando os coeficientes
a0 = (2/T)*int(ft, t, 0, T);
an = (2/T)*int(ft*cos(n*w0*t), t, 0, T);
bn = (2/T)*int(ft*sin(n*w0*t), t, 0, T);
% s�rie de Fourier
sf = a0 + symsum(an*cos(n*w0*t)+bn*sin(n*w0*t), n, 1, N);
% cria uma fun��o para  manipula��o
f = @(a) subs(sf, t, a);

%% sa�da

subterfugio.a0 = a0;
subterfugio.an = an;
subterfugio.bn = bn;
subterfugio.sf = sf;
subterfugio.f = f;
