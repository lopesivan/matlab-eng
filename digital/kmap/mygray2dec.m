function strDec = mygray2dec(strGray)
% Conversion Gray Code To Decimal Number
% strGray: Gray code in string.
% strDec : decimal number in string
% Example: mygray2dec('11') will gets '2'

strDec = mybin2dec(mygray2bin(strGray));

end % function