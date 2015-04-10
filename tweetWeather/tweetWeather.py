#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import datetime
import time
import os
import sys
from twython import Twython

os.system("montage -geometry 300x180+0+0 /usr/share/nginx/www/data/daytemp.png /usr/share/nginx/www/data/daybarometer.png /usr/share/nginx/www/data/daywind.png /usr/share/nginx/www/data/dayrain.png /usr/share/nginx/www/wetter/summary.png")

tw = Twython(
    app_key = 'xxxxx',
    app_secret = 'xxxxx',
    oauth_token = 'xxxxx',
    oauth_token_secret = 'xxxxx'
)

json_data = open('/home/weewx/public_html/data.json')
data = json.load(json_data)
json_data.close()

barometer   = str(data["stats"]["current"]["barometer"])
temp        = str(data["stats"]["current"]["outTemp"])
humidity    = str(data["stats"]["current"]["humidity"])

now = time.localtime()[3]

statusMessage1 = "Das #Wetter in #Wedel: Temp: " + temp + "°C - Luftdr.: " + barometer + " - Luftfeucht.: " + humidity + " - #weewx #RaspberryPi"

photo = open('/usr/share/nginx/www/wetter/summary.png','rb')

media_status = tw.upload_media(media=photo)
tw.update_status(media_ids=[media_status['media_id']], status=statusMessage1)
