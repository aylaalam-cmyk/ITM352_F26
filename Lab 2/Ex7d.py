#This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
#create the converion as a function
#Name: Mahealani Alameida
#Date: 9/3/2024

def F_to_C(fahrenheit):
    celsius_value = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return round_celsius, 2

fahrenhight_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenhight_input)

celsius_value = F_to_C(fahrenheit_float)

print("you entered:", fahrenheit_float)
print("The temperature in Celsius is:", celsius_value)

