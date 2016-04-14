from lxml import html
import requests

#Tomorrow's forcast
page = requests.get('http://www.accuweather.com/en/us/new-york-ny/10007/daily-weather-forecast/349727?day=2')
tree = html.fromstring(page.content)
high = tree.xpath('//*[@id="detail-day-night"]/div[1]/div[1]/div[2]/span[3]/text()')[0]
low = tree.xpath('//*[@id="detail-day-night"]/div[2]/div[1]/div[2]/span[3]/text()')[0]
date = tree.xpath('//*[@id="feature-history"]/table/thead/tr/th[5]/text()')[0].strip()
print "date:", date, " high:", high, " low:", low
