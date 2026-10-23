#Read a csv file and compute the average, minimum, and maximum salary of the employees


import csv
csv_filename = "cleaning_company_employees.csv"
salaries = []

#read the csv file and store the salaries in a list
with open(csv_filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader) #skip the header row
    print(f"Headers: {headers}") #find the index of the salary column
    salaries_index = headers.index("Annual_Salary") #find the index of the salary column
    for row in reader:
        salary = float(row[salaries_index]) #convert the salary to a float
        salaries.append(salary) #append the salary to the list

    # compute salary stats
    avg_salary = sum(salaries) / len(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)

    #print the salary stats
    print(f"Average Salary: {avg_salary}")
    print(f"Minimum Salary: {min_salary}") 
    print(f"Maximum Salary: {max_salary}")


