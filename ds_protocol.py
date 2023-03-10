# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries
# in Python

# Replace the following placeholders with your information.

# Benjoseph Villamor
# villamob@uci.edu
# 62443909

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys

DataTuple = namedtuple('DataTuple', ['response', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to
    a DataTuple object

    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        token = json_obj['response']['token']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(response, token)


# formats the join message to follow the DSP protocol
def join(username, password):
    username = '"' + username + '"'
    password = '"' + password + '"'

    join_msg = '{"join": {"username": {filler_username},"password": {filler_password}, "token":""}}'
    join_msg = join_msg.replace('{filler_username}', username)
    join_msg = join_msg.replace('{filler_password}', password)

    return join_msg


# formats the post message to follow the DSP protocol
def post(token, message):
    post_format = '{"token":{filler_token}, "post": {"entry": {filler_post},"timestamp": "1603167689.3928561"}}'
    token = '"' + token + '"'
    message = '"' + message + '"'
    post_format = post_format.replace('{filler_token}', token)
    post_format = post_format.replace('{filler_post}', message)

    return post_format


# formats the bio message to follow the DSP protocol
def bio(token, bio):
    bio_format = '{"token":{filler_token}, "bio": {"entry": {filler_bio},"timestamp": "1603167689.3928561"}}'
    token = '"' + token + '"'
    bio = '"' + bio + '"'
    bio_format = bio_format.replace('{filler_token}', token)
    bio_format = bio_format.replace('{filler_bio}', bio)

    return bio_format
