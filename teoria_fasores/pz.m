% vetor ou matriz com os resistores(imped�ncia) que est�o em paralelo
% resultado: resist�ncia equivalente.
function o = pz(v)

o = 1/sum(v.^-1);
