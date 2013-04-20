% Potência complexa
% S = Vrms*conj(Irms)
% onde:
% S - a potência complexa(vetor)
% Vrms - a tensão rms(vetor)
% Irms - a corrente rms
function potencia = potencia_complexa(potencia_ativa, potencia_reativa)
    if potencia_reativa < 0
        potencia.tipo = 'capacitiva';
    elseif potencia_reativa > 0
        potencia.tipo = 'indutiva';
    else
        potencia.tipo = 'resistiva';
    end

    potencia.complexa = potencia_ativa + 1i*potencia_reativa;
    potencia.aparente = abs(potencia.complexa);
    potencia.fator_potencia = angle(potencia.complexa);
    potencia.fator_potencia_angulo = acosd(potencia.fator_potencia); % em graus
end
