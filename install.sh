isInstalled() {
    dpkg-query -Wf'${db:Status-abbrev}' "$1" 2> /dev/null | grep -q '^i' 
}

if ! isInstalled python3;
then
    sudo apt-get install python3
else 
	echo "Python already installed!"
fi

if ! isInstalled gnuradio;
then
    sudo apt-get install gnuradio
else 
	echo "GNU Radio already installed!"    
fi

