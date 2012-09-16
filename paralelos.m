%
% vetor ou matriz com os resistores que estao em paralelo
% Felipe Bandeira, 13/09/2012 - 18:52
%

function out = paralelos(v)

out = 1/sum(v.^-1);
