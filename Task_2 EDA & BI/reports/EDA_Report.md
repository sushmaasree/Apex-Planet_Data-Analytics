# EXPLORATORY DATA ANALYSIS (EDA) REPORT
## Coffee Sales Business Intelligence

**Project:** Task 2 - EDA & Business Intelligence  
**Date:** February 12, 2026  
**Analyst:** Data Analytics Intern  
**Dataset:** Coffee Sales (March 2024 - March 2025)

---

## Executive Summary

This EDA report presents comprehensive analysis of 3,547 coffee shop transactions spanning 13 months. The analysis uncovers key patterns, trends, and relationships that drive business performance, enabling data-driven decision making for operations, marketing, and strategic planning.

**Key Metrics:**
- Total Revenue: $112,245.58
- Average Transaction: $31.65
- Transaction Volume: 3,547 sales
- Product Range: 8 coffee varieties
- Operating Hours: 6 AM - 10 PM

---

## 1. DESCRIPTIVE STATISTICS

### 1.1 Revenue Analysis

| Metric | Value |
|--------|-------|
| Total Revenue | $112,245.58 |
| Average Transaction | $31.65 |
| Median Transaction | $32.82 |
| Standard Deviation | $4.88 |
| Min Transaction | $18.12 |
| Max Transaction | $38.70 |
| 25th Percentile | $27.92 |
| 75th Percentile | $35.76 |

**Insights:**
- Transaction amounts show low volatility (SD: $4.88)
- Average transaction slightly below median indicates left-skewed distribution
- Most transactions fall within $28-$36 range (IQR)

### 1.2 Temporal Patterns

**Operating Hours:**
- Opens: 6:00 AM
- Closes: 10:00 PM
- Peak Hour: 10:00 AM
- Average transaction hour: 2:12 PM

**Time Period Distribution:**
- Morning (6-11 AM): 33.3% of transactions ($35,929.20)
- Afternoon (12-17 PM): 34.0% of transactions ($38,130.04)
- Night (18-22 PM): 32.7% of transactions ($38,186.34)

**Key Finding:** Sales are remarkably balanced across all time periods, with slight afternoon preference.

---

## 2. PRODUCT PERFORMANCE

### 2.1 Product Rankings

| Rank | Product | Sales | % of Total | Revenue | Avg Price |
|------|---------|-------|------------|---------|-----------|
| 1 | Americano with Milk | 809 | 22.8% | $24,751.12 | $30.59 |
| 2 | Latte | 757 | 21.3% | $26,875.30 | $35.51 |
| 3 | Americano | 564 | 15.9% | $14,650.26 | $25.98 |
| 4 | Cappuccino | 486 | 13.7% | $17,439.14 | $35.88 |
| 5 | Cortado | 287 | 8.1% | $7,384.86 | $25.73 |
| 6 | Hot Chocolate | 276 | 7.8% | $9,933.46 | $35.99 |
| 7 | Cocoa | 239 | 6.7% | $8,521.16 | $35.65 |
| 8 | Espresso | 129 | 3.6% | $2,690.28 | $20.86 |

### 2.2 Product Category Analysis

**Coffee with Milk (65.9% of sales):**
- Products: Latte, Cappuccino, Americano with Milk, Cortado
- Revenue: $76,450.42 (68.1% of total)
- Insight: Core business driver, highest margin category

**Black Coffee (19.5% of sales):**
- Products: Americano, Espresso
- Revenue: $17,340.54 (15.4% of total)
- Insight: Lower volume but consistent demand

**Non-Coffee (14.5% of sales):**
- Products: Hot Chocolate, Cocoa
- Revenue: $18,454.62 (16.4% of total)
- Insight: Higher price point, strong evening sales

### 2.3 Price Categories

| Category | Transactions | Revenue | % of Revenue |
|----------|--------------|---------|--------------|
| Premium ($35+) | 1,415 (39.9%) | $51,511.80 | 45.9% |
| Mid-Range ($30-35) | 930 (26.2%) | $29,810.14 | 26.6% |
| Standard (<$30) | 1,202 (33.9%) | $30,923.64 | 27.5% |

**Strategy Insight:** Premium products drive nearly half of revenue despite representing only 40% of transactions.

---

## 3. TEMPORAL TRENDS

### 3.1 Monthly Performance

