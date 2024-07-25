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

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
# youtube = build("youtube", "v3", developerKey=api_key)
channel_id = "UCGGZ_POGmIWG1pQXTDzQv-g"
# creator_id = "@MichelleKhare"

# search for latest 20 videos given channel id
# request = youtube.search().list(part="snippet", maxResults=2, channelId=channel_id, type="video", order="date")
# response = request.execute()

# get the video_ids from the response
# video_ids = [i['id']['videoId'] for i in response['items']]
# pprint(video_ids)

# transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)
# pprint(transcripts[0])

def get_transcript_texts(transcripts):
  transcripts = [transcript for transcript in list(transcripts) if transcript != []]
  cleaned_transcripts = []
  for transcript in transcripts:
    texts = []
    for i in transcript.keys():
      for t in transcript[i]:
        texts.append(t['text'].replace('/"/g', "'"))
      cleaned_transcripts.append({i: texts})
  pprint(cleaned_transcripts)
  return cleaned_transcripts

def split_transcript_by_music(texts):
  split_texts = []
  pprint(texts)
  for t in texts:
    flattened = " ".join(t)
    segments = flattened.split("[Music]")
    print(segments)
    split_texts.append(segments)
  return segments

def match_texts_by_segment(texts, segments):
  new_list = [[]]
  for s in segments:
    for t in texts:
        if re.match(s, t):
            new_list.append([])
        new_list[-1].append(t)
  print(new_list[0])
  return new_list

def main():
  # transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)
  # texts = get_transcript_texts(transcripts)
  texts = data
  split = split_transcript_by_music(texts)
  new_transcripts = match_texts_by_segment(texts, split)
  # return
  return new_transcripts

main()

# texts = [line['text'] for line in transcript]
# starts = [int(line['start']) for line in transcript]
# durations = [int(line['duration']) for line in transcript]

# flattened = ", ".join(texts)
# split = flattened.split("[Music]")
# print(split[0])
# print(split[1])
# print(split[2])
# print(len(split))

# print(statistics.median(int(line['duration'])))
# print(statistics.median(starts))
# print(sum(durations))
# print(statistics.mean(durations))


# check for created transcript fist
# transcript = transcript_list.find_manually_created_transcript(['en'])

# or automatically generated ones
# transcript = transcript_list.find_generated_transcript(['en'])
# transcript.fetch()

# returns
#[
#    {
#        'text': 'Hey there',
#        'start': 7.58,
#        'duration': 6.13
#    },
#    {
#        'text': 'how are you',
#        'start': 14.08,
#        'duration': 7.58
#    },
#    # ...
#]
