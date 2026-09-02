#ask the user to enter a decimal number, Calculate the square of that number,
# round it to two decimal places, and print it out.
#name: Mahealani Alameida
#Date: 9/2/2024

input_value = input("Enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2
rounded_value = round(squared_value, 2)

print("you entered:", float_value)
print("The square of your number you entered is:", rounded_value,)

