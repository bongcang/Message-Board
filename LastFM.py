# lastfm.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664411

'''
key - 80dba62e72a066fcd1c0ff02b6c8642e
'''

from WebAPI import WebAPI


class LastFM(WebAPI):

  def __init__(self):
    self.track_name = 'instagram'
    self.track_artist = 'dean'

  def load_data(self) -> None:

    '''
    Loads all the data from the API and puts it into their respective variables
    :return:
    '''

    url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={self.apikey}&artist={self.track_artist}&track={self.track_name}&format=json"
    response = super(LastFM, self)._download_url(url)

    track_data = response

    self.track_name = track_data['track']['name']
    self.track_artist = track_data['track']['artist']['name']

    pass

  def transclude(self, message: str) -> str:

    '''
    Replaces keywords in a message with associated API data.
    :param message: The message to transclude
    :returns: The transcluded message
    '''

    return message.replace('@lastfm', f"'{self.track_name}' by {self.track_artist}")

    pass
