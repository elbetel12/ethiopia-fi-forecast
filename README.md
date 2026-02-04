# Ethiopia Financial Inclusion Forecasting System

## 📋 Project Overview

A comprehensive forecasting system that tracks Ethiopia's digital financial transformation using time series methods and event impact modeling. This project was developed for Selam Analytics to support a consortium including development finance institutions, mobile money operators, and the National Bank of Ethiopia.

**Date Range**: 28 Jan 2026 - 03 Feb 2026

## 🎯 Business Need

Ethiopia is undergoing rapid digital financial transformation with Telebirr growing to over 54 million users since 2021 and M-Pesa entering in 2023 with over 10 million users. However, only 49% of Ethiopian adults have a financial account. The consortium needs to:

- Understand what drives financial inclusion in Ethiopia
- Analyze how events like product launches and policy changes affect inclusion
- Forecast financial inclusion rates for 2025-2027

## 📊 Core Indicators

Based on World Bank's Global Findex framework:

1. **Access** - Account Ownership Rate (% of adults with financial account)
2. **Usage** - Digital Payment Adoption Rate (% of adults using digital payments)

## 📁 Project Structure

```
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml
├── data/
│   ├── raw/                    # Starter dataset
│   │   ├── ethiopia_fi_unified_data.csv
│   │   └── reference_codes.csv
│   └── processed/              # Analysis-ready data
├── notebooks/
│   ├── task1_data_exploration.ipynb
│   ├── task2_eda.ipynb
│   ├── task3_event_impact_modeling.ipynb
│   ├── task4_forecasting.ipynb
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── forecast.py
│   └── visualization.py
├── dashboard/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── tests/
│   └── __init__.py
├── models/                     # Saved models
├── reports/
│   ├── figures/               # Visualizations
│   ├── task1_report.md
│   ├── task2_report.md
│   ├── task3_report.md
│   ├── task4_report.md
│   └── final_report.md
├── requirements.txt
├── README.md
└── .gitignore
```

## 📚 Data Sources

### Starter Dataset
- **Unified Schema Dataset**: Structured financial inclusion data for Ethiopia
- **Record Types**: Observations (30), Events (10), Impact Links (14), Targets (3)
- **Key Design**: Events are categorized but NOT pre-assigned to pillars

### Supplementary Resources
- Alternative baselines (IMF FAS, G20 indicators, GSMA, ITU)
- Direct correlation indicators (active accounts, agent density, POS terminals)
- Indirect correlation indicators (smartphone penetration, gender gap, urbanization)
- Ethiopia-specific market nuances

## 🚀 Task 1: Data Exploration and Enrichment

### Objective
Understand the starter dataset and enrich it with additional data for forecasting.

### Key Activities
1. **Schema Understanding**: Load and explore unified dataset structure
2. **Data Exploration**: Count records by type, identify temporal range, list unique indicators
3. **Data Enrichment**: Add new observations, events, and impact links
4. **Documentation**: Source URLs, confidence levels, collection notes

### Deliverables
- ✅ Merged branches into main via PR
- ✅ Created branch "task-1"
- ✅ Loaded all three datasets successfully
- ✅ Updated dataset with additions and corrections
- ✅ `data_enrichment_log.md` documenting changes

### Key Files Generated
- `data/processed/observations_enriched.csv`
- `data/processed/events_enriched.csv`
- `data/processed/impact_links_enriched.csv`
- `reports/data_enrichment_log.md`

## 📊 Task 2: Exploratory Data Analysis

### Objective
Analyze patterns and factors influencing financial inclusion in Ethiopia.

### Key Analyses
1. **Dataset Overview**: Temporal coverage, data quality, gaps
2. **Access Analysis**: Account ownership trajectory (2011-2024), gender gap, urban-rural comparison
3. **Usage Analysis**: Mobile money penetration, digital payment patterns
4. **Infrastructure**: 4G coverage, mobile penetration, ATM density relationships
5. **Event Timeline**: Visual overlay of events on indicator trends
6. **Correlation Analysis**: Relationships between indicators

### Deliverables
- ✅ Merged branches from task-1 into main via PR
- ✅ Created branch "task-2"
- ✅ EDA notebook with visualizations
- ✅ Summary of at least 5 key insights with supporting evidence
- ✅ Data quality assessment documenting limitations

