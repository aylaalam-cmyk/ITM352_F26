birth_year = input("Enter your birth year: ")
birth_month = int(input("Enter your birth month (1-12): "))
current_year = 2026
current_month = 9
age = current_year - int(birth_year)

if birth_month > current_month:
	age -= 1

print("you entered:", birth_year)
print("your birth month is:", birth_month)
print("your age is:" + str(age))