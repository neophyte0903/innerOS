import random
from prompts import Journal_prompts
import json
from datetime import datetime
from pathlib import Path


#print('app started')

#--data layer---
JOURNAL_FILE = Path('journal.json')

#functions
def get_prompt():
    return random.choice(Journal_prompts)

def ask_prompt():
    prompt= get_prompt()
    print("Here is your journal prompt:")
    print(prompt)

    userInput =input("\n Your Response:")
    
    save_entry(prompt,userInput)

def save_entry(prompt,response):
    entry={
        "timestamp":datetime.now().isoformat(),
        "prompt":prompt,
        "response":response
    }

    if JOURNAL_FILE.exists():
        with open(JOURNAL_FILE,'r') as f:
            data=json.load(f)
    else:
        data=[]

    data.append(entry)

    with open(JOURNAL_FILE,'w') as f:
        json.dump(data,f,indent=2)

#---main----
def main():
    ask_prompt()


if __name__ == "__main__":
    main()