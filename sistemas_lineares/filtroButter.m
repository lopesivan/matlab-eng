function saida = filtroButter(sinal, ordem, frequenciaAmostragem)

[B, A] = butter(ordem, 20/(frequenciaAmostragem/2));
saida = filter(B, A, sinal);

end