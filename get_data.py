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

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
# youtube = build("youtube", "v3", developerKey=api_key)
channel_id = "UCGGZ_POGmIWG1pQXTDzQv-g"

data = ({'2fH2n1XbtU4': [{'duration': 5.7,
                   'start': 0.11,
                   'text': 'how I accidentally joined the MCU after'},
                  {'duration': 4.859,
                   'start': 3.53,
                   'text': "many years of trying to get Marvel's"},
                  {'duration': 5.039,
                   'start': 5.81,
                   'text': 'attention I finally got an invitation to'},
                  {'duration': 4.741,
                   'start': 8.389,
                   'text': 'attend the premiere of Miss Marvel Now'},
                  {'duration': 4.381,
                   'start': 10.849,
                   'text': 'typically out of big Hollywood Premiere'},
                  {'duration': 4.38,
                   'start': 13.13,
                   'text': 'the main cast in a-listers Walk the'},
                  {'duration': 4.379,
                   'start': 15.23,
                   'text': 'fancy red carpet with all the paparazzi'},
                  {'duration': 4.439,
                   'start': 17.51,
                   'text': 'while everyone else takes selfies at a'},
                  {'duration': 5.58,
                   'start': 19.609,
                   'text': 'fake red carpet off to the side but this'},
                  {'duration': 4.74,
                   'start': 21.949,
                   'text': 'time I was pulled onto the actual carpet'},
                  {'duration': 3.6,
                   'start': 25.189,
                   'text': 'cameras were flashing in my face'},
                  {'duration': 4.08,
                   'start': 26.689,
                   'text': 'Paparazzi were screaming my name and'},
                  {'duration': 4.741,
                   'start': 28.789,
                   'text': 'eager reporters kept asking me about'},
                  {'duration': 5.341,
                   'start': 30.769,
                   'text': "being in the show but I'm not in the"},
                  {'duration': 4.68,
                   'start': 33.53,
                   'text': "show and I have no idea why I'm here I"},
                  {'duration': 4.379,
                   'start': 36.11,
                   'text': 'tried to explain the truth but the next'},
                  {'duration': 4.56,
                   'start': 38.21,
                   'text': 'day I was listed in multiple articles as'},
                  {'duration': 5.581,
                   'start': 40.489,
                   'text': "a part of the cast I'm literally in"},
                  {'duration': 5.16,
                   'start': 42.77,
                   'text': "Marvel's thumbnail why am I there it's"},
                  {'duration': 3.84,
                   'start': 46.07,
                   'text': "been months and nobody's fixed it so I'm"},
                  {'duration': 4.32,
                   'start': 47.93,
                   'text': "taking it as a sign Marvel I'm available"},
                  {'duration': 4.46,
                   'start': 49.91,
                   'text': 'if you want to make this a reality and'},
                  {'duration': 2.12, 'start': 52.25, 'text': "that's"}],
  'arBIkByNJq4': [{'duration': 7.62,
                   'start': 0.0,
                   'text': 'this is a 270 pound professional arm'},
                  {'duration': 7.32,
                   'start': 3.6,
                   'text': 'wrestler named Brandon and this is me I'},
                  {'duration': 6.599,
                   'start': 7.62,
                   'text': "am 115 pounds 5'2 and about to challenge"},
                  {'duration': 5.76,
                   'start': 10.92,
                   'text': 'him to a duel little does he know I have'},
                  {'duration': 4.461, 'start': 14.219, 'text': 'a plan three'},
                  {'duration': 2.0, 'start': 16.68, 'text': 'two'},
                  {'duration': 5.04,
                   'start': 23.22,
                   'text': 'my plan was to LEAP up onto the table'},
                  {'duration': 3.42,
                   'start': 26.519,
                   'text': "because you can't win an arm wrestle"},
                  {'duration': 3.24,
                   'start': 28.26,
                   'text': 'battle unless the hand hits the table'},
                  {'duration': 4.561,
                   'start': 29.939,
                   'text': 'right so I was like I just have to block'},
                  {'duration': 5.899,
                   'start': 31.5,
                   'text': 'the goal area in its entirety well'},
                  {'duration': 2.899,
                   'start': 34.5,
                   'text': 'this is what happened'},
                  {'duration': 7.67, 'start': 38.22, 'text': '[Laughter]'},
                  {'duration': 10.44, 'start': 40.49, 'text': '[Music]'},
                  {'duration': 15.929, 'start': 45.89, 'text': '[Laughter]'},
                  {'duration': 10.889, 'start': 50.93, 'text': '[Music]'}],
  'eWxogC2yjjE': [{'duration': 4.38,
                   'start': 0.0,
                   'text': 'this is my grandma and I forgot her'},
                  {'duration': 3.3,
                   'start': 2.82,
                   'text': "birthday so it's my mission to wish her"},
                  {'duration': 6.0,
                   'start': 4.38,
                   'text': 'a happy birthday on the biggest'},
                  {'duration': 7.62,
                   'start': 6.12,
                   'text': 'Jumbotron in the NFL I tried dancing hey'},
                  {'duration': 5.58, 'start': 10.38, 'text': 'hey screaming'},
                  {'duration': 3.84,
                   'start': 13.74,
                   'text': 'and dancing again literally everyone'},
                  {'duration': 3.48,
                   'start': 15.96,
                   'text': "that's on it they don't even notice"},
                  {'duration': 3.9,
                   'start': 17.58,
                   'text': "they're on it but in a stadium of 70 000"},
                  {'duration': 4.82,
                   'start': 19.44,
                   'text': 'people I realized I needed to go big or'},
                  {'duration': 2.78, 'start': 21.48, 'text': 'go home can'},
                  {'duration': 6.02, 'start': 24.42, 'text': 'of my grandma'},
                  {'duration': 3.35, 'start': 27.09, 'text': '[Music]'},
                  {'duration': 4.501,
                   'start': 30.599,
                   'text': "and though my weird fake proposal didn't"},
                  {'duration': 4.021,
                   'start': 32.759,
                   'text': 'work word of my mission got around and'},
                  {'duration': 4.2,
                   'start': 35.1,
                   'text': 'someone offered to let me on the field'},
                  {'duration': 4.2,
                   'start': 36.78,
                   'text': 'giving me my best chance yet we just'},
                  {'duration': 4.14,
                   'start': 39.3,
                   'text': "really want to get on the Jumbotron it's"},
                  {'duration': 4.52,
                   'start': 40.98,
                   'text': "my grandmother's birthday he said no but"},
                  {'duration': 4.439,
                   'start': 43.44,
                   'text': 'then I saw my chance'},
                  {'duration': 4.739,
                   'start': 45.5,
                   'text': 'the camera operator and I locked eyes'},
                  {'duration': 2.36, 'start': 47.879, 'text': 'and'},
                  {'duration': 3.66,
                   'start': 50.64,
                   'text': 'happy birthday grandma turns out it'},
                  {'duration': 2.82,
                   'start': 52.739,
                   'text': "didn't make the broadcast but you can"},
                  {'duration': 2.82,
                   'start': 54.3,
                   'text': 'watch your favorite teams out of Market'},
                  {'duration': 3.421,
                   'start': 55.559,
                   'text': 'Sunday afternoon games now on YouTube'},
                  {'duration': 4.34,
                   'start': 57.12,
                   'text': 'and YouTube TV no tutor contracts'},
                  {'duration': 2.48, 'start': 58.98, 'text': 'required'}],
  'sZ9K4LGLLJ4': [{'duration': 3.86,
                   'start': 0.0,
                   'text': 'I will wear a blindfold'},
                  {'duration': 3.721,
                   'start': 3.959,
                   'text': 'for the whole game'},
                  {'duration': 4.29, 'start': 5.55, 'text': '[Music]'},
                  {'duration': 5.1, 'start': 7.68, 'text': 'pun'},
                  {'duration': 4.14,
                   'start': 9.84,
                   'text': "pun three I'll go Pawn to E5 how about"},
                  {'duration': 6.78, 'start': 12.78, 'text': 'uh'},
                  {'duration': 7.2,
                   'start': 13.98,
                   'text': 'Knight goes from B1 to C3 to C5'},
                  {'duration': 5.16,
                   'start': 19.56,
                   'text': "I think they're playing full you know"},
                  {'duration': 9.06,
                   'start': 21.18,
                   'text': "what okay how about this Pawn A4 uh I'll"},
                  {'duration': 7.559,
                   'start': 24.72,
                   'text': 'go Pawn to D5 Knight goes from G1 to F3'},
                  {'duration': 6.68,
                   'start': 30.24,
                   'text': "you're attacking my Pawn I'll push that"},
                  {'duration': 9.421,
                   'start': 32.279,
                   'text': 'pawn from E5 to E4 Knight E5 Queen to F6'},
                  {'duration': 6.04,
                   'start': 36.92,
                   'text': 'Pawn F4 Queen takes pawn bishop B2 okay'},
                  {'duration': 3.42,
                   'start': 41.7,
                   'text': 'so I could take your knight with my'},
                  {'duration': 6.54,
                   'start': 42.96,
                   'text': 'queen but I think a better move is Queen'},
                  {'duration': 9.32,
                   'start': 45.12,
                   'text': 'F2 Checkmate respectfully what the'},
                  {'duration': 4.94,
                   'start': 49.5,
                   'text': "it's not necessarily a fair fight so"}],
  'zHaYh_KB5AQ': [{'duration': 4.259,
                   'start': 0.0,
                   'text': 'this is the Secret Service physical'},
                  {'duration': 4.439,
                   'start': 1.92,
                   'text': "fitness test and today I'm competing"},
                  {'duration': 4.321,
                   'start': 4.259,
                   'text': 'against an actual secret service uniform'},
                  {'duration': 4.501,
                   'start': 6.359,
                   'text': 'division officer to see if I can beat'},
                  {'duration': 6.24,
                   'start': 8.58,
                   'text': 'them at their own game first event Max'},
                  {'duration': 6.8,
                   'start': 10.86,
                   'text': 'push-ups in one minute 36. okay how many'},
                  {'duration': 5.52,
                   'start': 14.82,
                   'text': 'did you get 50 50.'},
                  {'duration': 5.68,
                   'start': 17.66,
                   'text': 'the next two events were Max sit-ups in'},
                  {'duration': 4.76,
                   'start': 20.34,
                   'text': 'a minute and Max chin-ups four'},
                  {'duration': 5.64, 'start': 23.34, 'text': 'five'},
                  {'duration': 6.479,
                   'start': 25.1,
                   'text': 'and I lost both I definitely want Alex'},
                  {'duration': 4.739, 'start': 28.98, 'text': 'protecting me'},
                  {'duration': 4.0,
                   'start': 31.579,
                   'text': 'okay so even though I lost the first'},
                  {'duration': 4.5,
                   'start': 33.719,
                   'text': 'three events I had hope for the final'},
                  {'duration': 5.221,
                   'start': 35.579,
                   'text': 'test the mile and a half run the secret'},
                  {'duration': 4.68,
                   'start': 38.219,
                   'text': 'service has their secrets but so do I'},
                  {'duration': 3.84,
                   'start': 40.8,
                   'text': 'little did they know I had just run an'},
                  {'duration': 3.421,
                   'start': 42.899,
                   'text': 'ultra marathon through a desert last'},
                  {'duration': 4.32,
                   'start': 44.64,
                   'text': 'month and I was feeling hopeful I could'},
                  {'duration': 4.919,
                   'start': 46.32,
                   'text': 'score just one win I did manage to get'},
                  {'duration': 4.079,
                   'start': 48.96,
                   'text': 'one point on the board and pass all four'},
                  {'duration': 4.98,
                   'start': 51.239,
                   'text': 'events but it was made clear that I am'},
                  {'duration': 4.561,
                   'start': 53.039,
                   'text': 'still no match for the Secret Service'},
                  {'duration': 2.82,
                   'start': 56.219,
                   'text': 'most of my experience at the Secret'},
                  {'duration': 4.22,
                   'start': 57.6,
                   'text': 'Service you can check out the full video'},
                  {'duration': 2.781,
                   'start': 59.039,
                   'text': 'on my YouTube channel'}]})

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

def split_transcript_by_tag(texts):
  split_texts = []
  pprint(texts)
  for t in texts:
    flattened = " ".join(t)
    regex = r"\[.*?\]"
    segments = re.split(regex, flattened)
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
  texts = get_transcript_texts(data)
  texts = data
  split = split_transcript_by_tag(texts)
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
