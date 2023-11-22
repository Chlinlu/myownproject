import requests
import json,csv

#获取实时天气
def weather_now(site):
    with open(r'C:\\Users\\X79\Desktop\Django_Wordk\\hefengweather\\China-City-List-latest.csv','rt', encoding='utf-8') as mycsvfile:
        myreader=csv.reader(mycsvfile)
        for row in myreader:
            if site in row[2]:
                location_id = row[0]
    print(location_id)
    response=requests.get('https://devapi.qweather.com/v7/weather/now?location=101010100&key=9bf137c085fe4c5cb268a4654a66162d'.format(location_id))
    results = response.json()
    weather_text={}
    weather_text['城市']=site
    weather_text['气温']=results.get('now').get('temp')+'°C'
    weather_text['天气']=results.get('now').get('text')
    
    return weather_text

print(weather_now('乐山'))
