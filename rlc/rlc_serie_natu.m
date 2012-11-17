function retorno = rlc_serie_natu(R, L, C, f0, f1, DEBUG)

if nargin == 0
    R = input('R= ');
    L = input('L= ');
    C = input('C= ');
    f0 = input('f0= ');
    f1 = input('f1= ');
    DEBUG = 1;
end

retorno = rlc_nucleo(R, L, C, 0, f0, f1, 1, DEBUG);

end
