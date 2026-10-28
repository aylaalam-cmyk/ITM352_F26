#read a json file of taxi trip data and create a dataframe and simple stats
import pandas as pd

#read the JSON file into a DataFrame"
results_df = pd.read_json('Taxi_Trips.json')

#display the foirst five rows of the dataframe
print(results_df.heads(6))

#display basic statisics about the DataFrame
print(results_df.describe())

median = results_df["fare"].median()
print("The median fare value is:", median)

