function retorno = rlc_serie_forc(R, L, C, f0, f1, rf, DEBUG)

if nargin == 0
    R = input('R= ');
    L = input('L= ');
    C = input('C= ');
    f0 = input('f0= ');
    f1 = input('f1= ');
    rf = input('rf= ');
    DEBUG = 1;
elseif nargin <= 2
    if strcmp(R, '-a')
        disp('argumentos:');
        disp('R, L, C, f0, f1, rf, DEBUG');
        disp('f0 = condição inicial para f(t=0)');
        disp('f1 = condição inicial para df(t=0)');
    else
        disp('comandos disponiveis:');
        disp('-a = ajuda');
    end
    return;
end

retorno = rlc_nucleo(R, L, C, rf, f0, f1, 1, DEBUG);

end