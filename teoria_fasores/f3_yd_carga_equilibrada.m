% Sistema trif�sico YD equilibrado
% Y = liga��o estrela das fontes
% D = liga��o delta das carga
% vl = tens�o de linha
% f = frequencia de opera��o
% zl = carga
function saida = f3_yd_carga_equilibrada(vl, zl)
vp = abs(vl);               % tens�o de fase (eficazes)
ip = abs(vl/zl);            % corrente de fase (eficazes)
il = abs(sqrt(3)*ip);       % corrente de linha (eficazes)
oz = angle(zl);             % �ngulo da carga
p = sqrt(3)*vl*il*cos(oz);  % pot�ncia ativa da carga
q = sqrt(3)*vl*il*sin(oz);  % pot�ncia reativa da carga
s = p+q*1i;                 % pot�ncia complexa
pa = abs(s);                % pot�ncia aparente

saida.vp = vp;
saida.ip = ip;
saida.il = il;
saida.oz = oz;
saida.p = p;
saida.q = q;
saida.s = s;
saida.pa = pa;

end
