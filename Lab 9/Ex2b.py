#Read a csv file and compute the average, minimum, and maximum salary of the employees
# print info about file existance and permision beofr reading the file

import csv
import os
from zipfile import Path

#ceck if hte file exists and is readable
if not os.path.exists("cleaning_company_employees.csv"):
    print(f"Error: File cleaning_company_employees.csv is not found")
    exit(1)
if not os.access("cleaning_company_employees.csv", os.R_OK):
    print(f"Error: File cleaning_company_employees.csv is not readable")
    exit(1)
else:
    file_size = os.path.getsize("cleaning_company_employees.csv")
    print(f"File exists and is readable. File size: {file_size} bytes")



csv_filename = Path(__file__).resolve().parent.parent / "cleaning_company_employees.csv"
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


