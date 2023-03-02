# webapi.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664411

from abc import ABC, abstractmethod
import urllib, json
from urllib import request, error

class WebAPI(ABC):

  def __init__(self):
    self.message = ''
    self.url = ''
    self.apikey = ''

  def _download_url(self, url: str) -> dict:

    '''
    Requests data from the web api
    :param url: Link to request data
    :return: The response from the api
    '''

    response = None
    try:
      response = urllib.request.urlopen(url)
      json_results = json.loads(response.read())
      return json_results

    except urllib.error.HTTPError as e:
      print('Failed to download contents of URL')
      print('Status code: {}'.format(e.code))

      if e.code == 404:
        print('Error: Not Found')
      if e.code == 505:
        print('Error: Request Not Handled')
      if e.code == 401:
        print('Error: Invalid Format')
      else:
        print('Error')

    finally:
      if response != None:
        response.close()

    pass
	
  def set_apikey(self, apikey: str) -> None:
    self.apikey = apikey
    pass
	
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message: str) -> str:
    pass