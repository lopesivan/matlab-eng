function strBin = mydec2bin(strDec,nbits)
% Conversion Decimal Number To Binary Code
% strDec : decimal number in string.
% nbits  : indicate how many binary bits are display
% strBin : binary number in string
% Example: mydec2bin('12') will gets '1100'
%          mydec2bin('12',8) will gets '00001100'

dec = str2num(strDec);
strBin = '';	

if dec == 0
    strBin = '00';
else 
    while dec > 0
        strBin = [num2str(mod(dec,2)) strBin];
		dec = floor(dec / 2);
    end
end	
	
if nargin == 1    
    if mod(length(strBin),2) ~= 0
        strBin = [num2str(0) strBin];
    end     
else
    for nzero = 1:nbits - length(strBin)
        strBin = [num2str(0) strBin];
    end
end

end % function