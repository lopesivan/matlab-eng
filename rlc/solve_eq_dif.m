function out = solve_eq_dif(f, c1, c2, rf, DEBUG)

syms t A1 A2

% -----------

f1 = f-c1+rf;
df = subs(diff(f1, t)-c2, t, 0);
f1 = subs(f1, t, 0);

s = solve(f1, df, A1, A2);

% -----------

if DEBUG == 1
    disp('sistema:');
    disp(f1);
    disp(df);
    disp('val. das constantes:');
    disp(s.A1);
    disp(s.A2);    
end

% -----------

out.A1 = s.A1;
out.A2 = s.A2;