**Top 3 Months:**
1. October: $13,891.16 (426 transactions)
2. February: $13,215.48 (423 transactions)
3. March: $15,891.64 (494 transactions)

**Bottom 3 Months:**
1. April: $5,719.56 (168 transactions)
2. January: $6,398.86 (201 transactions)
3. July: $6,915.94 (237 transactions)

**Seasonal Pattern:**
- Q1 2024: $35,505.98 (31.6% of revenue)
- Q2 2024: $21,501.74 (19.2% of revenue) - Lowest
- Q3 2024: $24,518.42 (21.8% of revenue)
- Q4 2024: $30,719.44 (27.4% of revenue)

### 3.2 Weekly Patterns

**Day of Week Performance:**

| Day | Transactions | Revenue | Avg Revenue/Day |
|-----|--------------|---------|------------------|
| Tuesday | 572 (16.1%) | $18,168.38 | $317.68 |
| Monday | 544 (15.3%) | $17,363.10 | $319.13 |
| Friday | 532 (15.0%) | $16,802.66 | $315.80 |
| Thursday | 510 (14.4%) | $16,091.40 | $315.52 |
| Wednesday | 500 (14.1%) | $15,750.46 | $315.01 |
| Saturday | 470 (13.3%) | $14,733.52 | $313.48 |
| Sunday | 419 (11.8%) | $13,336.06 | $318.28 |

**Weekend vs Weekday:**
- Weekday: 2,658 transactions (75.0%) - $84,176.00 revenue
- Weekend: 889 transactions (25.0%) - $28,069.58 revenue
- Insight: Weekdays dominate but weekend average transaction is comparable

### 3.3 Hourly Distribution

**Peak Hours (Top 5):**
1. 10 AM: 323 transactions
2. 16 PM: 298 transactions
3. 14 PM: 277 transactions
4. 11 AM: 276 transactions
5. 15 PM: 265 transactions

**Business Insight:** Clear morning and mid-afternoon peaks suggest optimal staffing times.

---

## 4. MULTIVARIATE ANALYSIS

### 4.1 Correlation Analysis

**Strong Positive Correlations:**
- Month vs Quarter: 0.974
- Month vs Week of Year: 0.959
- Quarter vs Week of Year: 0.943
- Weekday vs Weekend: 0.770

**Weak Correlations with Revenue:**
- Revenue vs Hour: 0.203 (slight positive)
- Revenue vs Weekend: -0.008 (negligible)
- Revenue vs Weekday: -0.042 (negligible)

**Key Finding:** Revenue is remarkably stable across different times and days, indicating consistent customer base.

### 4.2 Product-Time Relationships

**Morning Preferences (6-11 AM):**
1. Americano with Milk (26.4% of morning sales)
2. Latte (22.1%)
3. Americano (17.2%)

**Afternoon Preferences (12-17 PM):**
1. Americano with Milk (23.7%)
2. Latte (21.9%)
3. Americano (15.5%)

**Night Preferences (18-22 PM):**
1. Americano with Milk (21.4%)
2. Latte (19.5%)
3. Hot Chocolate (9.5%) - Notably higher than other periods

**Insight:** Non-coffee items (Hot Chocolate, Cocoa) see 49% increase in evening vs morning.

### 4.3 Category Performance by Time

| Category | Morning | Afternoon | Night | Best Period |
|----------|---------|-----------|-------|-------------|
| Coffee - Milk | $25,608.60 | $25,222.00 | $25,619.82 | Night (+0.04%) |
| Coffee - Black | $6,516.82 | $7,323.10 | $3,500.62 | Afternoon (+12.4%) |
| Non-Coffee | $3,803.78 | $5,584.94 | $9,065.90 | Night (+138%) |

**Strategic Opportunity:** Promote non-coffee items during evening hours for revenue optimization.

---

## 5. BUSINESS INTELLIGENCE INSIGHTS

### 5.1 Revenue Optimization Opportunities

**1. Product Mix Enhancement:**
- Premium products (40% of transactions) generate 46% of revenue
- Opportunity: Upsell strategies during peak hours
- Recommendation: Bundle premium drinks with pastries

**2. Time-Based Promotions:**
- Slow hours: 6-8 AM, 20-22 PM
- Strategy: Happy hour pricing or loyalty rewards during off-peak
- Potential uplift: 15-20% in identified hours

