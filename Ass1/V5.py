#Interactive quiz system, 4th version
#make a list with the questions and correct answers

from string import ascii_lowercase

questions = [
    ("What is the capital of France? ", "Paris", "Toulouse", "Nice", "Avignon"),
    ("What is the capital of Germany? ", "Berlin", "Munich", "Hamburg", "Frankfurt"),
    ("What is the capital of Italy? ", "Rome", "Venice", "Milan", "Florence"),
    ("What is the number of Islands in Hawaii? ", "8", "7", "6", "9"),
    ("The last supper was painted by which artist? ", "Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"),
]

num_correct = 0

for num, (question, *answers) in enumerate(questions, start=1):
    correct_answer = answers[0]
    print(f"\nQuestion {num}: {question}")

    Sorted_answers = sorted(answers)
    label_answers = dict(zip(ascii_lowercase, Sorted_answers))

    for label, answer in label_answers.items():
        print(f"{label}. {answer}")
     
    answer_label = input("Choice? ").lower()
    answer = label_answers.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")

    print(f"\nYou got {num_correct} correct answers out of {num} questions.")