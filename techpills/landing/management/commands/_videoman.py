from . import _ytprivate as ytprivate
import requests
import json

# https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUVqlDOUyIjMWqBUhp73a90g&key=AIzaSyCU2BH6xton2Iyh4jzirtg0o0do7Q1e0D8

BASE_URL = 'https://www.googleapis.com/youtube/v3/'
KEY_PREFIX = '&key='
CHANNEL_ID = 'UCVqlDOUyIjMWqBUhp73a90g'
UPLOADS_ID = 'UUVqlDOUyIjMWqBUhp73a90g'
VIDEO_BASE_URL = 'https://www.youtube.com/watch?v='

def make_req(reqstr):
    url = BASE_URL + \
        reqstr + \
        KEY_PREFIX + \
        ytprivate.API_KEY
    return json.loads(requests.get(url).text)['items']


def get_latest_uploads(results=50):
    reqstr = 'playlistItems?part=snippet&maxResults=' + \
        str(results) + \
        '&playlistId=' + \
        UPLOADS_ID
    return make_req(reqstr)


class Video:
    def __init__(self, vid_id, title, description, thumb, date_time, url):
        self.vid_id = vid_id
        self.title = title
        self.description = description
        self.thumb = thumb
        self.date_time = date_time
        self.url = url

    def __repr__(self):
        return self.title

def make_vieo_objects(pl_dict):
    videos = []
    for vid_dict in pl_dict:
        details = vid_dict['snippet']
        vid_id = vid_dict['id']
        title = details['title']
        description = details['description']
        thumb = details['thumbnails']['maxres']['url']
        date_time = details['publishedAt'][:-8].replace('T', ' ')
        url = VIDEO_BASE_URL + \
            details['resourceId']['videoId']
        videos.append(Video(
            vid_id,
            title,
            description,
            thumb,
            date_time,
            url
        ))
    return videos