**3. Weekend Revenue Growth:**
- Current: 25% of weekly revenue
- Benchmark opportunity: 30-35%
- Actions: Weekend-specific promotions, extended hours

### 5.2 Operational Insights

**Staffing Recommendations:**
- **Peak hours (10-11 AM, 14-16 PM):** 3-4 staff members
- **Standard hours (12-13 PM, 17-19 PM):** 2-3 staff members
- **Low hours (6-9 AM, 20-22 PM):** 1-2 staff members

**Inventory Management:**
- High-volume items: Ensure 30% buffer stock for Americano with Milk, Latte
- Evening items: Increase Hot Chocolate, Cocoa inventory after 18:00
- Low-volume items: Reduce Espresso stock, consider promotion

### 5.3 Customer Behavior Patterns

**Consistency Indicators:**
- Low revenue volatility across days (SD: $4.88)
- Balanced time-of-day distribution (32-34% each period)
- Stable weekday performance (14-16% each day)

**Interpretation:** 
- Strong repeat customer base
- Predictable demand patterns
- Lower risk for inventory and staffing planning

---

## 6. KEY FINDINGS SUMMARY

### Revenue & Performance
✅ Total revenue: $112,245.58 across 3,547 transactions
✅ Consistent average transaction ($31.65) with low volatility
✅ Premium products drive 46% of revenue from 40% of sales

### Product Insights
✅ Coffee with Milk category dominates (66% of sales)
✅ Top 2 products (Americano with Milk, Latte) represent 44% of volume
✅ Non-coffee items perform best in evening (+138% vs morning)

### Temporal Patterns
✅ Tuesday is highest revenue day ($18,168)
✅ 10 AM is peak hour (323 transactions)
✅ Q1 strongest quarter (31.6% of annual revenue)

### Opportunities
✅ Weekend revenue growth potential (current 25%, target 30-35%)
✅ Off-peak hour promotions (6-8 AM, 20-22 PM)
✅ Evening non-coffee item marketing

---

## 7. RECOMMENDATIONS

### Immediate Actions (0-30 days)
1. Implement dynamic pricing for off-peak hours
2. Launch evening hot chocolate promotion campaign
3. Optimize staffing schedule based on hourly patterns
4. Create weekend-specific product bundles

### Short-term Initiatives (1-3 months)
1. Develop loyalty program focusing on premium products
2. Test extended hours on high-performing days (Tue, Mon, Fri)
3. Introduce seasonal drink variations for low-revenue months
4. Implement inventory forecasting system

### Long-term Strategy (3-12 months)
1. Expand product line in high-margin categories
2. Explore breakfast menu for morning revenue boost
3. Consider location analysis for multi-store expansion
4. Develop predictive analytics for demand forecasting

---

## 8. TECHNICAL APPENDIX

### Data Quality
- Zero missing values (100% completeness)
- Zero duplicates
- All monetary values validated
- Date ranges verified

### Analysis Methods
- Descriptive statistics (mean, median, std dev, percentiles)
- Univariate analysis (distributions, frequencies)
- Bivariate analysis (scatter plots, correlations)
- Multivariate analysis (heatmaps, cross-tabulations)
- Time series analysis (trends, seasonality)

### Visualizations Generated
1. Revenue distribution histogram
2. Product sales bar charts
3. Hourly sales patterns
4. Weekday revenue analysis
5. Time-of-day pie charts
6. Correlation heatmaps
7. Category-time heatmaps
8. Hour-weekday heatmaps
9. Advanced scatter plots
10. Pair plots

---

## 9. CONCLUSION

The coffee shop demonstrates strong, consistent performance with clear opportunities for revenue optimization. The analysis reveals:

1. **Stable Foundation:** Consistent demand patterns enable reliable forecasting
2. **Growth Potential:** Weekend and off-peak hours offer untapped revenue
3. **Product Strategy:** Premium products and evening non-coffee items are key growth drivers
4. **Operational Excellence:** Clear patterns enable optimized staffing and inventory

**Next Steps:** Implement recommended actions in priority order, monitor KPIs weekly, and iterate based on results.

---

**Report Prepared By:** Data Analytics Intern  
**Review Status:** Complete  
**Date:** February 12, 2026  
**Version:** 1.0
