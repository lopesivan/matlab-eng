% vetor ou matriz com os resistores(impedância) que estão em paralelo
function o = pz(v)

o = 1/sum(v.^-1);