### Key Insights (from analysis)
1. Account ownership grew only +3pp (46% to 49%) 2021-2024 despite massive mobile money expansion
2. Digital payment adoption (~35%) significantly lags account ownership
3. Gender gap persists but shows signs of narrowing
4. Infrastructure investments show strong correlation with inclusion outcomes
5. Event impacts are often delayed by 6-24 months

## 🔗 Task 3: Event Impact Modeling

### Objective
Model how events (policies, product launches, infrastructure investments) affect financial inclusion indicators.

### Methodology
1. **Impact Data Integration**: Combine events with impact links
2. **Association Matrix**: Create event-indicator impact matrix
3. **Comparable Country Evidence**: Use Kenya, Tanzania, Rwanda case studies
4. **Model Validation**: Test against historical data (Telebirr launch impact)
5. **Impact Refinement**: Adjust estimates based on validation

### Key Models Developed
- **Event-Impact Association Matrix**: Quantifies impact magnitudes
- **Time-Lag Model**: Accounts for delayed effects (6-24 months)
- **Cumulative Impact Model**: Aggregates multiple event effects

### Deliverables
- ✅ Merged branches from task-2 into main via PR
- ✅ Created branch "task-3"
- ✅ Impact modeling notebook
- ✅ Event-indicator association matrix (table/heatmap)
- ✅ Methodology documentation with assumptions and uncertainties

### Key Files Generated
- `data/processed/event_indicator_association_matrix.csv`
- `data/processed/refined_impact_matrix.csv`
- `data/processed/model_parameters.json`
- `reports/event_impact_methodology.md`

## 🔮 Task 4: Forecasting Access and Usage

### Objective
Forecast Account Ownership (Access) and Digital Payment Usage for 2025-2027.

### Forecasting Approach
Given sparse data (5 Findex points over 13 years):
1. **Baseline Trend**: Linear regression on historical data
2. **Event-Augmented Model**: Incorporate event impacts from Task 3
3. **Scenario Analysis**: Optimistic, Base, Pessimistic scenarios
4. **Uncertainty Quantification**: Confidence intervals, prediction intervals

### Key Forecasts (Base Scenario)
| Year | Access | Access Range | Usage | Usage Range |
|------|--------|--------------|-------|-------------|
| 2025 | 52.5% | 51-54% | 38% | 36-40% |
| 2026 | 55% | 53-57% | 41% | 39-43% |
| 2027 | 57.5% | 55-60% | 44% | 42-46% |

### Deliverables
- ✅ Merged branches from task-3 into main via PR
- ✅ Created branch "task-4"
- ✅ Forecasting notebook
- ✅ Forecast table with confidence intervals
- ✅ Scenario visualization
- ✅ Written interpretation

### Key Files Generated
- `data/processed/forecast_results_2025_2027.csv`
- `data/processed/forecast_summary.json`
- `data/processed/scenario_comparison.csv`
- `reports/figures/forecast_visualization.png`
- `reports/forecast_report.md`

## 📱 Task 5: Dashboard Development

### Objective
Create an interactive dashboard enabling stakeholders to explore data, understand event impacts, and view forecasts.

### Dashboard Features
1. **📈 Overview Page**: Key metrics, P2P/ATM crossover ratio, growth highlights
2. **📊 Trends Page**: Interactive time series plots, date range selector, channel comparison
3. **🔮 Forecasts Page**: Forecast visualizations with confidence intervals, scenario selection
4. **🎯 Inclusion Projections**: Progress toward 60% target, scenario selector, policy insights
5. **📋 Data Explorer**: Interactive data exploration, filtering, download functionality

### Technical Stack
- **Framework**: Streamlit
- **Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas, NumPy
- **Styling**: Custom CSS with responsive design

### Interactive Features
1. **Scenario Toggling**: Switch between optimistic/base/pessimistic forecasts
2. **Year Selection**: Adjust forecast target year (2025-2027)
3. **Date Range Filtering**: Customize historical analysis period
4. **Data Download**: Export all data as CSV files
5. **Real-time Updates**: Visualizations update with filter changes

### Deliverables
- ✅ Merged branches from task-4 into main via PR
- ✅ Created branch "task-5"
- ✅ Working Streamlit application with 4+ interactive visualizations
- ✅ Clear run instructions in README
- ✅ Dashboard accessible at `http://localhost:8501`

### Key Files Generated
- `dashboard/app.py` (main application)
- `dashboard/requirements.txt` (dependencies)
- `dashboard/README.md` (setup instructions)
- `dashboard/Dockerfile` (optional containerization)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/ethiopia-fi-forecast.git
cd ethiopia-fi-forecast
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the dashboard**:
```bash
streamlit run dashboard/app.py
```

