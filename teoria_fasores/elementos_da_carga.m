% Simples programa para o cálculo dos valores da parte indutiva ou
% capacitiva de uma carga
function componente = elementos_da_carga(carga, frequencia)

R = real(carga);

indutor = 0;
capacitor = 0;
    
if (imag(carga) > 0)
    indutor = imag(carga)/(frequencia*2*pi);
elseif (imag(carga) < 0)
    capacitor = 1/(abs(imag(carga))*frequencia*2*pi);
end

componente.resistencia = R;
componente.capacitor = capacitor;
componente.indutor = indutor;

end
