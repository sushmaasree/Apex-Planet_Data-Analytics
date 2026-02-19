# ☕ Coffee Sales EDA & Business Intelligence

## Project Overview
Exploratory Data Analysis of coffee shop sales data to uncover patterns, trends, and relationships that drive business performance. This analysis provides actionable insights for operations, marketing, and strategic planning.

**Task:** Exploratory Data Analysis & Business Intelligence  
**Timeline:** 14 Days  
**Dataset:** 3,547 coffee transactions (March 2024 - March 2025)  
**Tools:** Python, Pandas, Matplotlib, Seaborn, SQL

---

## Objectives
- Calculate key summary statistics for numerical and categorical variables
- Create visualizations to understand data distributions
- Write SQL queries to answer specific business questions
- Explore relationships between variables using correlation and multivariate analysis
- Provide actionable business intelligence insights

---

## Key Findings

### Revenue Metrics
- **Total Revenue:** $112,245.58
- **Average Transaction:** $31.65
- **Peak Hour:** 10:00 AM
- **Best Day:** Tuesday ($18,168)

### Product Insights
- Top product: Americano with Milk (22.8% of sales)
- Coffee with Milk category: 66% of volume, 68% of revenue
- Premium products: 40% of transactions, 46% of revenue

### Business Opportunities
- Weekend revenue growth potential (current 25%, target 30-35%)
- Evening non-coffee items show 138% increase vs morning
- Off-peak hour promotion opportunities (6-8 AM, 20-22 PM)

---

## Deliverables

### 1. Analysis Scripts
- `01_descriptive_statistics_univariate.py` - Summary statistics and distributions
- `02_sql_business_queries.py` - 15 SQL queries for business questions
- `03_multivariate_correlation.py` - Relationship analysis and correlations

### 2. Visualizations (11 charts)
- Revenue distribution histogram
- Product sales bar charts
- Hourly and weekday patterns
- Correlation heatmaps
- Category-time analysis
- Advanced scatter plots
- Pair plots

### 3. Documentation
- **EDA_Report.md** - Comprehensive analysis report with insights
- **business_queries.sql** - SQL queries with results

---

## Project Structure

```
task2/
├── charts/                          # All visualizations
│   ├── 01_revenue_distribution.png
│   ├── 02_product_sales_bar.png
│   ├── 03_hourly_patterns.png
│   └── ... 
├── sql_queries/
│   └── business_queries.sql         # 15 business SQL queries
├── reports/
│   └── EDA_Report.md                # Comprehensive EDA report
└── scripts/
    ├── 01_descriptive_statistics_univariate.py
    ├── 02_sql_business_queries.py
    └── 03_multivariate_correlation.py
```

---

## Analysis Highlights

### Descriptive Statistics
- Analyzed revenue distributions, temporal patterns, and product performance
- Identified peak hours (10 AM), best days (Tuesday), and seasonal trends
- Discovered balanced time-of-day distribution (32-34% each period)

### SQL Business Intelligence
Answered 15 key business questions including:
- Top 5 products by revenue
- Monthly acquisition trends
- Peak revenue hours
- Weekend vs weekday comparison
- Product performance by time period

### Multivariate Analysis
- Created correlation matrices showing variable relationships
- Built heatmaps for hour-weekday and category-time patterns
- Generated scatter plots revealing product price-popularity dynamics
- Identified that Coffee-Milk products perform consistently across all periods

---

## Key Recommendations

### Immediate Actions
1. Implement off-peak hour promotions (6-8 AM, 8-10 PM)
2. Launch evening hot chocolate marketing campaign
3. Optimize staffing based on hourly transaction patterns

### Strategic Initiatives
1. Develop weekend-specific product bundles
2. Introduce loyalty program for premium products
3. Expand evening menu with non-coffee options
4. Test extended hours on high-performing weekdays

---

## Technical Details

**Data Quality:**
- 100% complete (no missing values)
- Zero duplicates
- All values validated

**Analysis Methods:**
- Descriptive statistics
- Univariate distributions
- Bivariate correlations
- Multivariate relationships
- Time series patterns

**Visualizations:**
- Histograms, bar charts, line plots
- Heatmaps, scatter plots, pair plots
- Statistical overlays (mean, median, trends)

---

## Usage

### Run Analysis
```bash
# Generate descriptive statistics and visualizations
python 01_descriptive_statistics_univariate.py

# Create SQL queries
python 02_sql_business_queries.py

# Perform multivariate analysis
python 03_multivariate_correlation.py
```

### View Results
- Charts: `task2/charts/`
- SQL queries: `task2/sql_queries/business_queries.sql`
- Full report: `task2/reports/EDA_Report.md`

---

## Conclusion

This EDA reveals a stable, high-performing coffee shop with clear opportunities for revenue optimization through strategic promotions, product positioning, and operational adjustments. The analysis provides actionable insights backed by data-driven evidence.

**Status:** Complete  
**Date:** February 12, 2026  
**Analyst:** Data Analytics Intern
