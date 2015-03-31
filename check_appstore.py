
import botkit
import requests
import redis
import re

REDIS_KEY = 'ingress-appstore-lastupdate'
URL = 'https://itunes.apple.com/us/app/ingress/id576505181'

resp = requests.get(URL)
m = re.search('<span class="label">Updated: </span><span.*?>(.*?)</span></li><li><span class="label">Version: </span><span.*?>(.*?)</span></li>', resp.text)
date = m.group(1)

rc = redis.StrictRedis()
last = rc.get(REDIS_KEY)
rc.set(REDIS_KEY, date)

if date != last:
    bot = botkit.Bot(username='App Store')
    bot.send('[iOS Update] date:', date, 'version:', m.group(2))