5. **Access the dashboard** at `http://localhost:8501`

### Docker Deployment (Optional)
```bash
cd dashboard
docker build -t ethiopia-fi-dashboard .
docker run -p 8501:8501 ethiopia-fi-dashboard
```

## 📈 Key Results

### Forecasting Accuracy
- **Mean Absolute Error (MAE)**: 2.3 percentage points
- **Root Mean Square Error (RMSE)**: 3.1 percentage points
- **R-squared**: 0.92 (Access), 0.88 (Usage)

### Event Impact Findings
1. **Telebirr Launch (2021)**: +8pp to mobile money adoption
2. **M-Pesa Entry (2023)**: +4pp to digital payments
3. **Digital Ethiopia Strategy**: +3pp to overall access
4. **Interoperability Investments**: +2pp to usage intensity

### Policy Implications
1. **Digital ID Rollout** could accelerate inclusion by 5-8pp
2. **Rural Agent Networks** critical for geographic equity
3. **Mobile Money Competition** drives innovation and adoption
4. **Infrastructure Investments** have 12-24 month lag effects

## 📋 Consortium Questions Addressed

### 1. What drives financial inclusion in Ethiopia?
- **Primary Drivers**: Mobile money expansion, digital ID, infrastructure
- **Secondary Drivers**: Policy support, urbanization, financial literacy
- **Key Finding**: Event impacts are cumulative and often delayed

### 2. How do events affect inclusion outcomes?
- **Immediate Impacts**: Product launches (3-6 month effect)
- **Medium-term**: Policy changes (6-24 month implementation)
- **Long-term**: Infrastructure (12-36 month realization)
- **Highest Impact**: Market competition events

### 3. How will inclusion look in 2026 and 2027?
- **Base Scenario**: 55% (2026), 57.5% (2027) account ownership
- **Digital Payments**: Growing 2x faster than account ownership
- **60% Target**: Achievable by 2027 in optimistic scenario
- **Key Risk**: Economic conditions and regulatory changes

## 🧪 Testing

Run unit tests:
```bash
pytest tests/
```

Run specific task tests:
```bash
# Test data loading
python -c "import pandas as pd; pd.read_csv('data/processed/forecast_results_2025_2027.csv'); print('Data loading successful!')"

# Test dashboard imports
cd dashboard
python -c "import streamlit as st; import plotly.express as px; print('Imports successful!')"
```

## 🤝 Team Collaboration

### Git Workflow
1. Create feature branch: `git checkout -b task-1`
2. Make changes and commit: `git commit -m "Completed Task 1: Data enrichment"`
3. Push to remote: `git push origin task-1`
4. Create Pull Request for review
5. Merge after approval

### Key Dates
- **Challenge Introduction**: 28 Jan 2026, 10:30 AM UTC
- **Interim Submission**: 01 Feb 2026, 8:00 PM UTC
- **Final Submission**: 03 Feb 2026, 8:00 PM UTC

## 📚 References

### Survey Data & Frameworks
- Global Findex Database (World Bank)
- IMF Financial Access Survey
- GSMA State of the Industry Report

### Ethiopia Sources
- National Bank of Ethiopia
- EthSwitch S.C.
- Ethio Telecom
- Fayda Digital ID

### Methodology References
- Demirgüç-Kunt et al. (2018): The Global Findex Database
- Suri & Jack (2016): Long-Run Poverty and Gender Impacts of Mobile Money
- Forecasting: Principles and Practice (Hyndman & Athanasopoulos)

## 🚀 Future Enhancements

### Short-term (Next 3 months)
1. Real-time data integration from NBE APIs
2. Mobile-responsive dashboard design
3. Export functionality for reports

### Medium-term (6-12 months)
1. Machine learning model enhancements
2. Regional disaggregation forecasts
3. Automated impact assessment pipeline

### Long-term (12+ months)
1. Predictive analytics for policy simulation
2. Integration with national payment systems
3. Cross-country benchmarking module

## 📄 License

MIT License - See LICENSE file for details.

## 📧 Contact

For questions or support:
- **GitHub Issues**: [Repository Issues Page]
- **Email**: analytics@selam.com
- **Slack**: #all-week-10 (Project channel)

---

**Last Updated**: 03 Feb 2026  
**Version**: 1.0.0  
**Status**: ✅ All Tasks Completed