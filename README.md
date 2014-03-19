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
# LOOP:   2014-03-19 22:22:42 CET (1395264162) {'outTempBatteryStatus': True, 'outHumidity': 69, 'rainBatteryStatus': True, 'extraBatteryStatus1': True, 'rainRate': 0.0, 'heatindex': 49.46, 'extraTemp2': None, 'inTemp': 67.46000000000001, 'windGustDir': None, 'barometer': 30.01698168930892, 'windchill': 48.56, 'dewpoint': 39.71921905385686, 'rain': 0.0, 'pressure': 29.90625864989311, 'extraHumid4': None, 'extraHumid2': None, 'extraHumid3': None, 'extraHumid1': None, 'rainTotal': 0.06578, 'extraTemp4': None, 'altimeter': 30.003953781021792, 'extraTemp3': None, 'usUnits': 1, 'extraTemp1': None, 'txBatteryStatus': True, 'extraBatteryStatus2': True, 'extraBatteryStatus3': True, 'windBatteryStatus': True, 'UV': None, 'extraBatteryStatus4': True, 'dateTime': 1395264162, 'windDir': None, 'outTemp': 49.46, 'windSpeed': 0.0, 'inHumidity': 52, 'windGust': 0.0}

```

  
