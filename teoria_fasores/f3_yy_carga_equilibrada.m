% Sistema trifásico YD equilibrado
% Y = ligação estrela das fontes
% D = ligação delta das carga
% vl = tensão de linha
% f = frequencia de operação
% zl = carga
function saida = f3_yy_carga_equilibrada(vl, zl)
vp = abs(vl/sqrt(3));   % tensão de fase
ip = abs(vp/zl);        % corrente de fase
il = ip;                % corrente de linha
oz = angle(zl);         % ângulo da carga
p = 3*vp*ip*cos(oz);    % potência ativa da carga
q = p*tan(oz);          % potência reativa da carga
s = p+q*1i;             % potência complexa
pa = abs(s);            % potência aparente

saida.vp = vp;
saida.ip = ip;
saida.il = il;
saida.oz = oz;
saida.p = p;
saida.q = q;
saida.s = s;
saida.pa = pa;

end