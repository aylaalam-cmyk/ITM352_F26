#ask the user for a sent (using input())
# turn the sentence into a list of strings (using split())
#Reverse the list.
# Join the list back into a string (using join())
#name: Ayla Alameida
#date: 9/18/2026

sentence = input("Enter a sentence: ")
words = sentence.split(" ")
words.reverse()
reversed_sentence = " ".join(words)
print("Reversed sentence: ", reversed_sentence)

joined_sentence = sentence + " " + reversed_sentence
print("Joined sentence: ", joined_sentence)
