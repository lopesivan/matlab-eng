function out = myconvert(str)
% Conversion: 
%     0 -> complement
%     1 -> non-complement
%     _ -> skip
% Example: 01_1 -> A'BD	// C was skip
%
% str : string. Contains chars which may be '_', '0' or '1'. 
%   1st char -> A
%   2nd char -> B
%   3rd char -> C
%   4th char -> D
% out : string. Example: 01_1 -> A'BD

out = '';
for i=1:length(str)		
    if str(i) == '_'
        continue;
	else
		out = [out char(i+64)];
		if str(i) == '0', out = [out char(39)]; % char(39) -> ', end
    end
end
end % function
