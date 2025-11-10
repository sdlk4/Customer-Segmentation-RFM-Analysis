import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
INPUT = Path("data/processed/rfm_segments.csv")
OUTPUT = Path("data/processed/kmeans_segments.csv")
PLOT_DIR = Path("outputs/plots")

# --------------------------------------------------------
# Load RFM data
# --------------------------------------------------------
def load_data():
    print(f"Loading RFM data from: {INPUT}")
    df = pd.read_csv(INPUT)
    return df

# --------------------------------------------------------
# Elbow Method
# --------------------------------------------------------
def elbow_method(df):
    print("Running Elbow Method to determine optimal K...")

    # Standardizing features
    features = df[["Recency", "Frequency", "Monetary"]]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    wcss = []  # Within-cluster sum of squares
    K_range = range(2, 10)

    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled)
        wcss.append(kmeans.inertia_)

    # Plot elbow
    plt.figure(figsize=(10, 6))
    plt.plot(K_range, wcss, marker="o")
    plt.title("Elbow Method — Optimal K")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Within-Cluster Sum of Squares (WCSS)")
    plt.grid(True)

    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(PLOT_DIR / "kmeans_elbow.png")
    plt.close()

    print("Elbow plot saved to outputs/plots/kmeans_elbow.png")

# --------------------------------------------------------
# Apply KMeans clustering
# --------------------------------------------------------
def apply_kmeans(df, n_clusters=5):
    print(f"Applying KMeans with k={n_clusters}...")

    features = df[["Recency", "Frequency", "Monetary"]]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["KMeans_Cluster"] = kmeans.fit_predict(scaled)

    print("KMeans clustering applied. Sample:")
    print(df[["CustomerID", "Recency", "Frequency", "Monetary", "KMeans_Cluster"]].head())

    return df

# --------------------------------------------------------
# Plot clusters
# --------------------------------------------------------
def plot_clusters(df):
    print("Generating KMeans cluster plots...")

    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    # Recency vs Monetary
    plt.figure(figsize=(10, 7))
    sns.scatterplot(data=df, x="Recency", y="Monetary", hue="KMeans_Cluster", palette="tab10")
    plt.title("KMeans Clusters: Recency vs Monetary")
    plt.savefig(PLOT_DIR / "kmeans_recency_monetary.png")
    plt.close()

    # Frequency vs Monetary
    plt.figure(figsize=(10, 7))
    sns.scatterplot(data=df, x="Frequency", y="Monetary", hue="KMeans_Cluster", palette="tab10")
    plt.title("KMeans Clusters: Frequency vs Monetary")
    plt.savefig(PLOT_DIR / "kmeans_frequency_monetary.png")
    plt.close()

    print("Cluster plots saved to outputs/plots/")

# --------------------------------------------------------
# Save results
# --------------------------------------------------------
def save_clusters(df):
    df.to_csv(OUTPUT, index=False)
    print(f"KMeans segmentation saved to: {OUTPUT}")

# --------------------------------------------------------
# Main execution flow
# --------------------------------------------------------
def main():
    df = load_data()
    elbow_method(df)         # Step 1 — find optimal K visually
    df = apply_kmeans(df)    # Step 2 — apply KMeans clustering
    plot_clusters(df)        # Step 3 — cluster visualizations
    save_clusters(df)        # Step 4 — save output

    print("KMeans segmentation completed successfully!")

# --------------------------------------------------------
# Entry point
# --------------------------------------------------------
if __name__ == "__main__":
    main()
