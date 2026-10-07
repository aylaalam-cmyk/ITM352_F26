#Interactive quiz system, 3rd version
#make a list with the questions and correct answers

questions = [
    ("What is the capital of France? ", "Paris", "Toulouse", "Nice", "Avignon"),
    ("What is the capital of Germany? ", "Berlin", "Munich", "Hamburg", "Frankfurt"),
    ("What is the capital of Italy? ", "Rome", "Venice", "Milan", "Florence"),
    ("The last supper was painted by which artist? ", "Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"),
]

for question, in questions.items():
    correct_answer = question[0]
    answer = input(f"{question}")
    for answer in answers:
        print(f"-{answer}")
    
    answer = input("Your answer: ")
    if answer == correct_answer:
        print("Correct!")
    
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")
    