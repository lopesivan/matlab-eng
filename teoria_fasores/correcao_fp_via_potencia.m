% Corre��o do fator de pot�ncia apartir da potencia real e o fator de
% pot�ncia de cada carga.
% -- entrada:
% vrms = tens�o(complexa) rms da fonte
% freq = frequencia da fonte
% fpdesejado = fator de pot�ncia desejado, positivo(atrasado),
% negativo(adiantado)
% pt = pot�ncia real da carga ou cargas(vetor)
% fp = fator de pot�ncia da carga ou das cargas(vetor)
%
% -- exemplo:
% problema 12.33 do Johnson
% 
% Uma carga � alimentada da pot�ncia complexa S = 6+j8 VA por uma fonte de
% tens�o de 10cos(100t) V. Calcule a capacit�ncia que deve ser conectada em
% paralelo com a carga para que o fator de pot�ncia visto pela fonte seja
% a) unit�rio
% b) 0.8(atrasado)
%
% resolvendo:
%
% do problema temos que a pot�ncia real da carga � de 6 W
% o fator de pot�ncia da carga � dado pela rela��o cos(atan(8/6)) = 0.6
% caracterizando uma carga do tipo indutiva. A tens�o de pico da fonte �
% 10 V logo a sua eficaz � 10/sqrt(2) = 7.0711, com frequ�ncia de 
% ~15.9155 hertz. Para o item (a) o fator de pot�ncia desejado � 1.
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
% o item (b) � resolvido da mesma forma, logo:
% correcao_fp_via_potencia(7.0711, 15.9155, 0.8, 6, 0.6)
% que nos d�:
% um capacitor de 700uF.
function correcao = correcao_fp_via_potencia(vrms, freq, fpdesejado, pt, fp)
potencia = potencia_n_cargas(pt, fp, abs(vrms));
correcao = correcao_fator_potencia(fpdesejado, real(potencia.carga), imag(potencia.carga), f_w(freq));
