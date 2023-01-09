import sqlite3
import os

def init_db(db_path, db_name):

    home_directory = os.path.expanduser('~')
    db_path = os.path.join(db_path.replace('~', home_directory),db_name)

    con = sqlite3.connect(db_name)
    con.execute('CREATE TABLE IF NOT EXISTS videos(Channel, PlaylistID, VideoID, DatePlayed)')

    return con

def video_check(video_id, con):
    
    with con:
        cur = con.cursor()
        cur.execute('SELECT VideoID FROM videos')

        video_ids = cur.fetchall()

        
