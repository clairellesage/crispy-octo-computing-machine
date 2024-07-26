from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import os
import json
from pprint import pprint
import statistics
import re
from googleapiclient.discovery import build
import ast
from demjson import decode
from dotenv import load_dotenv
from copy import deepcopy

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)
channel_id = "UCGGZ_POGmIWG1pQXTDzQv-g"

def get_transcript_texts(transcripts):
  transcripts = [transcript for transcript in list(transcripts) if transcript != []]
  cleaned_transcripts = []
  for video, transcript in transcripts[0].items():
    texts = []
    for t in transcript:
      texts.append(t['text'])
    cleaned_transcripts.append({video: texts})
  return cleaned_transcripts

def split_transcripts_by_tag(texts):
  split_texts = []
  # {len(texts[0].items())} 
  pprint(f"texts[0].items() {texts[0]}.items()")
  for video, t in texts[0].items():
    flattened = " ".join(t)
    regex = r"\s\[.*?\]\s"
    segments = re.split(regex, flattened)
    segments = [s.replace("'", "") for s in segments]
    split_texts.append({video: segments})
  return split_texts
  
request = youtube.search().list(part="snippet", maxResults=2, channelId=channel_id, type="video", order="date")
response = request.execute()  

def get_data():
  # search for latest 20 videos given channel id

  # get the video_ids from the response
  video_ids = [i['id']['videoId'] for i in response['items']]
  transcripts = deepcopy(YouTubeTranscriptApi.get_transcripts(video_ids))
  print(f"loaded {len(list(transcripts))} youtube transcripts")
  texts = get_transcript_texts(transcripts)
  pprint(f"cleaned {len(texts)} transcripts: {texts}")
  split_transcripts = split_transcripts_by_tag(texts)
  pprint(f"split {len(split_transcripts)} transcripts : {split_transcripts}")
  print("sending split transcripts to openai")
  return split_transcripts

get_data()
