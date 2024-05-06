@echo off
echo Installing EMvidence...

:: Add channels and set channel priority (suppressing output)
conda config --env --add channels conda-forge > NUL & ^
conda config --env --set channel_priority strict > NUL & ^
echo.

:: Create environment and install packages (suppressing output)
conda create -y -n EM gnuradio gnuradio-osmosdr > NUL

:: Incremental Progress Bar
setlocal enabledelayedexpansion
set "chars=▉▉▉▉▉▉▉▉▉▉"
set "delay=1"
set "progress="

echo Progress: 

for /l %%i in (1,1,10) do (
    set "progress=!progress!!chars:~%%i,1!"
    echo !progress!
    timeout /t %delay% /nobreak >nul
)

echo.
echo Done!
