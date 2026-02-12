# DATA DICTIONARY - COFFEE SALES DATASET

## Dataset Overview
- **Dataset Name:** Coffee Sales Transaction Data
- **Total Records:** 3,547 transactions
- **Date Range:** March 2024 - December 2024
- **Source:** Coffee shop sales system
- **Last Updated:** December 2024

---

## Column Descriptions

| Column Name    | Data Type | Description | Example Values | Business Relevance |
|---------------|-----------|-------------|----------------|-------------------|
| **hour_of_day** | Integer | Hour of transaction (24-hour format) | 6, 10, 14, 22 | Identifies peak hours for staffing and inventory planning |
| **cash_type** | String | Payment method used | "card" | Currently only card payments recorded; useful for payment processing analysis |
| **money** | Float | Transaction amount in local currency | 28.9, 33.8, 38.7 | Revenue tracking and pricing analysis |
| **coffee_name** | String | Name/type of coffee product sold | "Latte", "Americano", "Cappuccino" | Product popularity and inventory management |
| **Time_of_Day** | String | Period of day categorization | "Morning", "Afternoon", "Night" | Customer behavior patterns and marketing strategies |
| **Weekday** | String | Day of the week | "Mon", "Tue", "Wed", etc. | Weekly sales patterns and staffing optimization |
| **Month_name** | String | Month of transaction | "Jan", "Feb", "Mar", etc. | Seasonal trends and yearly performance |
| **Weekdaysort** | Integer | Numeric code for weekday sorting | 1-7 (1=Monday, 7=Sunday) | Database sorting and filtering operations |
| **Monthsort** | Integer | Numeric code for month sorting | 1-12 (1=January, 12=December) | Chronological analysis and reporting |
| **Date** | String | Transaction date | "2024-03-01" | Daily sales tracking and trend analysis |
| **Time** | String | Exact timestamp of transaction | "10:15:50.520000" | Precise transaction timing and customer flow analysis |

---

## Data Value Ranges

### Numerical Columns
- **hour_of_day:** Range 6-22 (6 AM to 10 PM operating hours)
- **money:** Range varies by product (see Product Pricing below)
- **Weekdaysort:** 1-7 (Monday to Sunday)
- **Monthsort:** 1-12 (January to December)

### Categorical Values

**coffee_name (8 unique products):**
1. Americano with Milk (809 sales - 22.8%)
2. Latte (757 sales - 21.3%)
3. Americano (564 sales - 15.9%)
4. Cappuccino (486 sales - 13.7%)
5. Cortado (287 sales - 8.1%)
6. Hot Chocolate (276 sales - 7.8%)
7. Cocoa (239 sales - 6.7%)
8. Espresso (129 sales - 3.6%)

**Time_of_Day (3 periods):**
- Morning: 1,181 transactions (33.3%)
- Afternoon: 1,205 transactions (34.0%)
- Night: 1,161 transactions (32.7%)

**Weekday (7 days):**
- Tuesday: 572 transactions (highest)
- Sunday: 419 transactions (lowest)

**Month_name (12 months):**
- March: 494 transactions (highest)
- January: 201 transactions (lowest)

**cash_type:**
- Card: 3,547 transactions (100%)

---

## Product Pricing Analysis
Based on observed transaction amounts:
- **Premium Products (~38.7):** Latte, Hot Chocolate, Cocoa
- **Mid-Range Products (~33.8):** Americano with Milk, Cappuccino
- **Standard Products (~28.9):** Americano, Cortado, Espresso

---

## Data Quality Notes

### Strengths:
✅ **Complete Dataset:** No missing values in any column
✅ **No Duplicates:** All 3,547 records are unique
✅ **Consistent Formatting:** All dates and times follow standard format
✅ **Valid Ranges:** All numerical values within expected ranges

### Observations:
⚠️ **Single Payment Method:** Only card payments recorded (no cash transactions)
⚠️ **Date/Time Format:** Currently stored as strings; recommend datetime conversion for analysis
⚠️ **Operating Hours:** Business operates 6 AM - 10 PM

### Recommendations for Analysis:
1. Convert Date and Time columns to datetime format
2. Create combined datetime column for time-series analysis
3. Extract additional features: quarter, week number, day of month
4. Analyze price points and product profitability
5. Identify peak hours and optimize staffing

---

## Business Use Cases

1. **Sales Forecasting:** Predict daily/weekly/monthly sales trends
2. **Inventory Management:** Stock planning based on product popularity
3. **Staffing Optimization:** Schedule staff based on peak hours/days
4. **Marketing Strategy:** Target promotions during slow periods
5. **Product Performance:** Identify bestsellers and underperformers
6. **Customer Behavior:** Understand purchasing patterns by time/day

---

**Document Version:** 1.0
**Created By:** Data Analytics Intern
**Date:** February 2026
**Contact:** [Your contact information]
