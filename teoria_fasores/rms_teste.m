clc;
v = @(t) 1.6482+330.7e-3*sin(t);
x = 0:0.1:2*pi;
length(x)
y = v(x);
y2 = y.^2;
s = sum(y2);
p = s/length(x);
vrms = sqrt(p)
