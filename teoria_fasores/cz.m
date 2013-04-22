% transforma��o indut�ncia capacitiva para valor do capacitor
% entrada:
% z - imped�ncia do capacitor
% f - frequencia(Hertz)
function c = cz(z, f)

    c = -1i/(2*pi*f*z);
    
end
