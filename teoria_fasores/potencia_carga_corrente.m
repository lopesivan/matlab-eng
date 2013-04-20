% pot�ncia complexa, pela rela��o carga corrente:
% S = z * Irms^2
% onde:
% S - potencia complexa(vetor)
% Irms - corrente rms aplicada na carga z(vetor ou n�o)
% z - carga(vetor)
function potencia = potencia_carga_corrente(irms, z)
    potencia.complexa = (abs(irms)^2)*z;
end
