#ask the user to enter a decimal number, Calculate the square of that number and print it out.
#name: Mahealani Alameida
#Date: 9/2/2024

input_value = input("Enter a floating point number: ")
# Convert the input text to a decimal so Python can perform arithmetic.
float_value = float(input_value)
# Use the exponent operator to calculate the number multiplied by itself.
squared_value = float_value ** 2

print("you entered:", float_value)
print("The square of your number you entered is:", squared_value,)


