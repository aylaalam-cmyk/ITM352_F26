#Python code that creates a list with a variety of different values. 
# Include control logic (if, elif, else) that will print different messages 
# whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. 
# Test your code on lists with several different lengths


def list_length(my_list):
    if len(my_list) < 5:
        print(f"List has {len(my_list)} List contains fewer than 5 elements.")

    elif 5 <= len(my_list) <= 10:
        print(f"list has {len(my_list)} Between 5 and 10 (inclusive)")

    else:
        print(f"list has {len(my_list)} More than 10 elements")










