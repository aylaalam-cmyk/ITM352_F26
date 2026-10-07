# Exercise 6
# Try to append an input from the user to the tuple from Exercise 3

data = ("hello", 10, "goodbye", 3, "goodnight", 5)

value = input("Enter a value to append: ")

try:
    data.append(value)
except Exception as e:
    print(f"An attempt was made to append {value!r} to the tuple.")
    print(f"Error: {type(e).__name__}: {e}")
else:
    print(data)
