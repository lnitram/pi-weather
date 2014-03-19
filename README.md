# pi-weather

Some scripts and howtos, to use the raspberry pi for weather stuff

## basic installation

* prepare sd-card with raspbian
* basic - settings (expand filesystem, locale, hostname, timezone, keyboard-settings, password,...)
* update

```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
sudo reboot
```

## use weewx to read data from weather-station and generate html-reports

Hardware used for this project:
- Weather station TE831X
- Other stations supported by weewx: http://www.weewx.com/hardware.html

Software
- weewx (http://www.weewx.com)

Installation of weewx:
Installation-guide: http://www.weewx.com/docs/usersguide.htm#installing

Example using python-tool setup.py:
```
# install dependencies
sudo apt-get install python-configobj
sudo apt-get install python-cheetah
sudo apt-get install python-imaging
sudo apt-get install python-serial
sudo apt-get install python-usb
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install pyephem

# install weewx
# download weewx (check http://sourceforge.net/projects/weewx/files/ for latest version)
# replace x.x.x with latest version
wget -O weewx.tar.gz http://sourceforge.net/projects/weewx/files/weewx-x.x.x.tar.gz/download
tar xvfz weewx.tar.gz
cd weewx-x.x.x
./setup.py build
sudo ./setup.py install
```



  
