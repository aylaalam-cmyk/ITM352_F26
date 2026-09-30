#Python code that creates a list with a variety of different values. 
# Include control logic (if, elif, else) that will print different messages 
# whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. 
# Test your code on lists with several different lengths


def list_length(my_list):
    if len(my_list) < 5:
        print(f"List has {len(my_list)} elements: fewer than 5.")

    elif 5 <= len(my_list) <= 10:
        print(f"List has {len(my_list)} elements: between 5 and 10 inclusive.")

    else:
        print(f"List has {len(my_list)} elements: more than 10.")

test_cases = [
    [1, "two", 3.0, True],
    [1, "two", 3.0, True, "five"],
    [1, "two", 3.0, True, "five", 6, "seven", 8.0, False, "ten"],
    [1, "two", 3.0, True, "five", 6, "seven", 8.0, False, "ten", 11],
]

for test_list in test_cases:
    list_length(test_list)


















