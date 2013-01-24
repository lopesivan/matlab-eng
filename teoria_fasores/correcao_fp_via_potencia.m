% Correção do fator de potência apartir da potencia real e o fator de
% potência de cada carga.
% -- entrada:
% vrms = tensão(complexa) rms da fonte
% freq = frequencia da fonte
% fpdesejado = fator de potência desejado, positivo(atrasado),
% negativo(adiantado)
% pt = potência real da carga ou cargas(vetor)
% fp = fator de potência da carga ou das cargas(vetor)
%
% -- exemplo:
% problema 12.33 do Johnson
% 
% Uma carga é alimentada da potência complexa S = 6+j8 VA por uma fonte de
% tensão de 10cos(100t) V. Calcule a capacitância que deve ser conectada em
% paralelo com a carga para que o fator de potência visto pela fonte seja
% a) unitário
% b) 0.8(atrasado)
%
% resolvendo:
%
% do problema temos que a potência real da carga é de 6 W
% o fator de potência da carga é dado pela relação cos(atan(8/6)) = 0.6
% caracterizando uma carga do tipo indutiva. A tensão de pico da fonte é
% 10 V logo a sua eficaz é 10/sqrt(2) = 7.0711, com frequência de 
% ~15.9155 hertz. Para o item (a) o fator de potência desejado é 1.
% entrando com esses dados no programa:
% vrms = 7.0711
% freq = 15.9155
% fpdesejado = 1
% pt = 6
% fp = 0.6
% temos:
% correcao_fp_via_potencia(7.0711, 15.9155, 1, 6, 0.6)
% o que nos leva:
% capacitor de 1.6e-3 F ou 1.6mF
% o item (b) é resolvido da mesma forma, logo:
% correcao_fp_via_potencia(7.0711, 15.9155, 0.8, 6, 0.6)
% que nos dá:
% um capacitor de 700uF.
function correcao = correcao_fp_via_potencia(vrms, freq, fpdesejado, pt, fp)
potencia = potencia_n_cargas(pt, fp, abs(vrms));
correcao = correcao_fator_potencia(fpdesejado, real(potencia.carga), imag(potencia.carga), f_w(freq));
