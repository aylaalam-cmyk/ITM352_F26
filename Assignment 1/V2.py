#Interactive quiz system, seccond version
#make a list with the questions and correct answers

questions = [
    ("What is the capital of Hawaii? ", "Honolulu"),
    ("What is the capital of California? ", "Sacramento"),
    ("What is the capital of Texas? ", "Austin"),
    ("The last supper was painted by which artist? ", "Leonardo da Vinci"),
]

for question, correct_answer in questions:
    answer = input(f"{question}")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.")