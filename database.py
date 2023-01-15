import sqlite3

def init_db(db_name):
    '''Initialize db.  Will create necessary tables if don't exist'''

    # home_directory = os.path.expanduser('~')
    # db_path = os.path.join(db_path.replace('~', home_directory),db_name)

    con = sqlite3.connect(db_name)
    con.execute('CREATE TABLE IF NOT EXISTS videos(VideoID)')
    con.execute('CREATE TABLE IF NOT EXISTS uploads(UploadID)')

    return con

def insert_channel_detail(con, upload_id):
    '''Create channeldetails into db'''

    with con:
        sql = ''' INSERT INTO uploads(UploadID)
                VALUES(?) '''
        
        value = (upload_id,)
        cur = con.cursor()
        cur.execute(sql, value)
        con.commit()

    return cur.lastrowid

def insert_video_id(con, video_id):
    '''Create channeldetails into db'''

    with con:
        sql = ''' INSERT INTO videos(VideoID)
                VALUES(?) '''
        
        value = (video_id,)
        cur = con.cursor()
        cur.execute(sql, value)
        con.commit()

    return cur.lastrowid

def get_video_ids(con):
    '''Pull all video id's that have been used'''

    with con:
        sql = '''SELECT VideoID FROM videos'''

        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    
    videos = [i[0] for i in rows]
    return videos