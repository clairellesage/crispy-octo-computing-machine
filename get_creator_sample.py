from openai import OpenAI
import os
from dotenv import load_dotenv
from get_beat_sheet import get_beat_sheet

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def main():
    client = OpenAI(api_key=api_key)
    beat_sheet = get_beat_sheet()
    topic = "Training to be a stunt driver"
    content = f"Write a video transcript given the following topic: {topic} and the following beat sheet: {beat_sheet}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a content creator assistant, skilled in writing video transcripts given a beat sheet. you output a transcript for a given a 'beat sheet' that may contain any of that follows the given story beats exactly. Your input is a topic of interest that needs to fit the story beats provided. Be creative and match the tone of the input. Do not match the topic of the given beat sheet, instead write a new script about the given topic"},
            {"role": "user", "content": content}
        ]
    )
    print(completion.choices[0].message.content)

main()
