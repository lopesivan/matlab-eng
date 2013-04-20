% potência complexa, pela relação carga corrente:
% S = z * Irms^2
% onde:
% S - potencia complexa(vetor)
% Irms - corrente rms aplicada na carga z(vetor ou não)
% z - carga(vetor)
function potencia = potencia_carga_corrente(irms, z)
    potencia.complexa = (abs(irms)^2)*z;
end
