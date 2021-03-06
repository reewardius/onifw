# For v3 core
clear
echo "
 _                      _ _             
(_)           _        | | |            
 _ ____   ___| |_  ____| | | ____  ____ 
| |  _ \ /___)  _)/ _  | | |/ _  )/ ___)
| | | | |___ | |_( ( | | | ( (/ /| |    
|_|_| |_(___/ \___)_||_|_|_|\____)_|                                                                                         
";

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/onifw"
    BIN_DIR="$PREFIX/bin"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python3 python2 perl gcc ruby

else
    INSTALL_DIR="$HOME/.onifw"
    BIN_DIR="/usr/local/bin"
    BASH_PATH="/bin/bash"
    TERMUX=false

fi

echo "[*] - Looking for old install...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] - onifw is already installed. Do you want to overwrite anyways? [y/N]";
    read ans
    if [ "$ans" = "y" ] || [ "$ans" = "Y"]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/onifw"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/onifw"
        fi
    else
        echo "[!] - Unable to delete onifw folder"
        echo "[!] - In order to install this version you must manually remove the installed one";
        echo "[!] - Installation aborted.";
        exit
    fi
fi

echo "[*] - Cleaning...";
if [ -d "$ETC_DIR/w0bos" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/w0bos"
    else
        sudo rm -rf "$ETC_DIR/w0bos"
    fi
fi

echo "[*] - Installing...";
echo "";
# Install when merge done
git clone https://github.com/w0bos/onifw "$INSTALL_DIR"
#echo "#!$BASH_PATH python3 $INSTALL_DIR/oni.py" '${1+"$@"}' > "$INSTALL_DIR/onifw"
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/src/bin/onifw" "$BIN_DIR"
    #cp -r "$INSTALL_DIR/src/data" "$BIN_DIR"
    #cp -r "$INSTALL_DIR/src/core" "$BIN_DIR"
    #cp launcher "$BIN_DIR" onifw
else
    sudo cp "$INSTALL_DIR/src/bin/onifw" "$BIN_DIR"
    #sudo cp -r "$INSTALL_DIR/src/core" "$BIN_DIR"
    #sudo cp -r "$INSTALL_DIR/src/data" "$BIN_DIR"
    #sudo cp launcher "$BIN_DIR" onifw
fi
#For merged
curl https://raw.githubusercontent.com/w0bos/onifw/master/src/uninstall > uninstall
sudo chmod +x uninstall
mv uninstall "$INSTALL_DIR"
sudo pip3 install packaging

if [ $# -eq 1 ]
    then
        if [ $1=="--install-all" ]; then
            echo "[*] - Install all flag"
        else
            echo "[!] - unkown flag $1"
        fi
fi



if [ -d "$INSTALL_DIR" ] ;
then
    echo "[*] - onifw successfully installed"
else
    echo "[!] - Installation failed";
    exit
fi
