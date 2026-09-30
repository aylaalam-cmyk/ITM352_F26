#even = *number* is the starting point
'''evens = [2]
num = 2

#making it < has it stop on time the <= gives the error of 2 more than needed
while evens[-1] < 50:
    num += 2
    evens.append(num)

print(evens)'''

#most effecitan way of doing it *I think*
evens = []
for num in range(2, 51, 2):
    evens.append(num)
print(evens)


