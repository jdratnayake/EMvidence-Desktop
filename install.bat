
conda create -y -n newconda &^
call activate newconda & ^
conda config --env --add channels conda-forge & ^
conda config --env --set channel_priority strict & ^
conda install -y gnuradio & ^
conda install -y conda-forge::gnuradio-osmosdr & ^
call conda deactivate