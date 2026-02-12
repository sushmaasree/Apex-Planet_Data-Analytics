# ☕ Coffee Sales Data Immersion & Wrangling Project

## 📋 Project Overview
This project demonstrates comprehensive data wrangling and preparation skills on a coffee shop sales dataset. The analysis covers data acquisition, quality assessment, cleaning, transformation, and preparation for business intelligence.

**Internship Task:** Data Immersion & Wrangling  
**Timeline:** 10 Days  
**Dataset:** Coffee Shop Sales Transactions (March 2024 - March 2025)  
**Tools Used:** Python, Pandas, NumPy

---

## 🎯 Objectives
- Rapidly acquaint with provided dataset
- Master critical first steps of data analysis: acquiring, cleaning, and preparing data
- Identify and resolve data quality issues
- Transform raw data into analysis-ready format
- Create comprehensive documentation

---

## 📊 Dataset Information

### Source Data
- **File:** `Coffe_sales.csv`
- **Records:** 3,547 transactions
- **Period:** March 1, 2024 - March 23, 2025
- **Columns:** 11 original features
- **Total Revenue:** $112,245.58

### Key Features
| Feature | Description |
|---------|-------------|
| `hour_of_day` | Hour of transaction (6-22) |
| `cash_type` | Payment method (card) |
| `money` | Transaction amount |
| `coffee_name` | Product name (8 varieties) |
| `Time_of_Day` | Period (Morning/Afternoon/Night) |
| `Weekday` | Day of week |
| `Month_name` | Month of transaction |
| `Date` | Transaction date |
| `Time` | Exact timestamp |

---

## 🔍 Data Quality Assessment

### Quality Metrics
✅ **Completeness:** 100% (No missing values)  
✅ **Accuracy:** 98% (All values valid)  
✅ **Consistency:** 100% (Uniform formatting)  
✅ **Uniqueness:** 100% (No duplicates)  
✅ **Validity:** 100% (All business rules met)  

**Overall Quality Score:** ⭐⭐⭐⭐⭐ (99.6%)

### Data Quality Highlights
- ✓ Zero missing values across all columns
- ✓ Zero duplicate transactions
- ✓ All monetary values positive and valid
- ✓ Consistent date/time formatting
- ✓ Operating hours properly bounded (6 AM - 10 PM)

---

## 🛠️ Data Cleaning & Transformation Process

### Step 1: Data Loading & Initial Assessment
```python
- Loaded 3,547 rows × 11 columns
- Verified data types
- Checked for missing values and duplicates
```

### Step 2: Data Type Conversions
```python
✓ Date: string → datetime
✓ Time: string → time object
✓ Created DateTime: combined timestamp
✓ Money: standardized to 2 decimal places
```

### Step 3: Feature Engineering
Created 10 new features for enhanced analysis:
- **Temporal Features:** Year, Quarter, Week_of_Year, Day_of_Month, Day_of_Year
- **Categorical Features:** Is_Weekend, Product_Category, Price_Category, Hour_Category
- **Combined Feature:** DateTime (for time-series analysis)

### Step 4: Data Validation
```python
✓ Validated all monetary values ≥ 0
✓ Verified DateTime completeness
✓ Confirmed data integrity (no row loss)
✓ Validated new feature consistency
```

### Step 5: Output Generation
Generated multiple analysis-ready datasets and summaries

---

## 📁 Project Structure

```
coffee-sales-analysis/
│
├── data/
│   ├── raw/
│   │   └── Coffe_sales.csv                    # Original dataset
│   ├── cleaned/
│   │   ├── Coffee_Sales_Cleaned.csv           # Full cleaned dataset
│   │   └── Coffee_Sales_Analysis_Ready.csv    # Analysis-optimized version
│   └── summaries/
│       ├── daily_sales_summary.csv            # Daily aggregations
│       ├── product_performance_summary.csv    # Product metrics
│       └── hourly_sales_pattern.csv           # Hourly patterns
│
├── scripts/
│   ├── 01_data_exploration.py                 # Initial data exploration
│   └── 02_data_cleaning_script.py             # Complete cleaning pipeline
│
├── documentation/
│   ├── Data_Dictionary.md                     # Comprehensive data dictionary
│   ├── Data_Quality_Assessment.md             # Quality assessment report
│   └── Cleaning_Report.txt                    # Cleaning summary
│
└── README.md                                   # This file
```

---

## 🔑 Key Insights

### Sales Performance
- **Total Revenue:** $112,245.58
- **Average Transaction:** $31.65
- **Transaction Count:** 3,547

