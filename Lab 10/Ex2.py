#create a Pandas dataframe from individual lists.
# DO some simple stats on the data 
import pandas as pd

#list of individuals' names, ages, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

raw_data = zip(ages, gender)

#create a pandas dataframe from the list
df = pd.DataFrame(data=raw_data, index=names, columns=["Age", "Gender"])

summary = df.describe() # get summary statistics for the dataframe
print(summary) #print the summary statistics

#calculate average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
print("\Average age by gender")
print()