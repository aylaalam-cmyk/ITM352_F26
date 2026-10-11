# Assignment 1: Interactive Quiz System
# I need to Allow for multiple correct answers.
# & Add explanations for why the correct answer is the correct answer.
# Answers: 1.ʻAʻaliʻi, Maʻo Hau Hele, 2. Koa, Hala, 3. Naupaka, ʻŌhiʻa Lehua, 4. Pōpolo, ʻIlima, 5. ʻIliahi (Sandalwood), Maʻo Hau Hele, 6. Silversword, Naupaka

from string import ascii_lowercase
import random
import json
from pathlib import Path
with Path(__file__).with_name("questions.json").open(encoding="utf-8") as question_file:
    questions = json.load(question_file)


NUM_QUESTIONS_PER_QUIZ = 6

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]


def ask_question(question, question_data):    
    alternatives = question_data["answers"]
    correct_response = question_data["correct_response"]
    correct_answer = (alternatives[0], alternatives[1])
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)

    if answer in correct_answer:
        print(f"Correct!")
        print(f"{correct_response}")
        return 1
    else:
        print(f"The correct answers are '{correct_answer!r}', not {answer!r}. ")
        print(f"{correct_response}")
        return 0


# Main program logic starts here
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

# Main Loop
for num, (question, question_data) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, question_data)

print(f"\nYou got {num_correct} correct.")