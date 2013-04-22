% Transforma��o imped�ncia indutiva para valor do indutor
% entrada
% z - imped�ncia do indutor
% f - freq��ncia (Hertz)
function l = lz(z, f)

    l = z/(2*pi*f*1i);
    
end
