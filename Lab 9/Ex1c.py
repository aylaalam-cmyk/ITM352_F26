#open filr and read its contents

with open("example.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    contents_list = contents.split("\n")
    print(f"Number of Names: {len(contents_list)}")
    for name in contents_list:
        print(name)