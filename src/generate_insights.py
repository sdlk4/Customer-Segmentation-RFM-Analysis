import pandas as pd
from pathlib import Path

INPUT = Path("data/processed/rfm_segments.csv")
OUTPUT = Path("outputs/rfm_summary.md")

def load_rfm():
    return pd.read_csv(INPUT)

def generate_summary(rfm: pd.DataFrame) -> str:
    total_customers = len(rfm)
    segments_count = rfm["Segment"].value_counts()
    segments_revenue = rfm.groupby("Segment")["Monetary"].sum().sort_values(ascending=False)

    summary = []
    summary.append("# RFM Segmentation Insights\n")
    summary.append(f"**Total Customers Analyzed:** {total_customers}\n")

    summary.append("## Customer Count by Segment\n")
    summary.append(segments_count.to_string())
    summary.append("\n")

    summary.append("## Revenue Contribution by Segment\n")
    summary.append(segments_revenue.to_string())
    summary.append("\n")

    summary.append("## Interpretation\n")
    summary.append("- Champions are highly valuable customers with highest recency, frequency, and spending.")
    summary.append("\n- Big Spenders contribute significant revenue even if they don’t purchase often.")
    summary.append("\n- Hibernating customers need reactivation strategies.")
    summary.append("\n- At Risk customers require targeted retention offers.\n")

    return "\n".join(summary)

def save_summary(text: str):
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Insights saved to: {OUTPUT}")

def main():
    rfm = load_rfm()
    summary_text = generate_summary(rfm)
    save_summary(summary_text)

if __name__ == "__main__":
    main()
