#Interactive quiz system, 4th version
#make a list with the questions and correct answers

questions = [
    ("What is the capital of France? ", "Paris", "Toulouse", "Nice", "Avignon"),
    ("What is the capital of Germany? ", "Berlin", "Munich", "Hamburg", "Frankfurt"),
    ("What is the capital of Italy? ", "Rome", "Venice", "Milan", "Florence"),
    ("The last supper was painted by which artist? ", "Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"),
]

for question, in answers in questions.items():
    correct_answer = answers[0]
    Sorted_answers = sorted(answers)

    for label, answer in enumerate(question[1:], start=1):
        print(f"{label}. {answer}")
     
    answer_label = int(input(f"{question} "))
    answer = sorted(question[1:])[answer_label - 1]

    if answer == correct_answer:
        print("Correct!")
    
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")
    