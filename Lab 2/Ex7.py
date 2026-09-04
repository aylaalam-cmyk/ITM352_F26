#This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
#Name: Mahealani Alameida
#Date: 9/3/2024


fahrenhight_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenhight_input)

celsius_value = (fahrenheit_float - 32) * 5 / 9

celsius_value = F_to_C(fahrenheit_float)

print("you entered:", fahrenheit_float)
print("The temperature in Celsius is:", celsius_value)

