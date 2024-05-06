@echo off
echo Installing EMvidence...
echo Please wait this may take a few moments.
conda config --env --add channels conda-forge & ^
conda config --env --set channel_priority strict & ^
conda create -y -n EMvidence gnuradio gnuradio-osmosdr & ^
echo Installation Complete!

