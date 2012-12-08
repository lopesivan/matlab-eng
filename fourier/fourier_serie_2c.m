% Série de Fourier para 2 elementos
% Felipe Bandeira, 07/12/2012. Fortaleza-CE.
%
% Entrada:
% T = período
% ft = valor entre t(t0) e t(t0+1)
% ts = tempo inicial e final do evento ft
% N = número de interação do somatório
% 
% Saída:
% a0 = componente DC
% an = enésima constante de Fourier
% bn = enésima constante de Fourier
% sf = função de Fourier(simbolica)
% f = função de Fourier
%
% Exemplo:
% fourier_serie_2c(T, [2 1], [0 1 2 ], 10)
%
%--------------------------------------------------------------------------
% Subterfúgio:
% s.m. Evasiva alegação e pretexto usado por quem 
% procura, de maneira ardilosa, esquivar-se de 
% dificuldades: algumas pessoas utilizam a mentira como subterfúgio 
% para conseguir privilégios. 
% Estratégia ou tentativa de se obter alguma coisa de modo ardil. 
%--------------------------------------------------------------------------

function subterfugio = fourier_serie_2c(T, ft, ts, N)

if length(ts) <= 2
    disp('erro: numero de pontos no tempo menor que 2');
    subterfugio = NaN;
    return;
end

if length(ts) > 3
    disp('erro: numero de pontos no tempo superior a 2');
    subterfugio = NaN;
    return;
end

if length(ft) > 2
    disp('erro: numero de amostras superior a 2');
    subterfugio = NaN;
    return
end

% frequência fundamental
w0 = (2*pi)/T;

syms t n;

%--------------------------------------------------------------------------

% cálculo da componente DC, coeficiente a0 de Fourier
a0 = (1/T)*(int(ft(1), t, ts(1), ts(2)) + int(ft(2), t, ts(2),ts(3)));

% cálculo para a enésima 'an' componente
an = (2/T)*(int(ft(1)*cos(n*w0*t), t, ts(1), ts(2)) + int(ft(2)*cos(n*w0*t), t, ts(2),ts(3)));

% cálculo para a enésima 'bn' componente
bn = (2/T)*(int(ft(1)*sin(n*w0*t), t, ts(1), ts(2)) + int(ft(2)*sin(n*w0*t), t, ts(2),ts(3)));

% série de Fourier
sf = a0 + symsum(an*cos(n*w0*t)+bn*sin(n*w0*t), n, 1, N);

% cria uma função para  manipulação
f = @(a) subs(sf, t, a);

% harmônicas
An = sqrt((an^2)+(bn^2));

fAn = @(a) subs(An, n, a);

On = atan(bn/an);

fOn = @(a) subs(On, n, a);

%--------------------------------------------------------------------------
% Graficos

subplot(3,1,1);
%figure(1);
ezplot(f, [0, 10*T]);

subplot(3,1,2);
%figure(2);
ezplot(fAn, [0, 100*T]);

subplot(3, 1, 3);
ezplot(fOn, [0, 10*T]);

%--------------------------------------------------------------------------

% Os subterfúgios
subterfugio.a0 = a0;
subterfugio.an = an;
subterfugio.bn = bn;
subterfugio.sf = sf;
subterfugio.f = f;
subterfugio.An = An;
subterfugio.fAn = fAn;
subterfugio.On = On;
subterfugio.fOn = fOn;

%--------------------------------------------------------------------------
