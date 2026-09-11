#create a function-call it midpoint that takes two numbers as imput and returns the value halfway between them.

def midpoint(xnum1, num2):
    return (xnum1 + num2) / 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The midpoint is:", midpoint(num1, num2))