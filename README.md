# Customer Segmentation Using RFM and K-Means
This project performs customer segmentation using the Recency, Frequency, Monetary (RFM) analytical model combined with K-Means clustering. It classifies customers based on their purchasing behavior and identifies actionable business groups for targeted interventions. In addition to traditional RFM segmentation, unsupervised clustering is used to uncover deeper customer patterns.

## Customer segmentation helps organizations:
- Identify high-value and loyal customers
- Reduce churn by identifying at-risk customers
- Personalize marketing communication
- Improve customer retention strategies
- Prioritize resource allocation
- Understand revenue contribution by each customer group

## Project Structure
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/
│       ├── cleaned_data.csv
│       ├── rfm_segments.csv
│       └── kmeans_segments.csv
│
├── outputs/
│   ├── plots/
│   │   ├── recency_distribution.png
│   │   ├── frequency_distribution.png
│   │   ├── monetary_distribution.png
│   │   ├── segment_count.png
│   │   ├── frequency_vs_monetary_scatter.png
│   │   ├── kmeans_recency_monetary.png
│   │   ├── kmeans_frequency_monetary.png
│   │   └── kmeans_elbow.png
│   └── rfm_summary.md
│
├── src/
│   ├── prep_data.py
│   ├── rfm_segment.py
│   ├── generate_insights.py
│   ├── visualize_rfm.py
│   └── kmeans_segmentation.py
│
├── requirements.txt
└── README.md

## Getting Started
## Prerequisites
- Ensure you have the following installed: Python 3.10 or higher
The packages listed in requirements.txt including:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Installation
Clone the repository: git clone https://github.com/<sdlk4>/Customer-Segmentation-RFM-Analysis.git
cd Customer-Segmentation-RFM-Analysis

## Install dependencies:
- pip install -r requirements.txt
Run the processing and segmentation scripts:
- python src/prep_data.py
- python src/rfm_segment.py
- python src/generate_insights.py
- python src/visualize_rfm.py
- python src/kmeans_segmentation.py

## How the Project Works
## Data Cleaning (prep_data.py)
- Loads raw dataset containing transaction logs
- Removes missing customer IDs
- Removes negative quantities
- Converts InvoiceDate to datetime
- Creates TotalAmount column as Quantity multiplied by UnitPrice
- Saves cleaned structured dataset
## RFM Calculation and Segmentation (rfm_segment.py)
- Computes Recency as days since last purchase
- Computes Frequency as number of invoices
- Computes Monetary as total amount spent
- Assigns R, F, M scores using quintiles
- Combines scores into RFM_Score
## Classifies customers into segments such as:
- Champions
- Loyal Customers
- Big Spenders
- New Customers
- Promising
- At Risk
- Hibernating
## Business Insights Generation (generate_insights.py)
- Loads segmented RFM output
- Generates summary of customer distribution
- Computes revenue by segment
- Produces text-based analytic report stored in outputs directory
## Visualizations (visualize_rfm.py)
Produces plots for:
- Recency distribution
- Frequency distribution
- Monetary distribution
- Segment count comparison
- Frequency vs Monetary scatter colored by segment

These visualizations help understand customer behavior distributions.
- K-Means Clustering (kmeans_segmentation.py)
- Scales Recency, Frequency, and Monetary features
- Applies the Elbow method to determine optimal number of clusters
- Fits K-Means model
- Assigns cluster labels to customers

Generates cluster scatter plots for:
- Recency vs Monetary
- Frequency vs Monetary
- Saves clustered dataset

## Key Features
- Complete end-to-end RFM segmentation pipeline
- Business segment labeling for actionable insights
- K-Means clustering for unsupervised segmentation
- Multiple visualizations for behavioral understanding
- Insights summary file generated automatically
- Clean modular code structure

## Sample Outputs
The repository includes the following outputs:
- Recency distribution chart
- Frequency distribution chart
- Monetary distribution chart
- Customer segment count plot
- Frequency vs Monetary scatter colored by segment
- K-Means elbow method plot
- K-Means cluster scatter plots
Plots are stored inside the outputs/plots directory.

## Data Requirements
The input dataset must contain:
- InvoiceDate column representing transaction date
- CustomerID
- Quantity of items purchased
- UnitPrice of items
- InvoiceNo

Example: InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
536365,85123A,DECORATIVE... ,6,2010-12-01 08:26:00,2.55,17850,United Kingdom

## Contributing
Contributions are welcome. You may:
- Fork the repository
- Add new segmentation methods
- Improve visualization quality
- Enhance results interpretation
- Submit pull requests

## Technical Notes
- RFM captures customer behavior using three financial dimensions
- Quintile-based scoring ensures relative comparison across customers
- K-Means clustering supplements RFM by identifying statistical clusters
- Scaling is necessary for K-Means to handle variable magnitude
- Elbow method helps determine optimal K
- Visualizations help interpret segmentation results