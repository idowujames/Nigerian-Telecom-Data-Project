import pandas as pd
from typing import Dict, List

CORRECTION_MAP: Dict[str, str] = {
    "Ar1tel": "Airtel",
    "G1o": "Glo",
    "9mobil3": "9mobile",
    "MNT": "MTN"
}

GENDER_MAP: Dict[str, str] = {
    "Male": "male",
    "Female": "female",
    "Other": "other"
}

EXCLUDED_VALUES: List[str] = ["G1o", "9mobil3", "Ar1tel", "MNT"]

def read_csv(file_path: str) -> pd.DataFrame:
    """Read CSV file and return DataFrame."""
    return pd.read_csv(file_path)

def clean_transaction_date(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and convert Transaction Date column."""
    df["transaction_date"] = pd.to_datetime(
        df["Transaction Date"].str.replace("T", " ", regex=False).str.split(".").str[0]
    )
    return df.drop(columns=["Transaction Date"])

def clean_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and convert categorical columns."""
    categorical_columns = [
        ("Operator Name", CORRECTION_MAP),
        ("Transaction Type", None),
        ("Customer Gender", GENDER_MAP),
        ("Service Plan", None),
        ("Internet Package", None),
        ("Transaction Status", None)
    ]
    
    for column, mapping in categorical_columns:
        if mapping:
            df[column.lower()] = df[column].replace(mapping).astype("category")
        else:
            df[column.lower()] = df[column].astype("category")
        df = df.drop(columns=[column])
    
    return df

def clean_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and convert numeric columns."""
    numeric_columns = [
        "Transaction Amount",
        "Data Usage (MB)",
        "Call Duration (min)"
    ]
    
    for column in numeric_columns:
        df[column.lower().replace(" ", "_")] = (
            df[column].str.strip().str.replace("$", "", regex=False).astype("float")
        )
        df = df.drop(columns=[column])
    
    return df

def filter_excluded_values(df: pd.DataFrame) -> pd.DataFrame:
    """Filter out rows with excluded values."""
    columns_to_filter = [
        "transaction_type",
        "service_plan",
        "internet_package",
        "transaction_status"
    ]
    
    for column in columns_to_filter:
        df = df[~df[column].isin(EXCLUDED_VALUES)]
    
    return df

def drop_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop unnecessary columns."""
    return df.drop(columns=["Transaction ID", "Customer ID"])

def wrangle(file_path: str) -> pd.DataFrame:
    """Main function to wrangle the data."""
    df = read_csv(file_path)
    df = clean_transaction_date(df)
    df = clean_categorical_columns(df)
    df = clean_numeric_columns(df)
    df = filter_excluded_values(df)
    df = drop_unnecessary_columns(df)
    
    df = df.drop_duplicates().dropna()
    
    df.columns = df.columns.str.replace(" ", "_").str.lower()
    
    df.to_pickle("../data/processed/wrangled-file-export.pkl")
    
    return df

if __name__ == "__main__":
    processed_df = wrangle("../data/raw/nigeria_telecom_transactions_messy_actual_cities.csv")
    print(processed_df.info())