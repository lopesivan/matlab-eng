function strBin = mygray2bin(strGray)
% Conversion Gray Code To Binary Code
% strGray: Gray code in string.
% strBin : binary number in string
% Example: mygray2bin('11') will gets '10'

strBin = strGray(1);
for i=2:length(strGray)    
    strBin = [strBin num2str(xor(str2num(strBin(length(strBin))),str2num(strGray(i))))]; 
end

end % function
		