% pot�ncia complexa, pela rela��o carga tens�o:
% S = (Vrms^2)/z
% onde:
% S - potencia complexa(vetor)
% Vrms - tens�o rms aplicada na carga z(vetor ou n�o)
% z - carga(vetor)
function potencia = potencia_carga_tensao(vrms, z)
    potencia.complexa = (abs(vrms)^2)/conj(z);
end
