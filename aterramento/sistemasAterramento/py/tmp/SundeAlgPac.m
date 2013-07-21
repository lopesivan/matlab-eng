function [PopFx,fx1] = SundeAlgPac(PopIn,N,a,ROa,Passo)
%*******Dados Manipulados*******
PopIn = abs(PopIn);
D = a;%valores das distancias entre as hastes em metros
d = D(1):Passo:D(end);
Fx = [];
CurveTeor = [];
CurveExpe = [];
Error = [];
for ia = 1:size(PopIn,1)
    
    p = (PopIn(ia,[1:N])); %layers resistivity
    h = (PopIn(ia,N+1:end));%layers thickness
    %*******Inicio do Algoritmo de Sunde*******
    %*******Determina ̧ao dos valores E1********
    for a = 1:size(d,2)
        e(a) = a/size(d,2);
    end
    
    %*******Determinacao do termo independente nb*******
    for a = 1:N-1
    k(a)= (p(a+1) - p(a))/(p(a+1) + p(a));
    end
    
    for a = 1:size(d,2)
        arg1 = e(a);
        arg2 = h(N-1)/h(1);
        f(N-1) = (1 + k(N-1)*(arg1 ^ arg2))/(1 - k(N-1)*(arg1 ^ arg2));
        
    for b = 1:N-2
        kl(N-1-b) = (1 - k(N-1-b) - f(N-b)*(1 + k(N-1-b)))/(1 - k(N-1-b) + f(N-b)*(1 + k(N-1-b)));
        r(N-1-b) = h(N-1-b)/h(1);
        f(N-1-b) = (1 - kl(N-1-b)*(arg1^r(N-1-b)))/(1 + kl(N-1-b)*(arg1^r(N-1-b)));
    end
    
    a3(a,1) = f(1) - 1;
    
    end
%*******Determina ̧ao da matriz E1*******

    for a = 1:size(d,2)
        for b = 1:size(d,2)
            e1(a,b) = e(a)^b;
        end
    end
    
    matE1 = e1;
%*******Determinacao de X*******
    x40 = matE1 * a3;
%*******Calculo da resistividade aparente teorica*******
    for a = 1:size(d,2)
    hh = h(1)/d(a);
    ra1 = Passo;
    for b = 1:size(d,2)
        rr(b) = x40(b,1)*((1/sqrt(4*hh*hh*b*b+1)) - (1/(2*sqrt(hh*hh*b*b+1))));
        ra1 = ra1 + rr(b);
    end
    ra2(a) = 2*ra1;
    ppa(a) = p(1)*ra2(a);
    end
    
    for ia = 1:size(d,2)
        for ib = 1:size(D,2)
            if d(ia) == D(ib)
                Dd(ib) = ia;
            end
        end
    end

    dx = D(1):Passo:D(end);
    PPA = ppa(Dd);
    TT = interp1(D, PPA,dx,'spline');
    EE = interp1(D, ROa,dx,'spline');
    %*******Funtion Evaluation*******
    for ib = 1:size(ROa,2)
        fx1(ib) = ((ROa(ib) - PPA(ib))/(ROa(ib)))*100;
    end
    
    fx2 = sum(abs(fx1));
    Fx(end+1,1) = fx2;
    CurveTeor(end+1,:) = PPA;
    CurveExpe(end+1,:) = ROa;
    Error(end+1,:) = fx1;
    
    %*******Graficos*******
    figure(1); grid on; subplot(2,3,1);
    plot(dx,TT,'k-','LineWidth', 1.5);
    hold on; title('Curva de Resistividade Experimental & Teorica');

    xlabel('a [m]'); ylabel('Ro(a) [Ohm x m]')
    plot(dx,EE,'r-','LineWidth', 1.5);
    plot(D,PPA,'go','LineWidth', 2);
    plot(D,ROa,'bo','LineWidth', 2);
    hold off;
end

PopFx = [Fx PopIn];

