% Transformação impedância indutiva para valor do indutor
% entrada
% z - impedância do indutor
% f - freqüência (Hertz)
function l = lz(z, f)

    l = z/(2*pi*f*1i);
    
end
