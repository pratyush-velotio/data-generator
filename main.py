import json
import random
import string
from datetime import datetime, timedelta
import pandas as pd
import sys

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_column(dtype, n):
    if dtype == "int":
        return [random.randint(1, 1000) for _ in range(n)]
    elif dtype == "float":
        return [round(random.uniform(10.5, 500.5), 2) for _ in range(n)]
    elif dtype == "string":
        return [random_string() for _ in range(n)]
    elif dtype == "bool":
        return [random.choice([True, False]) for _ in range(n)]
    elif dtype == "date":
        start_date = datetime.now() - timedelta(days=365)
        return [(start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d") for _ in range(n)]
    else:
        raise ValueError(f"Unsupported data type: {dtype}")

def generate_data(config):
    num_records = config["num_records"]
    columns = config["columns"]
    
    data = {}
    for col, dtype in columns.items():
        try:
            data[col] = generate_column(dtype, num_records)
        except ValueError as e:
            print(f"Error generating column '{col}': {e}")
            sys.exit(1)

    return pd.DataFrame(data)

def write_data(df, config):
    fmt = config["file_format"].lower()
    fname = config["file_name"]

    if fmt == "csv":
        df.to_csv(f"{fname}.csv", index=False)
        print(f"CSV file saved as {fname}.csv")
    elif fmt == "parquet":
        df.to_parquet(f"{fname}.parquet", index=False)
        print(f"Parquet file saved as {fname}.parquet")
    elif fmt == "json":
        df.to_json(f"{fname}.json", orient="records", lines=True)
        print(f"JSON file saved as {fname}.json")
    else:
        print(f"Unsupported file format: {fmt}")
        sys.exit(1)

def load_config(path="config.json"):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file '{path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Invalid JSON format in '{path}'")
        sys.exit(1)

if __name__ == "__main__":
    configs = load_config()
    if not isinstance(configs, list):
        print("Expected config to be a list of configurations.")
        sys.exit(1)

    for i, config in enumerate(configs):
        print(f"\nGenerating dataset {i + 1}...")
        df = generate_data(config)
        write_data(df, config)
