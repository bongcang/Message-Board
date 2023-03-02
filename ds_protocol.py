# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664422

import json
import Profile as prof
from collections import namedtuple

class DSPProtocolError(Exception):
    pass

QUIT = "QUIT"
ERROR = "ERROR"
JOINED = "JOINED"
JOIN = "JOIN"
POST = "POST"
BIO = "BIO"
LOCATION = "LOCATION"
SONG = "SONG"
WEATHER_ERROR = "WEATHER ERROR"
LASTFM_ERROR = "LASTFM ERROR"

# Namedtuple to hold the values retrieved from json messages.
Response = namedtuple('Response', ['type', 'message', 'token'])

def profile(svr: str, usr: str, pwd: str):

    '''
    Creates a profile to store the current user's information
    :param svr:
    :param usr:
    :param pwd:
    :return:
    '''

    newProf = prof.Profile(svr, usr, pwd)
    return newProf

def join(usr: str, pwd: str):

    '''
    Formats the message for joining
    :param usr:
    :param pwd:
    :return:
    '''

    content = '{{"join": {{"username": "{username}", "password": "{password}", "token": ""}}}}'.format(username = usr, password = pwd)
    return content

def post(msg: str):

    '''
    Formats the message for a post
    :param msg:
    :return:
    '''

    post = prof.Post(msg)
    timestamp = post.timestamp
    content = '"post": {{"entry": "{post}", "timestamp": "{timestamp}"'.format(post = msg, timestamp = timestamp)
    return content

def bio(msg: str):

    '''
    Formats the message for a bio
    :param msg:
    :return:
    '''

    content = '"bio": {{"entry": "{bio}", "timestamp": ""'.format(bio = msg)
    return content

def check_join(msg: str):

    '''
    Checks the response from the server to check if joining was successful or not
    :param msg:
    :return:
    '''

    content = extract_json(msg)
    result = content[0]
    message = content[1]
    token = content[2]
    if result == 'ok':
        return JOINED, message, token
    elif result == 'error':
        return ERROR, message

def extract_json(json_msg: str) -> Response:

    '''
    Call the json.loads function on a json string and convert it to a DataTuple object
    '''

    try:
        json_obj = json.loads(json_msg)
        type = json_obj['response']['type']
        if not 'token' in json_msg:
            if type == 'error':
                message = json_obj['response']['message']
                return Response(type, message, None)
            elif type == 'ok':
                message = json_obj['response']['message']
                return Response(type, message, None)

        else:
            message = json_obj['response']['message']
            token = json_obj['response']['token']
            return Response(type, message, token)

    except json.JSONDecodeError:
        print("Json cannot be decoded.")