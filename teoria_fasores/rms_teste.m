clc;
v = @(t) 10*sin(t);
x = 0:0.1:1*pi;
length(x)
y = v(x);
y2 = y.^2;
s = sum(y2);
p = s/length(x);
vrms = sqrt(p)
