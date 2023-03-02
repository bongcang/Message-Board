# openweather.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664411

from WebAPI import WebAPI
from datetime import datetime

'''
key - 1bfa77f2ca7052bf2e2fb1ce35f4c644
'''

class OpenWeather(WebAPI):

  def __init__(self):
    self.zipcode = '92617'
    self.ccode = 'us'


  def load_data(self) -> None:

    '''
    Loads all the data from the API and puts it into their respective variables
    :return:
    '''

    url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}&units=imperial"
    response = super(OpenWeather, self)._download_url(url)

    weather_data = response

    self.temperature = str(weather_data['main']['temp'])[:4]
    self.high_temperature = str(weather_data['main']['temp_max'])[:4]
    self.low_temperature = str(weather_data['main']['temp_min'])[:4]
    self.longitude = str(weather_data['coord']['lon'])
    self.latitude = str(weather_data['coord']['lat'])
    self.description = weather_data['weather'][0]['description']
    self.humidity = weather_data['main']['humidity']
    self.city = weather_data['name']
    self.sunset = str(datetime.fromtimestamp(int(weather_data['sys']['sunset'])).time())

    pass

  def transclude(self, message: str) -> str:

    '''
    Replaces keywords in a message with associated API data.
    :param message: The message to transclude
    :returns: The transcluded message
    '''

    return message.replace('@weather', f"{self.temperature} degrees in {self.city}")

    pass