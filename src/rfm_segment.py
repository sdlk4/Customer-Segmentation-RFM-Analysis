import pandas as pd
from pathlib import Path

# Paths
PROCESSED = Path("data/processed/cleaned_data.csv")
OUTPUT = Path("data/processed/rfm_segments.csv")

# -----------------------------
# Load processed data
# -----------------------------
def load_data(path: Path) -> pd.DataFrame:
    print(f"Loading processed data from: {path}")
    return pd.read_csv(path, parse_dates=["InvoiceDate"])

# -----------------------------
# Calculate RFM metrics
# -----------------------------
def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    print("Calculating RFM metrics...")

    # Reference = latest purchase date
    reference_date = df["InvoiceDate"].max()
    print(f"Reference date for recency: {reference_date}")

    # Group by customer
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (reference_date - x.max()).days,  # Recency
        "InvoiceNo": "count",                                      # Frequency
        "TotalAmount": "sum"                                       # Monetary
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]
    print("RFM metrics calculated. Sample:")
    print(rfm.head())

    return rfm

# -----------------------------
# R/F/M Scoring (1–5)
# -----------------------------
def score_rfm(rfm: pd.DataFrame) -> pd.DataFrame:
    print("Assigning R, F, M scores...")

    # Recency — lower is better
    rfm["R_score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])

    # Frequency — higher is better
    rfm["F_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

    # Monetary — higher is better
    rfm["M_score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

    # Combined score
    rfm["RFM_Score"] = (
        rfm["R_score"].astype(str) +
        rfm["F_score"].astype(str) +
        rfm["M_score"].astype(str)
    )

    print("RFM scoring done. Sample:")
    print(rfm.head())

    return rfm

# -----------------------------
# Segment customers
# -----------------------------
def assign_segments(rfm: pd.DataFrame) -> pd.DataFrame:
    print("Assigning customer segments...")

    segments = []

    for _, row in rfm.iterrows():
        r = int(row["R_score"])
        f = int(row["F_score"])
        m = int(row["M_score"])

        if r >= 4 and f >= 4 and m >= 4:
            segments.append("Champions")

        elif f >= 4:
            segments.append("Loyal Customers")

        elif m >= 4:
            segments.append("Big Spenders")

        elif r == 5 and f <= 2:
            segments.append("New Customers")

        elif r >= 4:
            segments.append("Promising")

        elif r <= 2 and (f >= 3 or m >= 3):
            segments.append("At Risk")

        elif r <= 2 and f <= 2:
            segments.append("Hibernating")

        else:
            segments.append("Others")

    rfm["Segment"] = segments

    print("Segments assigned. Sample:")
    print(rfm.head())

    return rfm

# -----------------------------
# Save output
# -----------------------------
def save_results(rfm: pd.DataFrame, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rfm.to_csv(output_path, index=True)
    print(f"RFM result saved to: {output_path}")

# -----------------------------
# Main pipeline
# -----------------------------
def main():
    df = load_data(PROCESSED)
    rfm = calculate_rfm(df)
    rfm_scored = score_rfm(rfm)
    rfm_final = assign_segments(rfm_scored)
    save_results(rfm_final, OUTPUT)

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main()
