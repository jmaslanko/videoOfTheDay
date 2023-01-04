# TO DO: 
# - create youtube request class

with open('/Users/Jeremy/Documents/GitHub/YouTube_Channels/list.txt') as file:
    videoList = file.readlines()

import googleapiclient.discovery
import requests
import re
import os

# API information
api_service_name = "youtube"
api_version = "v3"


DEVELOPER_KEY = os.getenv('YOUTUBE')

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.channels().list(
        part="id",
        forUsername="StuffMadeHere"
    )
# Query execution
response = request.execute()
# Print the results
print(response)

#UURcgy6GzDeccI7dkbbBna3Q


def get_channel_info(video_list):
    new_video_list = [url for url in video_list if '/c/' in url or '/user/' in url or '/channel/' in url]
    split_string = [re.split(r"/c/|/user/|/channel/", url) for url in new_video_list]
    split_string = [i[1] for i in split_string]
    split_string = [re.split(r"/", channel)[0] for channel in split_string]
    return split_string

channels = get_channel_info(videoList)


def get_uploads_id(channel):
    '''Get the uploads ID for a channel.  Can use either channel name or ID'''

    if str(channel).startswith('UC'):
        request = youtube.channels().list(
            part="contentDetails",
            id=str(channel))
    else:
        request = youtube.channels().list(
            part="contentDetails",
            forUsername=str(channel))
    response = request.execute()

    try:
        response = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    except Exception:
        pass

    return response


uploads_ids = [get_uploads_id(channel) for channel in channels]
unique_uploads_ids = []
[unique_uploads_ids.append(i) for i in uploads_ids if type(i) == str and i not in unique_uploads_ids]


def get_channel_ids(channel_list):
    '''Get channel ID if object in list is the channel name'''

    channel_ids = []
    for channel in channel_list:
        if str(channel).startswith('UC'):
            channel_ids.append(channel)
        else:
            try:
                request = youtube.channels().list(
                    part="id",
                    forUsername=str(channel))
                response = request.execute()
                id = response['items'][0]['id']
                channel_ids.append(id)
            except Exception:
                pass
            
    return channel_ids

def playlist_request(channel_id):
    '''Get playlist info for given channel ID'''

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlists().list(
        part="snippet",
        channelId=channel_id,
        maxResults=25
    )
    response = request.execute()

    return response

def get_video_ids():
    next_page_token = None

    request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId="UURcgy6GzDeccI7dkbbBna3Q",
            maxResults=50,
            pageToken=next_page_token
        )
    response = request.execute()

    return response


request = youtube.videos().list(
        part="statistics",
        id="CEg30z7cO-s"
    )
response = request.execute()

#https://www.youtube.com/watch?v=LhfCietvDZo