#Get public liscance data from the city of Chicago's data portal
import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)
json_file = "rr23-ymwb"

results = client.get(json_file, limit=2000)
#convert to a data frame
results_df = pd.DataFrame.from_records(results)
results_df.head()


vehicle= results_df[["public_vehicle_number", "public_vehicle_source"]]
print("Public vehicle and fuel sources:")

vehicle.info()
vehicle_by_fuel = vehicle.groupby("public_vehicle_source").count()
print(vehicle_by_fuel)


