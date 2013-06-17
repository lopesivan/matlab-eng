syms p1 k h;

pho = [320 245 182 162 168 152];
a = [2.5 5 7.5 10 12.5 15];

q = 6;
infinito = 6;

parte1 = 0;
fpho = 0;
for i = 1:q
    for n = 1:infinito
        parte1 = parte1 + (k^n/sqrt(1+(2*n*h/a(i))^2) - k^n/sqrt(4+(2*n*h/a(i))^2));
    end
    parte1 = p1*(1 + 4*parte1);
    fpho = a(i) - parte1;
end

%fun = @(a, b, c) subs(fpho,{p1, k, h}, {a, b, c});
%f = matlabFunction(fpho, 'file', '');
f = matlabFunction(fpho, 'file', 'fphom', 'vars', [p1 k h], 'outputs', {'phon'});
