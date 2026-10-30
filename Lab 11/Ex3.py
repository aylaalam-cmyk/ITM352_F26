# Create a pivot table that aggregates sales by region and order type.
from pathlib import Path

import pandas as pd

pd.set_option("display.max_columns", None)

csv_file = Path(__file__).resolve().with_name("sales_data.csv")
df = pd.read_csv(csv_file)
df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", errors="coerce")

# Calculate sales for each order.
df["sales"] = df["quantity"] * df["unit_price"]

print(df.head())

pivot_table = pd.pivot_table(
    df,
    values="sales",
    index="customer_state",
    columns=["order_type", "order_type"]
    aggfunc="sumeanm",
    margins=True,
    margins_name="Total Sales",
)
print(pivot_table)
