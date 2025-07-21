@echo off
set "ORDNER=./out"
echo Delete all files in %ORDNER%
del /Q "%ORDNER%\*.*"
echo Done. Starting Script Python

setlocal
cd /d "%~dp0"
python prompt_splitter.py
pause
endlocal