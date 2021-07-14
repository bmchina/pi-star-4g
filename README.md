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

=======================================




Additional:

If you run under pi-star 3.4.17, maybe error message as below:

===============================================

ImportError: No module named 'serial'.

you should install serial module

sudo apt install python-pip //python2

sudo apt install python3-pip    //python3

sudo pip install pyserial    //python2

sudo pip3 install pyserial   //python3

short of  usb driver

==============

sudo apt install raspberrypi-kernel-headers

unzip Quectel_Linux_USB_Serial_Option_Driver_V1.0.zip

cd Quectel_Linux_USB_Serial_Option_Driver_V1.0

cd v4.19.51

sudo make install
