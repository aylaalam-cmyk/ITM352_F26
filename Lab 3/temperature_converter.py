def convert_temperature(temperature, conversion_function):
    return conversion_function(temperature)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


print(convert_temperature(100, celsius_to_fahrenheit))
print(convert_temperature(32, fahrenheit_to_celsius))
print(convert_temperature(0, celsius_to_kelvin))
