function [c,tf]= gcnv(go,f,t,fs)
% go funcao de entrada
%  f resposta impulsiva do sistema
%  t vetor tempo
% fs amostragem de tempo
%
%  codigo exemplo:
%  t=0:0.1:2;
%  h=exp(-t);
%  x=[0 ones(1,10) zeros(1,10)];
% [y,F] = gcnv(x,h,t,0.1);



close all
% color of axis constant
  axis_color= [0.5 0.5 0.5];

% sampling interval constant
  s_int = fs;

% interval for function 'f(t)'
  %t = [ tini(1):s_int:4 ];

% definition of function 'f(t)'
%   f = 0.1*(t.^2);
 % f = exp(-1*t);
  %  f = t;

% interval for function 'go(t1)'
 % t1 = [tini(2):s_int:1];
t1=t;
% definition of function 'go(t1)'
%go = 1*ones(1, length(t1)); 

% go = .1*(t1.^3);
% go = 5*cos(2*pi*t1);
% go = 5*ones(1, length(t1));
% go = zeros(1, length(t1));go(1)=5;


% convolve: note the multiplation by the sampling interval
  c = s_int * conv(f, go);

% Animation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% flip 'go(t1)' for the graphical convolutions g = go(-t1)
  g = fliplr(go);
  tf = fliplr(-t1);

% slide range of 'g' to discard non-ovelapping areas with 'f' in the convolution
  tf = tf + ( min(t)-max(tf) );

% get the range of function 'c' which is the convolution of 'f(t)' and 'go(t1)'
  tc = [ tf t(2:end)];
  tc = tc+max(t1);

% start graphical output with three subplots
  a_fig = figure;
  set(a_fig, 'Name', 'Animated Convolution', 'unit', 'pixel', ...
             'Position', [300, 150, 600, 750]);

% plot f(t) and go(t1)  
  ax_1 = subplot(3,1,1);
  stem(t,f, 'b')
  hold on; grid on;
  stem(t1, go, 'r');
  hold on; grid on;
  set(ax_1, 'XColor', axis_color, 'YColor', axis_color, 'Color', 'w', 'Fontsize', 9);
  xlim( [ ( min(t)-abs(max(tf)-min(tf)) - 1 ) ( max(t)+abs(max(tf)-min(tf)) + 1 ) ] );
  title('Graph of f(t) and go(t)', 'Color', axis_color );
  legend({'f(t)' 'go(t)'});

% initialize animation the plot of 'g' is slided over the plot of 'f'

% plot f in the subplot number 2
  ax_2 = subplot(3,1,2);
  p = stem(t, f);
  hold on; grid on;
  title('Graphical Convolution: f(t) and g = go(-t1)', 'Color', axis_color );
  
% plot g in the subplot number 2
  q = stem(tf, g, 'r');
  xlim( [ ( min(t)-abs(max(tf)-min(tf))-1 ) ( max(t)+abs(max(tf)-min(tf))+1 ) ] );
  u_ym = get(ax_2, 'ylim');

% plot two vertical lines to show the range of ovelapped area
  s_l = line( [min(t) min(t)], [u_ym(1) u_ym(2)], 'color', 'g'  );
  e_l = line( [min(t) min(t)], [u_ym(1) u_ym(2)], 'color', 'g'  );
  hold on; grid on;
  set(ax_2, 'XColor', axis_color, 'YColor', axis_color, 'Color', 'w', 'Fontsize', 9);

  % put a yellow shade on ovelapped region
  sg = rectangle('Position', [min(t) u_ym(1) 0.0001 u_ym(2)-u_ym(1)], ...
                 'EdgeColor', 'w', 'FaceColor', 'y', ...
                 'EraseMode', 'xor');
  
  
% initialize the plot the convolution result 'c'
  ax_3 = subplot(3,1,3);
  r = stem(tc, c);
  grid on; hold on;
  set(ax_3, 'XColor', axis_color, 'YColor', axis_color, 'Fontsize', 9);
  % xlim( [ min(tc)-1 max(tc)+1 ] );
  xlim( [ ( min(t)-abs(max(tf)-min(tf)) - 1 ) ( max(t)+abs(max(tf)-min(tf)) + 1 ) ] );
  title('Convolutional Product c(t)', 'Color', axis_color );

% animation block
  for i=1:length(tc)
    
    % control speed of animation minimum is 0, the lower the faster
      pause;
      drawnow;
      
    % update the position of sliding function 'g', its handle is 'q'
      tf=tf+s_int;
      set(q,'EraseMode','xor');
      set(q,'XData',tf,'YData',g);

    % show overlapping regions
    
    % show a vetical line for a left boundary of overlapping region
      sx = min( max( tf(1), min(t) ), max(t) );  
      sx_a = [sx sx];
      set(s_l,'EraseMode','xor');
      set(s_l, 'XData', sx_a);

    % show a second vetical line for the right boundary of overlapping region
      ex = min( tf(end), max(t) );  
      ex_a = [ex ex];
      set(e_l,'EraseMode','xor');
      set(e_l, 'XData', ex_a);
      
    % update shading on ovelapped region
      rpos = [sx u_ym(1) max(0.0001, ex-sx) u_ym(2)-u_ym(1)];  
      set(sg, 'Position', rpos);
      
    % update the plot of convolutional product 'c', its handle is r
      set(r,'EraseMode','xor');
      set(r,'XData',tc(1:i),'YData',c(1:i) );
    
  end;
%
% end of acnv %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
