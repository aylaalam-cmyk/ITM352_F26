def celsius_to_fahrenheit(celsius):
	"""Convert a temperature from Celsius to Fahrenheit."""
	assert celsius >= -273.15, "Temperature cannot be below absolute zero."
	return (celsius * 9 / 5) + 32


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

# Assertions are useful for checking assumptions while a program is running.
# For example, they can verify that a temperature is physically possible,
# that a list contains the data an algorithm expects, or that a calculated
# value stays within an allowed range. If an assumption is false, an
# AssertionError stops the program and points out the problem.
#testng