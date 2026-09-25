#determine movie price, the rules are:
#- The normal price is $14
#- If someone is 65 or older, they pay $8.
#- If it is Tuesday, the price is $10.
#- If it is a matinee, the price is $5 for seniors and $8 otherwise
#Name: Mahealani Alameida
#Date: 9/25/26

age = 22
day = "Tuesday"
mantinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if mantinee:
    if age >= 65:
        price = 5
    else:
        price = 8
print(f"Day: {day}, Matinee: {mantinee}")
if (age>= 65):
    print("welcome, senior")
else:
    print("Welcoe, non-senior")
print(f"Ticket price is ${price:.2f}")