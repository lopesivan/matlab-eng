% -------------- Generate Kmap solutions -----------------
% In Kmap, we have 
% 1x1,                For  1 
% 1x2 or 2x1,         For  2
% 1x4 or 4x1 and 2x2, For  4
% 2x4 or 4x2,         For  8
% 4x4.                For 16

% ----------------- 1x1 ------------------------------------------

% % Generate 1-1 maps and codes	(n = 16 solutions)
% for i=0:3
% 	for j=0:3		
% 		temp = [mydec2gray(num2str(i)) mydec2gray(num2str(j))];
%       disp([num2str(mymap(i,j)) ': ' myconvert(temp)])		
%     end
% end

% Outputs:
% 0: A'B'C'D'
% 1: A'B'C'D
% 3: A'B'CD
% 2: A'B'CD'
% 4: A'BC'D'
% 5: A'BC'D
% 7: A'BCD
% 6: A'BCD'
% 12: ABC'D'
% 13: ABC'D
% 15: ABCD
% 14: ABCD'
% 8: AB'C'D'
% 9: AB'C'D
% 11: AB'CD
% 10: AB'CD'

% ----------------------------------------------------------------

% ----------------- 1x2 and 2x1 ----------------------------------

% % Generate 1-2 maps and codes	(n = 32 solutions)
% for i=0:3
% 	for j=0:3
% 		temp = '';
%         for p=1:2   % 2 bits: '00','01','10','11'
%             a = mydec2gray(num2str(j));
%             b = mydec2gray(num2str(mod((j+1),4)));
% 			if a(p) == b(p)				
% 				temp = [temp a(p)];
% 			else
% 				temp = [temp '_'];
%             end            
%         end
%         temp2 = temp;
%         temp = [mydec2gray(num2str(i)) temp2];  % for horizontal
%         disp(myconvert(temp));        
%         temp = [temp2 mydec2gray(num2str(i))];  % for vertical
%         disp(myconvert(temp));		
%     end                
% end

% Outputs:
% A'B'C'
% A'C'D'
% A'B'D
% BC'D'
% A'B'C
% AC'D'
% A'B'D'
% B'C'D'
% A'BC'
% A'C'D
% A'BD
% BC'D
% A'BC
% AC'D
% A'BD'
% B'C'D
% ABC'
% A'CD
% ABD
% BCD
% ABC
% ACD
% ABD'
% B'CD
% AB'C'
% A'CD'
% AB'D
% BCD'
% AB'C
% ACD'
% AB'D'
% B'CD'

% ----------------------------------------------------------------

% % ----------------- 1x4 and 4x1 ----------------------------------
% 
% % Generate 1-4 maps and codes	(n = 8 solutions)
% for i=0:3
% 	% Hoizontal lines
% 	temp = mydec2gray(num2str(i));
% 	disp(myconvert(temp));
% 	
% 	% Vertical lines
% 	temp = ['__' mydec2gray(num2str(i))];
% 	disp(myconvert(temp));
% end

% ----------------------------------------------------------------

% ----------------- 2x2 ------------------------------------------

% % Generate 2-2 maps and codes	(n = 16 solutions)
% for i=0:3
% 	for j=0:3
% 		temp = '';
% 		for p=1:2
%             a = mydec2gray(num2str(i));
%             b = mydec2gray(num2str(mod((i+1),4)));
% 			if a(p) == b(p)
% 				temp = [temp a(p)];                
% 			else
% 				temp = [temp '_'];
%             end							
%         end
% 		for p=1:2
%             a = mydec2gray(num2str(j));
%             b = mydec2gray(num2str(mod((j+1),4)));
% 			if a(p) == b(p)				
%                 temp = [temp a(p)];               
% 			else
% 				temp = [temp '_'];
%             end							
%         end        
% 		disp(myconvert(temp));
%     end
% end

% Outputs:
% A'C'
% A'D
% A'C
% A'D'
% BC'
% BD
% BC
% BD'
% AC'
% AD
% AC
% AD'
% B'C'
% B'D
% B'C
% B'D'

% ----------------------------------------------------------------

% ----------------- 2x4 and 4x2-----------------------------------

% % Generate 2-4 maps and codes	(n = 8 solutions)
% for i=0:3	
% 	temp = '';
% 	for p=1:2
%         a = mydec2gray(num2str(i));
%         b = mydec2gray(num2str(mod((i+1),4)));
% 		if a(p) == b(p)
%             temp = [temp a(p)];               
%     	else
% 			temp = [temp '_'];
%         end							
%     end
%     temp2 = temp;
% 	temp = [temp '__'];
% 	disp(myconvert(temp));  % for horizontal
%     temp = ['__' temp2];
%     disp(myconvert(temp));  % for vertical
% end

% Outputs:
% A'
% C'
% B
% D
% A
% C
% B'
% D'

% ----------------------------------------------------------------

% ----------------- 4x4 ------------------------------------------

% Generate 4-4 maps and codes	(n = 1 solution);
% disp(1);

% ----------------------------------------------------------------

