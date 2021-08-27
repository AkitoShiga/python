#!/Users/insightshiga/.pyenv/shims/python

from apiclient.discovery import build


YOUTUBE_API_KEY = ''
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_response = youtube.search().list(
                                           part='snippet',
                                           q='手芸',
                                           type='video'
                                       ).execute()

# レスポンスのJSONをパースしたDictで帰ってくるらしい
print(search_response)
