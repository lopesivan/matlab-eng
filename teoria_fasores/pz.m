% vetor ou matriz com os resistores(imped�ncia) que est�o em paralelo
function o = pz(v)

o = 1/sum(v.^-1);
