import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Set seed for reproducibility
Faker.seed(0)
np.random.seed(0)

# Define the number of rows
num_rows = 50000

# List of actual cities in Nigeria
nigerian_cities = [
    "Lagos", "Kano", "Ibadan", "Abuja", "Port Harcourt", "Benin City", "Maiduguri",
    "Zaria", "Aba", "Jos", "Ilorin", "Oyo", "Enugu", "Abeokuta", "Onitsha",
    "Warri", "Sokoto", "Kaduna", "Osogbo", "Akure", "Owerri", "Calabar",
    "Uyo", "Asaba", "Makurdi", "Minna", "Awka", "Jalingo", "Gombe", "Bauchi"
]

# Introduce some inconsistencies and missing values
def introduce_missingness(value, probability=0.1):
    return value if random.random() > probability else np.nan

def introduce_typos(value, typos=["MNT", "G1o", "Ar1tel", "9mobil3"]):
    return value if random.random() > 0.1 else random.choice(typos)

def introduce_inconsistent_formats(value, formats=["{:.2f}", "{:.1f}", "{:.0f}", "${:.2f}"]):
    return formats[random.randint(0, len(formats)-1)].format(value) if random.random() > 0.1 else value

# Generate messy data for Nigeria Telecom Operators with actual Nigerian cities
data_telecom_messy_actual_cities = {
    "Transaction ID": [introduce_missingness(fake.uuid4()) for _ in range(num_rows)],
    "Customer ID": [introduce_missingness(fake.uuid4()) for _ in range(num_rows)],
    "Transaction Date": [introduce_missingness(fake.date_time_between(start_date='-1y', end_date='now').isoformat() if random.random() > 0.2 else fake.date() + " " + fake.time()) for _ in range(num_rows)],
    "Operator Name": [introduce_typos(random.choice(['MTN', 'Airtel', 'Glo', '9mobile'])) for _ in range(num_rows)],
    "Transaction Type": [introduce_typos(random.choice(['Airtime Purchase', 'Data Purchase', 'Bill Payment'])) for _ in range(num_rows)],
    "Transaction Amount": [introduce_missingness(inconsistent_formats := introduce_inconsistent_formats(round(random.uniform(100.0, 20000.0), 2))) for _ in range(num_rows)],
    "Customer Age": [introduce_missingness(random.randint(18, 70)) for _ in range(num_rows)],
    "Customer Gender": [introduce_missingness(random.choice(['Male', 'Female', 'Other', 'male', 'female'])) for _ in range(num_rows)],
    "Customer Location": [introduce_missingness(random.choice(nigerian_cities)) for _ in range(num_rows)],
    "Service Plan": [introduce_typos(random.choice(['Prepaid', 'Postpaid'])) for _ in range(num_rows)],
    "Data Usage (MB)": [introduce_missingness(inconsistent_formats := introduce_inconsistent_formats(round(random.uniform(0.0, 5000.0), 2))) for _ in range(num_rows)],
    "Call Duration (min)": [introduce_missingness(inconsistent_formats := introduce_inconsistent_formats(round(random.uniform(0.0, 300.0), 2))) for _ in range(num_rows)],
    "SMS Sent": [introduce_missingness(random.randint(0, 100)) for _ in range(num_rows)],
    "Internet Package": [introduce_typos(random.choice(['Daily', 'Weekly', 'Monthly'])) for _ in range(num_rows)],
    "Transaction Status": [introduce_typos(random.choice(['Completed', 'Pending', 'Failed'])) for _ in range(num_rows)]
}

# Create DataFrame
df_telecom_messy_actual_cities = pd.DataFrame(data_telecom_messy_actual_cities)

# Introduce duplicates
# df_telecom_messy_actual_cities = df_telecom_messy_actual_cities.concat(df_telecom_messy_actual_cities.sample(frac=0.1))
df_telecom_messy_actual_cities = pd.concat([df_telecom_messy_actual_cities, df_telecom_messy_actual_cities.sample(frac=0.1)])

# Shuffle the rows to mix duplicates
df_telecom_messy_actual_cities = df_telecom_messy_actual_cities.sample(frac=1).reset_index(drop=True)

# Save to CSV
csv_path_telecom_messy_actual_cities = 'nigeria_telecom_transactions_messy_actual_cities.csv'
df_telecom_messy_actual_cities.to_csv(csv_path_telecom_messy_actual_cities, index=False)

print(f"Dataset saved to {csv_path_telecom_messy_actual_cities}")