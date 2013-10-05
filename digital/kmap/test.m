%kmap=[ 0  1  1  1;
%       0  1  1  1; 
%       0  0  0  1;
%       1  0  0  0];
% ANSWER: A'D + A'B' + B'C'D' + BCD'
% PROBLEM: A'D + A'B' + A'C + B'C'D' + BCD'

kmap = [1 0 0 1; 0 0 0 0; 0 0 0 0; 0 0 0 0;]

X = 2;  % to indicate the portion of the kmap is get once.
   
% Compare and generate 4x4
if sum(sum(kmap)) == 16
    disp(1)
    return;
end
       
% Compare and generate 2x4 
for i=0:3	
    m = kmap([i+1 mod(i+1,4)+1],:);    
    if isequal(m,ones(2,4)+ones(2,4))
        ;   % do nothing
    else
        m = changem(m,1,2);        
        % horizontal    
        % v = sum(kmap');
        % if isequal([v(i+1) v(mod(i+1,4)+1)],[4 4])
        if isequal(m,ones(2,4))
            temp = '';
            for p=1:2
                a = mydec2gray(num2str(i));
                b = mydec2gray(num2str(mod((i+1),4)));
                if a(p) == b(p)
                    temp = [temp a(p)];               
                else
                    temp = [temp '_'];
                end							
            end        
            temp = [temp '__'];
            disp(myconvert(temp));  % for horizontal
            kmap([i+1 mod(i+1,4)+1],:) = ones(2,4)+ones(2,4);
        end
    end
    
    m = kmap(:,[i+1 mod(i+1,4)+1]);    
    if isequal(m,ones(4,2)+ones(4,2))
        ;   % do nothing        
    else
        m = changem(m,1,2);
        % vertical
        % v = sum(kmap);
        % if isequal([v(i+1) v(mod(i+1,4)+1)],[4 4])
        if isequal(m,ones(4,2))
            temp = '';
            for p=1:2
                a = mydec2gray(num2str(i));
                b = mydec2gray(num2str(mod((i+1),4)));
                if a(p) == b(p)
                    temp = [temp a(p)];               
                else
                    temp = [temp '_'];
                end							
            end 
            temp = ['__' temp];
            disp(myconvert(temp));  % for vertical
            kmap(:,[i+1 mod(i+1,4)+1]) = ones(4,2)+ones(4,2);
        end
    end
end
   
% Compare and generate 2x2
for i=0:3
	for j=0:3
        m = [kmap(i+1,j+1) kmap(i+1,mod(j+1,4)+1);
             kmap(mod(i+1,4)+1,j+1) kmap(mod(i+1,4)+1,mod(j+1,4)+1)];
        if isequal(m,ones(2,2)+ones(2,2))
            ; % donothing
        else
            m = changem(m,1,2);
            if isequal(m,[1 1; 1 1])
                temp = '';
                for p=1:2
                    a = mydec2gray(num2str(i));
                    b = mydec2gray(num2str(mod((i+1),4)));
                    if a(p) == b(p)
                        temp = [temp a(p)];                
                    else
                        temp = [temp '_'];
                    end							
                end
                for p=1:2
                    a = mydec2gray(num2str(j));
                    b = mydec2gray(num2str(mod((j+1),4)));
                    if a(p) == b(p)				
                        temp = [temp a(p)];               
                    else
                        temp = [temp '_'];
                    end							
                end        
                disp(myconvert(temp));
                kmap(i+1,j+1) = 2;
                kmap(i+1,mod(j+1,4)+1) = 2;
                kmap(mod(i+1,4)+1,j+1) = 2;
                kmap(mod(i+1,4)+1,mod(j+1,4)+1) = 2;
            end
        end
    end
end   
       
% Comapre and generate 1x4 
for i=0:3
    m = kmap(i+1,:);
    if isequal(m,ones(1,4)+ones(1,4))
        ; %do nothing
    else
        m = changem(m,1,2);
        % Hoizontal lines
        if isequal(m,[1 1 1 1])
            temp = mydec2gray(num2str(i));
            disp(myconvert(temp));
            kmap(i+1,:) = 2;
        end
    end

    m = kmap(:,i+1);
    if isequal(m,ones(4,1)+ones(4,1))
        ; %do nothing
    else
        m = changem(m,1,2);    
        % Vertical lines
        if isequal(m,[1;1;1;1])
            temp = ['__' mydec2gray(num2str(i))];
            disp(myconvert(temp));
            kmap(:,i+1) = 2;
        end
    end
end   
       
% Compare and generate 1x2 
for i=0:3
	for j=0:3
        m = [kmap(i+1,mod(j,4)+1) kmap(i+1,mod(j+1,4)+1)];
        if isequal(m,ones(1,2)+ones(1,2))
            ; % do nothing
        else
            m = changem(m,1,2);
            % compare horizontal
            if isequal(m, [1 1]) 
                temp = '';
                for p=1:2   % 2 bits: '00','01','10','11'
                    a = mydec2gray(num2str(j));
                    b = mydec2gray(num2str(mod((j+1),4)));
                    if a(p) == b(p)				
                        temp = [temp a(p)];
                    else
                        temp = [temp '_'];
                    end            
                end            
                temp = [mydec2gray(num2str(i)) temp];  % for horizontal
                disp(myconvert(temp));   
                kmap(i+1,mod(j,4)+1) = 2;
                kmap(i+1,mod(j+1,4)+1) = 2;
            end	
        end
        
        m = [kmap(mod(j,4)+1,i+1);kmap(mod(j+1,4)+1,i+1)];
        if isequal(m,ones(2,1)+ones(2,1))
            ; % do nothing
        else
            m = changem(m,1,2);        
            % compare vertical
            if isequal(m, [1;1]) 
                temp = '';
                for p=1:2   % 2 bits: '00','01','10','11'
                    a = mydec2gray(num2str(j));
                    b = mydec2gray(num2str(mod((j+1),4)));
                    if a(p) == b(p)				
                        temp = [temp a(p)];
                    else
                        temp = [temp '_'];
                    end            
                end  
                temp = [temp mydec2gray(num2str(i))];  % for vertical
                disp(myconvert(temp));
                kmap(mod(j,4)+1,i+1) = 2;
                kmap(mod(j+1,4)+1,i+1) = 2;
            end	
        end        
    end                
end   
       
       
% Compare and generate 1x1
for i=0:3
	for j=0:3        
        if kmap(i+1,j+1) == 1
            temp = [mydec2gray(num2str(i)) mydec2gray(num2str(j))];
            disp(myconvert(temp))
            kmap(i+1,j+1) = 2;
        end
    end
end
