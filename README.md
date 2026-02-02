# Ethiopia Financial Inclusion Forecasting System

## Project Overview
This project builds a forecasting system to track Ethiopia's digital financial transformation using time series methods. The system predicts financial inclusion metrics for 2025-2027 based on historical data, events, and policy impacts.

## Key Metrics
- **Access**: Account Ownership Rate (% of adults with financial accounts)
- **Usage**: Digital Payment Adoption Rate (% of adults using digital payments)

## Project Structure
ethiopia-fi-forecast/
├── data/ # Data directory
│ ├── raw/ # Raw data files
│ └── processed/ # Processed data files
├── notebooks/ # Jupyter notebooks for analysis
├── src/ # Source code modules
├── dashboard/ # Streamlit dashboard
├── tests/ # Unit tests
├── models/ # Trained models
└── reports/ # Reports and figures


## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ethiopia-fi-forecast
2.Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
pip install -r requirements.txt
4.Download data files from provided Google Sheets links and place in data/raw/
Dashboard
Run the interactive dashboard:
streamlit run dashboard/app.py