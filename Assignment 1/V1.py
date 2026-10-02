#First version of the quiz game
#Name: Mahealani Alameida
#Date: 10/2/2026

answer = input ("What is the capital of Hawaii? ")
if answer == "Honolulu":
    print("Correct!")
else:
    print(f"The answer is 'Honolulu', not {answer!r}.")
#!r prints error in its raw form, including quotes and escape characters

answer = input ("What is the capital of California? ")
if answer == "Sacramento":
    print("Correct!")
else:
    print(f"The answer is 'Sacramento', not {answer!r}.")
    