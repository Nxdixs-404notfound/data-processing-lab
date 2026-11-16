# OOP Data Processing Lab

## Lab Overview
This lab refactors a procedural CSV data processing script into an Object-Oriented Programming (OOP) design in Python. It implements classes to load CSV datasets, manage multiple data tables inside a simple in-memory database, and perform relational operations such as filtering, aggregation, and joining tables on a common attribute.

## Project Structure
```text
data-processing-lab/
│
├── README.md              # Project documentation
├── Cities.csv             # Dataset containing city names, countries, coordinates, and temperatures
├── Countries.csv          # Dataset containing country names, populations, EU status, and coastline status
└── data_processing.py     # OOP implementation (DataLoader, Table, DB) and test queries
```

## Design Overview

### 1. `DataLoader`
Handles reading CSV files from disk and converting each row into a Python dictionary.
- **Attributes:**
  - `base_path` (`Path`): Directory path where the CSV dataset files are located.
- **Key Methods:**
  - `__init__(base_path=None)`: Sets the base directory path (defaults to the directory containing `data_processing.py`).
  - `load_csv(filename)`: Reads the specified CSV file using `csv.DictReader` and returns a list of dictionaries.

### 2. `Table`
Represents a relational table stored as a list of dictionaries and provides data manipulation operations.
- **Attributes:**
  - `table_name` (`str`): Name identifying the table.
  - `table` (`list[dict]`): List of row dictionaries representing records in the table.
- **Key Methods:**
  - `__init__(table_name, table)`: Initializes a table with its name and row data.
  - `filter(condition)`: Returns a new `Table` containing only rows that satisfy the given `condition` function.
  - `aggregate(aggregation_function, aggregation_key)`: Extracts values for `aggregation_key` (converting numeric values to `float` when applicable) and applies `aggregation_function`.
  - `join(other_table, common_key)`: Performs an inner join between the current table and `other_table` where values for `common_key` match, returning a new combined `Table`.
  - `__str__()`: Returns a readable string formatted as `table_name:table_data`.

### 3. `DB`
Acts as a lightweight database container managing multiple `Table` instances.
- **Attributes:**
  - `tables` (`list[Table]`): A list storing inserted `Table` objects.
- **Key Methods:**
  - `__init__()`: Initializes an empty list of tables.
  - `insert(table)`: Adds a `Table` object into the database.
  - `search(table_name)`: Searches and returns the `Table` matching `table_name` (or `None` if not found).

## How to Test and Run Your Code
1. Ensure Python 3 is installed and that `data_processing.py`, `Cities.csv`, and `Countries.csv` are located in the same directory.
2. Open a terminal in the project directory and run:
   ```bash
   python3 data_processing.py
   ```
3. Verify that the console output prints the filtered city/country lists, temperature aggregations, and joined table records matching the expected test results.