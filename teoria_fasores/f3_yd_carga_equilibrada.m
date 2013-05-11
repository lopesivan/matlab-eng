% Sistema trifásico YD equilibrado
% Y = ligação estrela das fontes
% D = ligação delta das carga
% vl = tensão de linha
% f = frequencia de operação
% zl = carga
function saida = f3_yd_carga_equilibrada(vl, zl)
vp = abs(vl);               % tensão de fase (eficazes)
ip = abs(vl/zl);            % corrente de fase (eficazes)
il = abs(sqrt(3)*ip);       % corrente de linha (eficazes)
oz = angle(zl);             % ângulo da carga
p = sqrt(3)*vl*il*cos(oz);  % potência ativa da carga
q = sqrt(3)*vl*il*sin(oz);  % potência reativa da carga
s = p+q*1i;                 % potência complexa
pa = abs(s);                % potência aparente

saida.vp = vp;
saida.ip = ip;
saida.il = il;
saida.oz = oz;
saida.p = p;
saida.q = q;
saida.s = s;
saida.pa = pa;

end
