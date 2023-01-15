import googleapiclient.discovery
import os

class YoutubeClass:

    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.DEVELOPER_KEY = os.getenv('YOUTUBE')
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey = self.DEVELOPER_KEY)
    

    def get_uploads_id(self, channel):
        '''Get the uploads ID for a channel.  Can use either channel name or ID'''

        if str(channel).startswith('UC'):
            request = self.youtube.channels().list(
                part="contentDetails",
                id=str(channel))
        else:
            request = self.youtube.channels().list(
                part="contentDetails",
                forUsername=str(channel))
        response = request.execute()

        try:
            response = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        except Exception:
            pass

        return response


    def get_channel_ids(self, channel_list):
        '''Get channel ID if object in list is the channel name'''

        channel_ids = []
        for channel in channel_list:
            if str(channel).startswith('UC'):
                channel_ids.append(channel)
            else:
                try:
                    request = self.youtube.channels().list(
                        part="id",
                        forUsername=str(channel))
                    response = request.execute()
                    id = response['items'][0]['id']
                    channel_ids.append(id)
                except Exception:
                    pass
                
        return channel_ids

    def playlist_request(self, channel_id):
        '''Get playlist info for given channel ID'''

        request = self.youtube.playlists().list(
            part="snippet",
            channelId=channel_id,
            maxResults=25
        )
        response = request.execute()

        return response

    def get_video_ids(self, UploadID):
        '''
        - Get video ID from uploads playlist.
        - TO DO: Will need to edit this to take next_page_token into account, but fine for the time being
        '''

        next_page_token = None

        request = self.youtube.playlistItems().list(
                part="contentDetails",
                playlistId=UploadID,
                maxResults=50,
                pageToken=next_page_token
            )
        response = request.execute()

        return response