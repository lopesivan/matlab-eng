function retorno = rlc_serie_forc(R, L, C, f0, f1, rf, DEBUG)

if nargin == 0
    R = input('R= ');
    L = input('L= ');
    C = input('C= ');
    f0 = input('f0= ');
    f1 = input('f1= ');
    rf = input('rf= ');
    DEBUG = 1;
end

retorno = rlc_nucleo(R, L, C, rf, f0, f1, 1, DEBUG);

end