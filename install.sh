#!/bin/bash
sudo cp 98-usb4g.rules /etc/udev/rules.d
sudo cp usbin.sh /usr/local/bin
sudo cp start4g.py /usr/local/bin
echo -e "Installation completed, please REBOOT your device to take effaction."
