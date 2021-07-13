4G model auto-start scripts for pi-star & mmdvm

(Only for QUECTEL EC200 series USB model）

=======================================

Usage:

rpi-rw

sudo git clone https://github.com/bmchina/pi-star-4g.git

cd pi-star-4g

sudo ./install.sh

=======================================

NOTE: Need -REBOOT- your device after installation.


about ImportError: No module named 'serial' ---

install serial module


sudo apt install python-pip //python2
sudo apt install python3-pip    //python3

sudo pip install pyserial    //python2
sudo pip3 install pyserial   //python3

