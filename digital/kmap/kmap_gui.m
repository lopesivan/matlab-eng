function varargout = kmap_gui(varargin)
% KMAP_GUI M-file for kmap_gui.fig
%      KMAP_GUI, by itself, creates a new KMAP_GUI or raises the existing
%      singleton*.
%
%      H = KMAP_GUI returns the handle to a new KMAP_GUI or the handle to
%      the existing singleton*.
%
%      KMAP_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in KMAP_GUI.M with the given input arguments.
%
%      KMAP_GUI('Property','Value',...) creates a new KMAP_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before kmap_gui_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to kmap_gui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help kmap_gui

% Last Modified by GUIDE v2.5 01-Feb-2005 09:50:15

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @kmap_gui_OpeningFcn, ...
                   'gui_OutputFcn',  @kmap_gui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before kmap_gui is made visible.
function kmap_gui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to kmap_gui (see VARARGIN)

% Choose default command line output for kmap_gui
handles.output = hObject;

for i=1:16
    set(eval(['handles.pushbutton' num2str(i)]),'ForegroundColor',[1 1 1]);
end

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes kmap_gui wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = kmap_gui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end
% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton8.
function pushbutton8_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton11.
function pushbutton11_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton12.
function pushbutton12_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton13.
function pushbutton13_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton14.
function pushbutton14_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton15.
function pushbutton15_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end

% --- Executes on button press in pushbutton16.
function pushbutton16_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject,'String') == '0'
    set(hObject,'String','1');
    set(hObject,'ForegroundColor',[0 0 0]); % Black
else
    set(hObject,'String','0');
    set(hObject,'ForegroundColor',[1 1 1]); % White
end



% --- Executes on button press in solveit_pushbutton.
function solveit_pushbutton_Callback(hObject, eventdata, handles)
% hObject    handle to solveit_pushbutton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

kmap = zeros(4,4);
for i=1:4
    for j=1:4
        pb = (i-1)*4+(j-1)+1;
        if get(eval(['handles.pushbutton' num2str(pb)]),'String') == '1'
            kmap(i,j) = 1;
        else
            kmap(i,j) = 0;
        end
    end    
end

result = solveKmap(kmap);

set(handles.result_edit,'String',result);
guidata(hObject, handles);

function result_edit_Callback(hObject, eventdata, handles)
% hObject    handle to result_edit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of result_edit as text
%        str2double(get(hObject,'String')) returns contents of result_edit as a double


% --- Executes during object creation, after setting all properties.
function result_edit_CreateFcn(hObject, eventdata, handles)
% hObject    handle to result_edit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


