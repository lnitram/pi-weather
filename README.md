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
Configuration:

```
# copy original config-file:
cd /home/weewx
sudo cp weewx.conf weewx-own.conf

# change some settings
sudo vim weewx-own.conf

[Station]
location = city,country
latitude = xx.xxx
longitude = yy.yyy
altitude = xx, meter
station_type = TE923

[TE923]
model = TE831X

[StdReport]
  [[StandardReport]]
    skin = Own

[StdArchive]
  archive_interval = 60

# save and exit

cd skins
sudo cp -r Standard Own
cd Own
sudo vim skin.conf
[Units]
  [[Groups]]
    group_altitude = meter
    group_degree_day = degree_C_day
    group_pressure = hPa
    group_rain = mm
    group_rainrate = mm_per_hour
    group_speed = km_per_hour
    group_speed2 = km_per_hour
    group_temperature = degree_C

# save and exit

cd /home/weeewx
sudo ./bin/weewxd weewx-own.conf

# now you should see some loop-data. Should look like this:
# LOOP:   2014-03-19 22:22:42 CET (1395264162) {'outTempBatteryStatus': True, ...}

# after 1 minute there should be some files in /home/weewx/public_html

```

Install webserver (nginx)

```
sudo apt-get install nginx

# put a symbolic-link from nginx-document-root to weewx/public_html
cd /usr/share/nginx/www
sudo ln -s /home/weewx/public_html weather

# start nginx
sudo /etc/init.d/nginx start

# now the weather-data should be visible in local lan at http://ip.of.raspberry/weather
```
