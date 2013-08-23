% Prática de laboratório 1
% Aluno:
% - Felipe Bandeira da Silva, 1020942-X

disp('1 - Defina duas variáveis de números reais...')

x = 1.1
y = 2.2

r1 = x + y
r2 = y - x
r3 = x * y
r4 = y / x
r5 = x ^ y 
r6 = sin(x) + cos(y)
r7 = exp(x)*log(y)
r8 = sqrt(x*y)
p = input('Proximo item[ENTER]?');

disp('2 - Defina duas variáveis de números complexos...')

cx = 1+2j
cy = 2+3j

r9 = abs(cx)
r10 = angle(cy)
r11 = rad2deg(r10)
r12 = real(cx*cy)
r13 = imag(cx/cy)
r14 = x*conj(cy)
r15 = atan(imag(cx)/real(cx))
p = input('Proximo item[ENTER]?');

disp('3 - Defina duas listas contendo cinco números reais...')

lx = [1 2 3 4 5]
ly = [6;7;8;9;10]

r16 = sum(lx)
r17 = prod(ly)
r18 = lx*ly
r19 = lx.*ly'
r20 = lx(5)/ly(2)
r21 = lx+ly'
p = input('Proximo item[ENTER]?');

disp('4 - Defina uma matriz...')

M = [3 7 9; 1 5 5; 8 7 0]
Mt = M'
Ms = sum(M(1,:))
Mi = inv(M)
Md = det(M)
p = input('Proximo item[ENTER]?');

disp('5 - Crie um vetor de 1000 pontos...')
t = 0:0.01:10;

x1 = 5*exp(-t).*sin(2*t)+2*exp(-t).*cos(2*t);
x2 = exp(-2*t);

plot(t, x1, t, x2)
p = input('Proximo item[ENTER]?');

disp('6 - Encontre o valor mínimo...')

x = -20:1:20;
f = x.^2-8*x+4;

minimo = f(1);
for I=2:length(f)
    if f(I) < minimo
        minimo = f(I);
        posicao = I;
    end
end

disp('Menor valor:')
disp(minimo)
disp('Posicao:')
disp(posicao)

