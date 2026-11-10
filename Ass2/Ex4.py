import pandas as pd
import time
from pathlib import Path


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Numbner of rows: {len(df)}")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None


# asks the user what data rows to use for analytics where thet then use this data for the analysis
#generateded using Copiolot from the prompt: "Write a function that asks the user what data rows to use for analytics where thet then use this data for the analysis"
def select_data_rows(data): # defines the function select_data_rows 
    """Return the rows selected by the user using 1-based row numbers."""
    while True: # asks the user to select rows until valid input is provided
        response = input(
            f"\nWhich data rows should this analysis use? "
            f"(1-{len(data)}, e.g. 1-5 or 1,3,7; enter 'all' for every row): "
        ).strip().lower() # strips whitespace and converts to lowercase

        if response == "all": #if the user enters 'all', return the entire dataset
            return data

        try:
            row_numbers = [] # initializes an empty list to store the selected row numbers
            for selection in response.split(","): # splits the user input by commas and iterates over each selection
                selection = selection.strip() #strips whitespace from the selection
                if "-" in selection: # if the selection contains a hyphen, it is treated as a range of rows
                    start, end = (int(value.strip()) for value in selection.split("-", 1)) # splits the selection by the hyphen and converts the start and end values to integers
                    if start < 1 or end < start or end > len(data): # checks if the start and end values are valid row numbers
                        raise ValueError
                    row_numbers.extend(range(start, end + 1))
                else: # if the selection is a single row number, convert it to an integer and add it to the list
                    row_number = int(selection)
                    if row_number < 1 or row_number > len(data): # checks if the row number is valid
                        raise ValueError
                    row_numbers.append(row_number)
        except ValueError: # if a ValueError is raised, print an error message and continue
            print(f"Invalid row selection. Enter a range or list from 1 to {len(data)}.")
            continue

        if not row_numbers: # if the list of selected row numbers is empty, print an error message and continue
            print("Select at least one row.")
            continue

        unique_rows = list(dict.fromkeys(row_numbers)) # removes duplicates while preserving order
        return data.iloc[[row_number - 1 for row_number in unique_rows]]


def display_initial_rows(data):
    """Ask the user how many initial rows to show and print them.

    Accepts a positive integer or 'all'. Invalid entries are reported and
    the user is re-prompted.
    """
    data = select_data_rows(data)
    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all'): "
        ).strip().lower()

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number or 'all'.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return


def show_employees_by_region(data):
    """Print the number of unique employees in each sales region."""
    data = select_data_rows(data)
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())


def get_user_selection(options, prompt, required=False, single=False):
    """Prompt for comma-separated option numbers and return the chosen options.

    Re-prompts on invalid input. An empty entry returns [] unless required.
    """
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected


def generate_custom_pivot_table(data):
    """Interactively build and display a pivot table."""
    data = select_data_rows(data)
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)


def show_average_sales_by_region(data):
    """Pivot average sales (quantity * unit_price) by region, with state and sale type sub-columns."""
    data = select_data_rows(data)
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")

#use while, if, and else to create a main function that prompts the user to choose between loading sales_data.csv or dataset.json
def main():
    while True:
        print("Choose sales data to load:") #chooses between sales_data.csv and dataset.json
        print("1. sales_data.csv")
        print("2. dataset.json")
        choice = input("Enter 1 or 2: ").strip() # prompt user to enter 1 or 2
        if choice in ("1", "2"):
            break
        print("Invalid choice. Please enter 1 or 2.")

    # if the user chooses 1, load sales_data.csv, if the user chooses 2, load dataset.json
    data_file = Path(__file__).resolve().with_name(
        "sales_data.csv" if choice == "1" else "dataset.json"
    )

    try: #load the selected file
        if choice == "1":
            sales_data = load_csv(data_file)
        else: #load dataset.json otherwise
            print(f"Loading JSON file from: {data_file}")
            sales_data = pd.read_json(data_file)
            print(f"JSON file loaded successfully. Number of rows: {len(sales_data)}")
    except Exception as e:
        print("Error reading the JSON file:", e)
        return

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()