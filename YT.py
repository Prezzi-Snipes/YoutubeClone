from flask import Flask, jsonify, render_template


import pprint
import requests

Channels = {
  'apworld' : 'UCZHJHOn0PyBgkx3ztZu3vtQ',
  'playboicarti' : 'UC652oRUvX1onwrrZ8ADJRPw',
  'liluzi' : 'UCqwxMqUcL-XC3D9-fTP93Mg',
  'kanyewest' : 'UCs6eXM7s8Vl5WcECcRHc2qQ', 
}

pp = pprint.PrettyPrinter(indent=1)
app = Flask(__name__)


data = {
  'contents': [ 
    {
      'type': 'video',
      'video': {
        'isLiveNow': False,
        'publishedTimeText': '3 weeks ago', 
        'stats': {'views': 409000},
        'title': 'MOORCASH-HONEST FREESTYLE',
        'thumbnails': [
          {'url': 'link.com'}, 
          {'url': 'link.com'}, 
        ]
      }
    },
    {
      'type': 'video',
      'video': {
        'isLiveNow': False,
        'publishedTimeText':'4 months ago', 
        'stats': {'views': 46},
        'title': 'Moorcash - Talk It Out',
        'thumbnails': [
          {'url': 'link.com'}, 
          {'url': 'link.com'}, 
        ]
      }
    },
  ],
  
  'cursorNext': 'blah'
}

first_video = data['contents'][0]['video']

# print(first_video['title'])
# print(first_video['publishedTimeText'])
# print(first_video['thumbnails'])




@app.route('/')
def index():
  url = "https://youtube138.p.rapidapi.com/channel/videos/"
  querystring = {"id":Channels['playboicarti'],"hl":"en","gl":"US"}

  headers = {
  	"X-RapidAPI-Key": "6ccbd27063msh564e89de4f0fd6ep1c01fejsnd73e1f945c58",
  	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.json()
  contents = data['contents']
  videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
  print(videos) 
  video = videos[0]
  return render_template('index.html', videos=videos, video=video,)

app.run(host='0.0.0.0', port=81) 


