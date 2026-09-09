#this program prompts the user to enter a weight in pounds and then converts it to kilograms and displays the result.
#Name: Mahealani Alameida
#Date: 9/3/2024

#print("The weight in kilograms is:", float(input("Enter weight in pounds: "))*0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds = input("Enter weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = weight_in_pounds_float * KG_TO_POUNDS

print("you entered:", weight_in_pounds_float)
print("The weight in kilograms is:", weight_in_kilograms)