function strGray = mydec2gray(strDec)
% Conversion Decimal Number To Gray Code
% strDec : decimal number in string
% strGray: Gray code in string.
% Example: mydec2gray('2') will gets '11'

strGray = mybin2gray(mydec2bin(strDec));	

end % function