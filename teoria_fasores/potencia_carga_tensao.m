% potência complexa, pela relação carga tensão:
% S = (Vrms^2)/z
% onde:
% S - potencia complexa(vetor)
% Vrms - tensão rms aplicada na carga z(vetor ou não)
% z - carga(vetor)
function potencia = potencia_carga_tensao(vrms, z)
    potencia.complexa = (abs(vrms)^2)/conj(z);
end
