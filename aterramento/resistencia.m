function R = resistencia(pho, a, p)
R = (1 + (2*a)/sqrt(a^2+(2*p)^2) - (2*a)/sqrt((2*a)^2+(2*p)^2)) * pho/(4*pi*a);
end