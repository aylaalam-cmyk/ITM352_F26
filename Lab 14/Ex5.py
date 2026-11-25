# Retrieve and print the latest mortgage rates from the Hawaii Board of REALTORS.
from io import StringIO

import pandas as pd
import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url, timeout=30)
response.raise_for_status()

# Extract the mortgage rate table from the downloaded HTML.
tables = pd.read_html(StringIO(response.text))
rate_table = tables[0]

# Print each lender's mortgage term and rates.
for _, row in rate_table.iterrows():
    print(
        f"{row['Lender']} | {row['Term/Type']} | "
        f"Rate: {row['Interest Rate']}% | "
        f"Points: {row['% Points']}% | APR: {row['% *APR']}%"
    )
