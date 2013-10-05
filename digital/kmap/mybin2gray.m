function strGray = mybin2gray(strBin)
% Conversion Binary Code To Gray Code
% strBin : binary number in string
% strGray: Gray code in string.
% Example: mybin2gray('1010') will gets '1111'

strGray = strBin(1);
for i=2:length(strBin)
    strGray = [strGray num2str(xor(str2num(strBin(i-1)),str2num(strBin(i))))];    
end
	
end % funtion