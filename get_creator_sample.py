from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def main():
    client = OpenAI(api_key=api_key)
    beat_sheet = [{"Opening Image": "The video begins with a tense atmosphere as Michelle nervously prepares to join the bomb squad academy, setting the tone for a challenging and dangerous journey ahead."}, {"Introduction": "Michelle is introduced as the main character who is eager but apprehensive about her intense training with the bomb squad. She wants to prove herself and gain the skills necessary to safely handle explosives, but she is held back by her fear and the daunting challenges ahead."}, {"Statement of Theme": "The film explores themes of bravery, perseverance, and personal growth in the face of fear and uncertainty. It highlights the mental and physical challenges involved in becoming a bomb technician."}, {"Catalyst": "Michelle learns that she will soon be participating in a physical assessment that tests her endurance, dexterity, and memory while wearing a 65 lb bomb suit. This moment propels her into the rigorous training of the bomb squad.\n\n5. Debate: Michelle expresses her doubts about whether she is truly ready for the physical and mental challenges of the assessment, revealing her vulnerability before the big test."}, {"B-Story": "The camaraderie between Michelle and the other bomb squad recruits, particularly Brian and Brad, adds depth to her journey as they provide support and encouragement through the challenges.\n\n7. New Characters: Michelle interacts with Brian and Brad, fellow recruits who offer insights and help ease her nerves about the intense training she is about to face."}, {"Midpoint": "Michelle successfully completes her physical agility test after grappling with the limitations of the bomb suit and her own physical endurance, marking a turning point where she begins to regain confidence."}, {"Low Point": "After the intense physical assessment, Michelle has to suit up again in a hazardous materials suit, which heightens her fears and challenges her resolve as she prepares for the next critical test."}, {"Climax": "Michelle, now layered in both the bomb suit and hazmat suit, faces her fears head-on as she is confined in a dark shipping container, providing a thrilling peak moment where she must confront the unknown."}, {"Beginning of the End": "After completing the initial physical challenges and passing her tests, Michelle begins to reflect on her journey and the sacrifices involved in her training."}, {"Finale": "The video concludes with Michelle''s hopeful outlook as she contemplates the challenges and triumphs she faces while pursuing her dream of becoming a bomb technician, leaving the audience with a sense of her growth and determination."}]
    topic = "Training to be a stunt driver"
    content = f"Write a video transcript given the following topic: {topic} and the following beat sheet: {beat_sheet}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a content creator assistant, skilled in writing video transcripts given a beat sheet. you output a transcript for a given a 'beat sheet' that may contain any of that follows the given story beats exactly. Your input is a topic of interest that needs to fit the story beats provided. Be creative and match the tone of the input. Do not match the topic of the given beat sheet, instead write a new script about the given topic"},
            {"role": "user", "content": content}
        ]
    )
    print(completion.choices[0].message)

main()
