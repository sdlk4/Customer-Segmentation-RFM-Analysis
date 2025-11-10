import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

INPUT = Path("data/processed/rfm_segments.csv")
OUTPUT_DIR = Path("outputs/plots")

def load_data():
    df = pd.read_csv(INPUT)
    return df

def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def plot_recency(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df["Recency"], bins=50, kde=True, color="green")
    plt.title("Recency Distribution")
    plt.xlabel("Days Since Last Purchase")
    plt.ylabel("Number of Customers")
    plt.savefig(OUTPUT_DIR / "recency_distribution.png")
    plt.close()

def plot_frequency(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df["Frequency"], bins=50, kde=True, color="blue")
    plt.title("Frequency Distribution")
    plt.xlabel("Number of Purchases")
    plt.ylabel("Number of Customers")
    plt.savefig(OUTPUT_DIR / "frequency_distribution.png")
    plt.close()

def plot_monetary(df):
    plt.figure(figsize=(10,5))
    sns.boxplot(x=df["Monetary"], color="orange")
    plt.title("Monetary Distribution (Boxplot)")
    plt.xlabel("Total Amount Spent")
    plt.savefig(OUTPUT_DIR / "monetary_distribution.png")
    plt.close()

def plot_segments(df):
    plt.figure(figsize=(12,6))
    sns.countplot(y=df["Segment"], order=df["Segment"].value_counts().index)
    plt.title("Customer Count by Segment")
    plt.xlabel("Count")
    plt.ylabel("Segment")
    plt.savefig(OUTPUT_DIR / "segment_count.png")
    plt.close()

def plot_rfm_scatter(df):
    plt.figure(figsize=(10,7))
    sns.scatterplot(data=df, x="Frequency", y="Monetary", hue="Segment", palette="tab10")
    plt.title("Frequency vs Monetary (Segment Colored)")
    plt.savefig(OUTPUT_DIR / "frequency_vs_monetary_scatter.png")
    plt.close()

def main():
    ensure_output_dir()
    df = load_data()

    print("Generating plots...")

    plot_recency(df)
    plot_frequency(df)
    plot_monetary(df)
    plot_segments(df)
    plot_rfm_scatter(df)

    print("Plots saved to outputs/plots/")

if __name__ == "__main__":
    main()
