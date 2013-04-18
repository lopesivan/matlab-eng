function estabilidade(raizes)
    est = 0;
    ins = 0;
    mar = 0;

    for x=1:length(raizes)
        if real(raizes(x)) < 0
            est = est + 1;
        elseif real(raizes(x)) > 0
            ins = ins + 1;
        elseif real(raizes(x)) == 0
            mar = mar + 1;
        end
    end

    if ins > 0
        disp('sistema instavel');
    else
        disp('sistema estavel');
    end
end