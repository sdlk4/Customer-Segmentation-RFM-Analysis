import pandas as pd
from pathlib import Path

RAW = Path("data/raw/data.csv")   # change to your actual filename
PROCESSED = Path("data/processed/cleaned_data.csv")

def load_any(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, encoding="latin1")
    elif path.suffix.lower() in (".xlsx", ".xls"):
        return pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Initial shape:", df.shape)

    # Drop rows with missing CustomerID
    df = df.dropna(subset=["CustomerID"])
    print("After removing missing CustomerID:", df.shape)

    # Remove negative or zero Quantity
    df = df[df["Quantity"] > 0]
    print("After removing negative Quantity:", df.shape)

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df = df.dropna(subset=["InvoiceDate"])
    print("After fixing InvoiceDate:", df.shape)

    # Create TotalAmount
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]
    print("Added TotalAmount column.")

    # Keep only required columns
    df = df[["InvoiceNo", "CustomerID", "InvoiceDate", "Quantity", "UnitPrice", "TotalAmount"]]
    print("Final cleaned shape:", df.shape)

    return df

def save_processed(df: pd.DataFrame):
    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED, index=False)
    print(f"Processed data saved to: {PROCESSED}")

def main():
    df = load_any(RAW)
    print("Loaded successfully.")
    df = clean_data(df)
    save_processed(df)

if __name__ == "__main__":
    main()
