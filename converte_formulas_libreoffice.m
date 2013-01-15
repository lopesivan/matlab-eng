% clc
% clear all
% syms a b
% 
% f = a/2 + b + a^2/2
% 
% pretty(f);
% fs = char(f);
% 
% s = regexprep(fs, '/', 'over')

function subterfugio = converte_formulas_libreoffice(formula)

s = regexprep(formula, '/', ' over ');
s = regexprep(s, '(', '{');
s = regexprep(s, ')', '}');
s = regexprep(s, '*', ' ');

subterfugio = s;
