#testing the use fo assertions.
#Name: Mahealani Alameida
#Date: 9/25/26

def celsius_to_fahrenheit(celsius):
	"""Convert Celsius to Fahrenheit."""
	assert celsius >= -273.15, "Temperature cannot be below absolute zero."
	fahrenheit = (celsius * 9 / 5) + 32
	return fahrenheit

print(celsius_to_fahrenheit(0)) #should pritn 32.0
print(celsius_to_fahrenheit(100)) #should pritn 212.0
print(celsius_to_fahrenheit(-300)) #should raise and Assertion error

