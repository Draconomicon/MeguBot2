rem @ECHO OFF

set pyexe=D:\Python\Project\MeguBot\Scripts\pythonw
set Helios=D:\Python\Project\MeguBot\main.py

%pyexe% -m cProfile -s tottime %Helios%