import feedparser
import datetime
import delorean
import requests

rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
time_limit = delorean.parse(rss.headers['Date']) - datetime.timedelta(hours=6)
entries = [entry for entry in rss.entries if delorean.parse(entry.published) > time_limit]
print(requests.get(entries[5]['link']))