import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?textField1=40.71&textField2=-74.01")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id='seven-day-forecast')

forecast_items = seven_day.find_all(class_='tombstone-container')

for x in forecast_items:

	period = x.find(class_='period-name').get_text()
	short_desc = x.find(class_='short-desc').get_text()
	temp = x.find(class_='temp').get_text()

	print(period)
	print(short_desc)
	print(temp)
	print('')