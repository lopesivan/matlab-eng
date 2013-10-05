function strDec = mybin2dec(strBin)
% Conversion Binary Code To Decimal Number
% strBin : binary number in string
% strDec : decimal number in string.
% Example: mybin2dec('1010') will gets '10'

dec = 0;
len = length(strBin);
for i = len:-1:1
	dec = dec + str2num(strBin(i)) * power(2,len-i);
end

strDec = num2str(dec);
end % function