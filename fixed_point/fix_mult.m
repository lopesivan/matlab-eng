function subterfurgio = fix_mult(a, b)

sinal = 1;
tamanho = 16;
fracao = 8;

subterfurgio = fi(a, sinal, tamanho, fracao) * fi(b, sinal, tamanho, fracao);
