function [i,j] = mygray2ij(strDec)	
% Conversion Decimal Number To Binary Code, Then separate Into Two
% Substring And Convert To Decimal Number.
% For example:    
%     strDec = '14' is equivalent to strBin = '1110', then
%     separate '1110' into two sections: '11' and '10'. After that,
%     '11' and '10' from gray codes convert to decimal number:
%     strGray = '11' is equivalent to strDec = '3', and
%     strGray = '10' is equivalent to strDec = '2'.
%
% i,j : Integer number. are the coordinates of kmap.
%
% See also: mymap.m for further information.

strBin = mydec2bin(strDec);

while length(strBin) <= 4
    strBin = ['0' strBin];
end

len = length(strBin);
stri = strBin(1:uint8(len/2));
strj = strBin(uint8(len/2+1):len);
i = str2num(mygray2dec(stri));
j = str2num(mygray2dec(strj));

end % function
