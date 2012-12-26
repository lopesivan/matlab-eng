function subterfugio = conversao_y_d(z1, z2, z3)

a = z1*z2+z2*z3+z3*z1;

za = a/z1;
zb = a/z2;
zc = a/z3;

subterfugio.za = za;
subterfugio.zb = zb;
subterfugio.zc = zc;