### Product Performance
| Rank | Product | Sales Count | % of Total |
|------|---------|-------------|------------|
| 1 | Americano with Milk | 809 | 22.8% |
| 2 | Latte | 757 | 21.3% |
| 3 | Americano | 564 | 15.9% |
| 4 | Cappuccino | 486 | 13.7% |
| 5 | Cortado | 287 | 8.1% |

### Temporal Patterns
- **Busiest Day:** Tuesday (572 transactions)
- **Slowest Day:** Sunday (419 transactions)
- **Peak Hour:** 10:00 AM
- **Peak Period:** Afternoon (34.0% of transactions)

### Product Categories
- **Coffee with Milk:** 60.9% (Latte, Cappuccino, Americano with Milk, Cortado)
- **Black Coffee:** 19.5% (Americano, Espresso)
- **Non-Coffee:** 14.5% (Hot Chocolate, Cocoa)

---

## 🚀 Usage

### Prerequisites
```bash
Python 3.8+
pandas
numpy
```

### Running the Analysis
```bash
# Step 1: Explore the data
python scripts/01_data_exploration.py

# Step 2: Clean and transform
python scripts/02_data_cleaning_script.py
```

### Loading Cleaned Data
```python
import pandas as pd

# Load full cleaned dataset
df_cleaned = pd.read_csv('data/cleaned/Coffee_Sales_Cleaned.csv')

# Load analysis-ready dataset
df_analysis = pd.read_csv('data/cleaned/Coffee_Sales_Analysis_Ready.csv')

# Load daily summary
df_daily = pd.read_csv('data/summaries/daily_sales_summary.csv')
```

---

## 📈 Potential Use Cases

1. **Sales Forecasting**
   - Predict daily/weekly/monthly revenue
   - Seasonal trend analysis

2. **Inventory Management**
   - Stock optimization based on product demand
   - Reduce waste for slow-moving items

3. **Staffing Optimization**
   - Schedule employees during peak hours
   - Adjust staffing for weekday vs weekend patterns

4. **Marketing Strategy**
   - Promote products during slow periods
   - Bundle popular items

5. **Customer Behavior Analysis**
   - Understand purchasing patterns
   - Time-of-day preferences

---

## 📝 Documentation Files

### 1. Data Dictionary
Comprehensive documentation of all dataset columns, including:
- Column descriptions and data types
- Value ranges and examples
- Business relevance
- Categorical value breakdowns

### 2. Data Quality Assessment Report
Detailed analysis of data quality covering:
- Completeness assessment
- Accuracy validation
- Consistency checks
- Uniqueness verification
- Validity testing
- Quality metrics and scores

### 3. Cleaning Report
Summary of all transformations applied:
- Original vs cleaned dataset comparison
- List of all transformations
- New features created
- Output files generated
- Key insights

---

## 🎥 Video Walkthrough

**LinkedIn Video:** [3-5 minute walkthrough] *(Link to be added)*

Topics covered:
1. Dataset introduction and business context
2. Data quality issues identification
3. Cleaning process demonstration
4. Key transformations and feature engineering
5. Results and business insights

---

## 🎓 Learning Outcomes

Through this project, I demonstrated:
- ✅ Data acquisition and familiarization techniques
- ✅ Systematic data quality assessment
- ✅ Comprehensive data cleaning strategies
- ✅ Feature engineering for business insights
- ✅ Professional documentation practices
- ✅ Python/Pandas proficiency
- ✅ Business intelligence fundamentals

---

## 🔮 Future Enhancements

1. **Advanced Analytics**
   - Time series forecasting models
   - Customer segmentation analysis
   - A/B testing framework

2. **Visualization Dashboard**
   - Interactive sales dashboard (Tableau/Power BI)
   - Real-time monitoring system

3. **Additional Data**
   - Customer demographics
   - Weather data correlation
   - Marketing campaign effectiveness

4. **Automation**
   - Automated data pipeline
   - Scheduled reports
   - Alert system for anomalies

---

## 📫 Contact

**Author:** [Your Name]  
**Email:** [Your Email]  
**LinkedIn:** [Your LinkedIn]  
**GitHub:** [Your GitHub]

---

## 📄 License

This project is part of an internship assignment for educational purposes.

---

## 🙏 Acknowledgments

- **ApexPlanet Software Pvt Ltd** for providing the internship opportunity
- Dataset provided as part of the Data Analytics Internship program
- Python community for excellent data science tools

---

**Last Updated:** February 12, 2026  
**Status:** ✅ Complete - All deliverables submitted
