#read a file of quiz questiona and save as a dictionary

import json
filename = "quiz_questions.json"
with open(filename, 'r') as file:
    quiz_questions = json.load(file)

print(quiz_questions)