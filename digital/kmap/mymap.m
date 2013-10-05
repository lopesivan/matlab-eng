% /*=============================Descriptions============================
% 		Generate Maps:
% 		f(i,j)	-	A function converts each two decimal number to gray code,
% 					then concatenate them together become a binary code. 
% 					After that, convert it again to decimal number.
% 					i, j is decimal number (in string???)
% 					
% 		Generate 1-1, 1-2, 1-4, 2-2, 2-4, and 4-4 maps according to the maps
% 		show below:
%
%        j:   0  1  2  3 
% 			 00 01 11 10
% 			+--+--+--+--+
% 		0 00| 0| 1| 3| 2|
% 			+--+--+--+--+
% 	i:  1 01| 4| 5| 7| 6|
% 			+--+--+--+--+
% 		2 11|12|13|15|14|
% 			+--+--+--+--+
% 		3 10| 8| 9|11|10|
% 			+--+--+--+--+	
% 		Total maps = 16 + 32 + 8 + 16 + 8 + 1 = 81
% 		gray2i(strDec) , gray2j(strDec)	- Functions that convert the Gray Code
% 										  to i-axis value and j-axis value.
% 		convert(str)	- 	Conversion: 0->complement, 1->non-complement, _->skip
% 							Example: 01_1 -> A'BD	// C was skip
% 	=====================================================================*/
function map = mymap(i,j)
% Generate Maps as below:       
%                               How to do it?
%        j:   0  1  2  3        Solution:
% 			 00 01 11 10        % Converts each two decimal number to gray code,
% 			+--+--+--+--+       % then concatenate them together become a binary code. 
% 		0 00| 0| 1| 3| 2|       % After that, convert it again to decimal number.
% 			+--+--+--+--+       % i, j is string or number.
% 	i:  1 01| 4| 5| 7| 6|
% 			+--+--+--+--+
% 		2 11|12|13|15|14|
% 			+--+--+--+--+
% 		3 10| 8| 9|11|10|
% 			+--+--+--+--+	
%
% map : A 4x4 matrix which is same as above.
%       OR a single value (i,j) are accepted.
% i,j : integer (0-3 for 4x4 Kmap), string or number

if nargin == 0
    map = zeros(4,4);    
    for i = 0:3
        for j = 0:3            
            map(i+1,j+1) = str2num(mybin2dec([mydec2gray(num2str(i)) mydec2gray(num2str(j))]));
        end
    end
elseif nargin == 2
    i = num2str(i); 
    j = num2str(j);
    map = str2num(mybin2dec([mydec2gray(i) mydec2gray(j)]));
else
    disp('Error! Please refer to HELP MYMAP function.');
end
end % function