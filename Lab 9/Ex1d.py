#Read a file of names one line at a time and print each time

with open("example.txt", "r") as file_object:
    while (line := file_object.readline()):
        print(line.strip())
        print(number_of_names )
        for name in line.split():
            print(name.strip())