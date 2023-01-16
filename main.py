import youtube as yt
import database as db
import random


def random_playlist(con):
    '''Randomly select a channel uploads playlist'''
    
    uploads_ids = db.get_uploads_ids(con)
    selection = random.choice(uploads_ids)
    return selection

def random_video(con, video_id):
    '''
    - Selects a video id from the uploads playlist.
    - Checks to see if that video id has been played before and skips it if it has
    '''

    youtube = yt.YoutubeClass()

    past_videos = db.get_video_ids(con)
    video_response = youtube.get_video_ids(video_id)
    
    n = 0
    while True:
        id = video_response['items'][n]['contentDetails']['videoId']
        if id in past_videos:
            n += 1
        else:
            break
    
    return id


    
# Need to now create html production file that will get updated with 
# the new video id.  Will use beautifulsoup to do so    




def main():
    con = db.init_db('StemVideo.db')
    playlist = random_playlist(con)
    video = random_video(con, playlist)
    db_id = db.insert_video_id(con, video)

if __name__ == '__main__':
    main()