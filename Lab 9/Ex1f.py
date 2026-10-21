#Open names.text and read its contents
#append a new name at the end of the file

with open("names.txt", "r") as file_object:
    content_list = file_object.readlines()
    print(content_list)
    file_object.write("doe, john\n")
    