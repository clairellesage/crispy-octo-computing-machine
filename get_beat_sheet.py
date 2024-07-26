from openai import OpenAI
import os
from dotenv import load_dotenv
from get_data import get_data
from pprint import pprint

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_beat_sheet():
  client = OpenAI(api_key=api_key)
  t = get_data()
  pprint(t)
  content = f"Write a beat sheet template for the following video transcript: {t}"
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "You are a summarizer assistant, skilled in summarizing video transcripts. you output a 'beat sheet' for each video in the dict, that may contain any of the following story beats but does not require all of them: 1. Opening image. A short description of the very first moment or event people will see. Strive for an exciting opening that makes people lean in and sets the tone for the story you''re telling. 2. Introduction. One or more beats in which your characters and setting come into clear focus. Who is the main character? What does she want? What is holding her back from getting it. 3. Statement of theme. What is your film about? This is the opportunity to show the audience. 4. Catalyst. This is the moment in which the main character either actively sets out to achieve her goals, or is forced to go down the path plotted for her. Think of the most extreme thing that can happen to your characters, make it happen, and go from there. 5. Debate. However, even great characters have their doubts. The main character might need to confer with other characters, or do some soul-searching, before embarking on her journey. 6. B-Story or B-Plot. The best time to introduce a secondary plot is roughly towards the end of the first act. The audience will now be familiar with the main character, her world, and her plight, and therefore should be more invested in the other goings-on that may affect the story. The B-Plot often carries the first act through to the second act. 7. New characters. As the main character goes through the story, she will likely meet other characters who help or hurt her. This opportunity for one or more new characters, which should come towards the first half of the second act, allows a writer to deepen the conflict and increase tension in the narrative. 8. Midpoint. Exactly halfway through your story. The characters have made their decisions, and now reality sets in. 9. Low point. Just as as the main character seems to be within reach of her goal, something happens that derails her progress or makes her question her journey. A sense of despair or confusion may set in. 10. Climax. This is the big moment in which the action spikes and everything that you’ve set up before now comes to a head. In a traditional action film, the climax might be a big chase or fight scene. In short, the climax should show your main character just within reach of her goal. 11. Beginning of the end. Once the main character has reached her goal (or come up short), the story begins to wind down. Any secondary storylines should start coming to a close. 12. Finale. The final scene viewers will see. This should cap off the theme of the story, and leave your audience with a sense of how your protagonist has grown through the events of the film. Please output in the following format: story beat name, e.g. 'Introduction' or 'Catalyst' and description of the event  e.g. New Characters: Michelle meets Brian. Keep the description concise and to the point, only 1 sentence. Use the comma-separated list as hints for a new story beats"},
      {"role": "user", "content": content}
    ]
  )
  print(completion.choices[0].message.content)

get_beat_sheet()
