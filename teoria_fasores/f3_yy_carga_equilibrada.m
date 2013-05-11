% Sistema trif�sico YD equilibrado
% Y = liga��o estrela das fontes
% D = liga��o delta das carga
% vl = tens�o de linha
% f = frequencia de opera��o
% zl = carga
function saida = f3_yy_carga_equilibrada(vl, zl)
vp = abs(vl/sqrt(3));   % tens�o de fase
ip = abs(vp/zl);        % corrente de fase
il = ip;                % corrente de linha
oz = angle(zl);         % �ngulo da carga
p = 3*vp*ip*cos(oz);    % pot�ncia ativa da carga
q = p*tan(oz);          % pot�ncia reativa da carga
s = p+q*1i;             % pot�ncia complexa
pa = abs(s);            % pot�ncia aparente

saida.vp = vp;
saida.ip = ip;
saida.il = il;
saida.oz = oz;
saida.p = p;
saida.q = q;
saida.s = s;
saida.pa = pa;

end