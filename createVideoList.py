# This file became the working file to take list of channels
# and get their uploads playlist ID.  Those id's are then
# uploaded to the db

import re
import youtube as yt
import database as db

with open('/Users/Jeremy/Documents/GitHub/YouTube_Channels/list.txt') as file:
    videoList = file.readlines()

def get_channel_info(video_list):
    new_video_list = [url for url in video_list if '/c/' in url or '/user/' in url or '/channel/' in url]
    split_string = [re.split(r"/c/|/user/|/channel/", url) for url in new_video_list]
    split_string = [i[1] for i in split_string]
    split_string = [re.split(r"/", channel)[0] for channel in split_string]
    return split_string

channels = get_channel_info(videoList)

youtube = yt.YoutubeClass()
uploads_ids = [youtube.get_uploads_id(channel) for channel in channels]
unique_uploads_ids = []
[unique_uploads_ids.append(i) for i in uploads_ids if type(i) == str and i not in unique_uploads_ids]

#Insert uploads playlist id's to db
con = db.init_db('StemVideo.db')
ids = [db.insert_channel_detail(con, id) for id in unique_uploads_ids]
