#idl

first = input("enter your first name: ")
middle_inital = input("enter your middle initial: ")
last = input("enter your last name: ")

full_name = first + " " + middle_inital + ". " + last
print("Your full name is:", full_name)

print(f"your full name is: {first} {middle_inital}. {last}")
print("your full name using percent formatting is: %s %s. %s" % (first, middle_inital, last))
print("your full name using format method is: {} {}. {}".format(first, middle_inital, last))
