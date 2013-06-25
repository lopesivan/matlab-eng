% Algoritimo para calculo de resistência de aterramento para uma
% configuração em quadrado cheio.
% Codigo original por Rooney Coelho, rooneycoelho at hotmail at com

function saida = quadradoCheio(m, n, esp, phoa, L, d)

R = zeros(m, n);
%Rpropria = (phoa/(2*pi*L))*log((4*L)/(d*2.54e-2));
Rpropria = (phoa/(2*pi*L))*log((4*L)/(d))

for i=1:m
    for j=1:n
        for x=1:m
            for y=1:n
                if (i==x)&&(j==y)
                    R(i, j) = R(i, j)+Rpropria
                else
                    e = sqrt((i-x)^2+(j-y)^2);
                    e = e*esp;
                    b = sqrt(L^2+e^2);
                    aux = (phoa/(4*pi*L))*log(((b+L)^2-e^2)/(e^2-(b-L)^2));
                    R(i, j) = R(i, j) + aux;
                end
            end
        end
    end
end

Raux = 0;
for i=1:m
    for j=1:n
        Raux = Raux+1/R(i, j);
    end
end

Req = 1/Raux;

saida.res = Req;

end