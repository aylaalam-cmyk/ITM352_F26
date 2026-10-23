# save the dictionary of quiz questions to the JSON file

import json

questions = {
    "What is the capital of France?": [
        "Paris",
        "Toulouse",
        "Nice",
        "Avignon"
    ],
    "What is the capital of Germany?": [
        "Berlin",
        "Munich",
        "Hamburg",
        "Frankfurt"
    ],
    "What is the capital of Italy?": [
        "Rome",
        "Venice",
        "Milan",
        "Florence"
    ],
    "What is the number of Islands in Hawaii?": [
        "8",
        "7",
        "6",
        "9"
    ],
    "The last supper was painted by which artist?": [
        "Leonardo da Vinci",
        "Michelangelo",
        "Raphael",
        "Donatello"
    ]
}

filename = "quiz_questions.json"

# open the file in write mode and save the dictionary to the file
with open(filename, 'w') as file:
    json.dump(questions, file, indent=2)

print(f"Quiz questions saved to {filename}")