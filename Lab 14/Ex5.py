#Get a Jsn file from CUty of Chicago's data portal and analyze driver types
import pandas as pd
import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

response_json = response.json()

print("Driver types and license counts:")
print(response_json)

response_df = pd.DataFrame.from_records(response_json)
response_df.columns = ["Driver Type", "Count"]
response_df = response_df.set_index("Driver Type")

print(response_df)