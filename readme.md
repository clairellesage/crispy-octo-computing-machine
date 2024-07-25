This repository contains scripts to:
    1) retrieve youtube data (get_data.py)
    2) extract a beat sheet (get_beat_sheet.py)
    3) write a sample transcript (get_creator_sample.py)

To run:
    - clone the repository
    - pip install -r requirements.txt
    - acquire YOUTUBE_API_KEY, OPENAI_API_KEY and put tokens .ent file
    - from the command line in the repository, run
        - `python3 get_data.py` to aquire latest video transcripts
        - `python3 get_beat_sheet.py` > outputs sample beat sheet to cmd line
        - `python3 get_creator_sample.py` > output creator sample to cmd line
