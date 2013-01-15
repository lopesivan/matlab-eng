function subterfugio = converte_formulas_libreoffice(formula)

s = regexprep(formula, '/', ' over ');

subterfugio = s;
