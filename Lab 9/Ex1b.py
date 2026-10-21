# open file usonh "with"

with open("names.txt", "r") as file_object:
    print(type(file_object))    

print("FIle is cloesd:", file_object.closed)
