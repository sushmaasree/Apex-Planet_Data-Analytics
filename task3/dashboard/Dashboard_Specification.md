# INTERACTIVE DASHBOARD SPECIFICATION
## Coffee Sales Business Intelligence Platform

**Document Type:** Technical Specification & Implementation Guide  
**Version:** 1.0  
**Date:** February 19, 2026  
**Target Platform:** Tableau / Power BI / Looker Studio

---

## DASHBOARD OVERVIEW

### Purpose
Create an interactive, automated dashboard that surfaces core KPIs, enables deep-dive analysis exploration, and supports data-driven decision making for coffee shop operations.

### Primary Users
- **Executive View:** High-level KPIs and trends
- **Manager View:** Operational metrics and segment analysis
- **Analyst View:** Detailed drill-down and cohort analysis

### Update Frequency
- **Real-time (Ideal):** Live connection to transaction database
- **Daily:** End-of-day batch update
- **Current:** Manual refresh from CSV export

---

## DASHBOARD STRUCTURE

### Page 1: EXECUTIVE DASHBOARD (Overview)

**Purpose:** At-a-glance business health monitoring

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                   COFFEE SALES PERFORMANCE DASHBOARD                 │
│                      [Date Range Selector] [Refresh]                 │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────── KPI CARDS ────────────────────────────┐
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│ │   DAILY     │  │  AVG TRANS  │  │   WEEKLY    │  │  REVENUE │ │
│ │  REVENUE    │  │    VALUE    │  │    TRANS    │  │ CONSIST  │ │
│ │             │  │             │  │             │  │          │ │
│ │  $294.61    │  │   $31.65    │  │    2,060    │  │  69.6%   │ │
│ │  ▲ +8.2%    │  │  ▲ +3.1%    │  │   ▲ +12.3%  │  │  ▼ -2.1% │ │
│ └─────────────┘  └─────────────┘  └─────────────┘  └──────────┘ │
└──────────────────────────────────────────────────────────────────┘

┌────────────── REVENUE TREND ──────────────┬─── TOP PRODUCTS ────┐
│                                            │ 1. Americano w/Milk │
│  [Line Chart: Daily Revenue Over Time]    │    Sales: 809       │
│  - 30-day moving average                  │    Revenue: $24.7K  │
│  - Target line ($339/day)                 │                     │
│  - Color-coded: Above/Below target        │ 2. Latte            │
│                                            │    Sales: 757       │
│                                            │    Revenue: $26.9K  │
└────────────────────────────────────────────┴─────────────────────┘

┌─── HOURLY PATTERN ──────┬─── WEEKDAY PERFORMANCE ───┬── SEGMENTS ─┐
│                          │                            │             │
│ [Area Chart: Trans/Hour]│ [Bar Chart: Day Revenue]  │ [Pie Chart: │
│ - Peak hours highlighted│ - Weekend vs Weekday      │  Segment %] │
│ - Staffing zones shown  │ - YoY comparison          │             │
│                          │                            │             │
└──────────────────────────┴────────────────────────────┴─────────────┘
```

**Interactive Elements:**
- Date range picker (last 7/30/90 days, YTD, custom)
- KPI cards clickable → drill down to detail pages
- Hoverable tooltips on all charts
- Export to PDF/PowerPoint functionality

**Data Connections:**
```sql
-- KPI Cards
SELECT 
    SUM(money) / COUNT(DISTINCT Date) as daily_revenue_rate,
    AVG(money) as avg_transaction_value,
    COUNT(*) / COUNT(DISTINCT strftime('%Y-%W', Date)) as weekly_transactions,
    1 - (STDEV(money) / AVG(money)) as revenue_consistency
FROM coffee_sales
WHERE Date >= date('now', '-30 days');

-- Revenue Trend
SELECT 
    Date,
    SUM(money) as daily_revenue,
    COUNT(*) as transaction_count,
    AVG(money) as avg_transaction
FROM coffee_sales
GROUP BY Date
ORDER BY Date;
```

---

### Page 2: COHORT ANALYSIS DASHBOARD

**Purpose:** Track customer acquisition and retention patterns

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                         COHORT ANALYSIS DASHBOARD                    │
│              [Cohort Selector] [Metric Selector] [Filters]           │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────── COHORT RETENTION HEATMAP ──────────────────────────┐
│                                                                     │
│  Cohort    │  Month 0  │  Month 1  │  Month 2  │  Month 3  │ ...  │
│  ──────────┼───────────┼───────────┼───────────┼───────────┼───── │
│  2024-03   │   100%    │    0%     │    0%     │    0%     │      │
│  2024-04   │   100%    │    0%     │    0%     │    0%     │      │
│  2024-05   │   100%    │    0%     │    0%     │           │      │
│  ...       │           │           │           │           │      │
│                                                                     │
│  Color Scale: [Red → Yellow → Green] (0% → 50% → 100%)            │
└─────────────────────────────────────────────────────────────────────┘

┌─────── COHORT SIZE ─────────┬────── COHORT REVENUE TRENDS ─────────┐
│                              │                                       │
│ [Bar Chart: Initial Size]   │ [Line Chart: Revenue by Cohort]      │
│ - Sorted by acquisition date│ - Multiple cohorts overlaid          │
│ - Quarterly grouping option │ - Normalized to Month 0 = 100%       │
│                              │                                       │
└──────────────────────────────┴───────────────────────────────────────┘

┌────────────────── COHORT PERFORMANCE METRICS ─────────────────────┐
│                                                                     │
│  Best Cohort: 2024-10 ($13,891 initial revenue, 426 transactions) │
│  Worst Cohort: 2024-04 ($5,719 initial revenue, 168 transactions) │
│  Avg Q4 Cohort: 315 initial transactions (+12% vs Q1)             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Interactive Features:**
- Toggle between transaction count and revenue metrics
- Filter by cohort quarter/month
- Click cohort to isolate trend line
- Export cohort table to Excel

**Data Connections:**
```sql
-- Cohort Retention Matrix
WITH cohorts AS (
    SELECT 
        strftime('%Y-%m', Date) as cohort,
        strftime('%Y-%m', Date) as order_month,
        COUNT(*) as transactions,
        SUM(money) as revenue
    FROM coffee_sales
    GROUP BY cohort, order_month
)
SELECT 
    cohort,
    order_month,
    transactions,
    revenue,
    (julianday(order_month) - julianday(cohort)) / 30 as period
FROM cohorts
ORDER BY cohort, order_month;
```

---

### Page 3: CUSTOMER SEGMENTATION DASHBOARD

**Purpose:** Understand customer diversity and segment-specific behavior

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                    CUSTOMER SEGMENTATION DASHBOARD                   │
│         [Segment Selector] [Comparison Mode] [Date Range]            │
└─────────────────────────────────────────────────────────────────────┘

┌──────────── SEGMENT OVERVIEW ────────────────────────────────────┐
│                                                                    │
│  [4-Quadrant Scatter Plot]                                        │
│  X-Axis: Average Transaction Value                                │
│  Y-Axis: Transaction Frequency                                    │
│  Bubble Size: Total Revenue                                       │
│  Color: Segment (Morning Premium, Evening Standard, etc.)         │
│                                                                    │
│  Click bubble → Filter entire dashboard to segment                │
└────────────────────────────────────────────────────────────────────┘

┌─── SEGMENT DISTRIBUTION ───┬───────── SEGMENT DETAILS ────────────┐
│                             │                                       │
│ [Pie Chart: Trans %]       │ Segment: Morning Premium Buyers       │
│ [Pie Chart: Revenue %]     │ ───────────────────────────────────── │
│                             │ Size: 804 transactions (22.7%)       │
│ Side-by-side comparison    │ Revenue: $27,593 (24.6%)             │
│                             │ Avg Trans: $34.32                     │
│                             │ Peak Hour: 10:00 AM                   │
│                             │ Top Product: Latte                    │
│                             │                                       │
│                             │ [Product Mix Chart]                   │
│                             │ [Hourly Pattern Chart]                │
└─────────────────────────────┴───────────────────────────────────────┘

┌──────────────── SEGMENT PERFORMANCE COMPARISON ──────────────────┐
│                                                                    │
│  Metric          │ Seg 1 │ Seg 2 │ Seg 3 │ Seg 4 │ Overall      │
│  ────────────────┼───────┼───────┼───────┼───────┼───────────── │
│  Avg Trans ($)   │ 34.32 │ 34.44 │ 31.74 │ 25.46 │ 31.65        │
│  Peak Hour       │  10AM │  7PM  │  12PM │  11AM │  2PM         │
│  Weekend %       │  0%   │  0%   │ 100%  │  1%   │  25%         │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**Interactive Features:**
- Segment selector (dropdown or multi-select)
- Comparison mode (show 2-4 segments side-by-side)
- Dynamic filtering of all visuals by segment
- Drill-down to individual customer transactions

**Data Connections:**
```sql
-- Segment Performance
SELECT 
    ml_segment_name as segment,
    COUNT(*) as transaction_count,
    SUM(money) as total_revenue,
    AVG(money) as avg_transaction,
    AVG(hour_of_day) as avg_hour,
    SUM(CASE WHEN Is_Weekend = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as weekend_pct,
    (SELECT coffee_name 
     FROM coffee_sales s2 
     WHERE s2.ml_segment_name = s1.ml_segment_name 
     GROUP BY coffee_name 
     ORDER BY COUNT(*) DESC LIMIT 1) as top_product
FROM coffee_sales s1
GROUP BY segment;
```

---

### Page 4: PRODUCT PERFORMANCE DASHBOARD

**Purpose:** Monitor product mix, pricing, and category trends

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                    PRODUCT PERFORMANCE DASHBOARD                     │
│        [Product Filter] [Category Filter] [Time Comparison]          │
└─────────────────────────────────────────────────────────────────────┘

┌────── PRODUCT MIX EVOLUTION ─────────────────────────────────────┐
│                                                                    │
│  [Stacked Area Chart: Revenue % by Category Over Time]           │
│  - Coffee-Milk (68.1%)                                            │
│  - Non-Coffee (16.4%)                                             │
│  - Coffee-Black (15.4%)                                           │
│                                                                    │
│  Target Lines: 65% / 20% / 15%                                   │
└────────────────────────────────────────────────────────────────────┘

┌── TOP PRODUCTS ─────────┬──── CATEGORY PERFORMANCE ───────────────┐
│                          │                                          │
│ [Tree Map: Revenue Size]│ Category: Coffee - Milk                  │
│ - Size = Revenue        │ ────────────────────────────────────────│
│ - Color = Growth %      │ Revenue: $76,450 (68.1%)                │
│ - Label = Product Name  │ Units: 2,339 (65.9%)                    │
│                          │ Avg Price: $32.68                        │
│ Top 3 by Revenue:       │ Growth: +5.2% vs last period            │
│ 1. Latte - $26.9K       │                                          │
│ 2. Americano w/M $24.7K │ [Time of Day Preference Chart]          │
│ 3. Cappuccino - $17.4K  │ Morning: 33.5% | Afternoon: 33.0%       │
│                          │ Evening: 33.5% (Balanced!)               │
└──────────────────────────┴──────────────────────────────────────────┘

┌────────── PRICE SENSITIVITY ANALYSIS ────────────────────────────┐
│                                                                    │
│  [Scatter Plot: Price vs Volume]                                 │
│  - Each point = Product                                           │
│  - Bubble size = Revenue                                          │
│  - Shows price elasticity                                         │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**Interactive Features:**
- Product search and multi-select
- Category toggle (show/hide categories)
- Time comparison (MoM, QoQ, YoY)
- Price band highlighting

---

### Page 5: OPERATIONAL EXCELLENCE DASHBOARD

**Purpose:** Optimize staffing, capacity, and operational efficiency

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                  OPERATIONAL EXCELLENCE DASHBOARD                    │
│            [Day Selector] [Hour Range] [Staff View]                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────── HOURLY HEATMAP ───────────────────────────────────────┐
│                                                                    │
│  Day/Hour│ 6 │ 7 │ 8 │ 9 │10 │11 │12 │13 │14 │15 │16 │17 │18 ... │
│  ────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼────── │
│  Monday  │ 12│ 18│ 24│ 35│ 48│ 42│ 38│ 35│ 40│ 38│ 45│ 38│ 28 ...│
│  Tuesday │ 14│ 20│ 26│ 38│ 52│ 45│ 42│ 38│ 45│ 42│ 48│ 40│ 30 ...│
│  ...                                                               │
│                                                                    │
│  Color Scale: [White → Yellow → Red] (Low → Med → High Volume)   │
│  Overlay: Staffing zones (1-2 staff, 2-3 staff, 3-4 staff)       │
└────────────────────────────────────────────────────────────────────┘

┌─── CAPACITY UTILIZATION ───┬──── STAFFING OPTIMIZATION ───────────┐
│                             │                                       │
│ [Gauge Chart: Peak Hour %] │ Recommended Staffing:                 │
│ Current: 25.3%             │                                       │
│ Target: 24-28%             │ Peak Hours (10-11, 14-16): 3-4 staff │
│ Status: ✅ Optimal         │ Standard Hours: 2-3 staff             │
│                             │ Off-Peak Hours: 1-2 staff             │
│ [Bar: Off-Peak Opportunity]│                                       │
│ Current: 27.3% of trans    │ Efficiency Metrics:                   │
│ Target: 32.8% (+5.5pp)     │ Trans per Staff Hour: 14.2            │
│                             │ Revenue per Staff Hour: $450          │
└─────────────────────────────┴───────────────────────────────────────┘

┌───────────── DAILY PERFORMANCE TRACKER ──────────────────────────┐
│                                                                    │
│  Today's Performance:           | Yesterday:    | This Day Last Wk:│
│  Revenue: $315 (vs $295 target)| $289         | $301             │
│  Transactions: 11 (vs 10 target)| 9            | 10               │
│  Avg Trans: $28.64              | $32.11       | $30.10           │
│                                                                    │
│  [Real-time Transaction Feed - Last 10 transactions]              │
└────────────────────────────────────────────────────────────────────┘
```

---

## TECHNICAL SPECIFICATIONS

### Data Sources

**Primary Data Source:**
```
File: coffee_sales_cleaned.csv
Location: Cloud storage / Database
Update Frequency: Daily (batch) or Real-time (streaming)
```

**Required Fields:**
- DateTime, Date, Time
- money (transaction amount)
- coffee_name, Product_Category
- hour_of_day, Time_of_Day
- Weekday, Is_Weekend
- Quarter, Month_name
- ML_Segment_Name (from segmentation)

### Platform Recommendations

**Option 1: Tableau Public/Desktop**
- **Pros:** Best-in-class visualizations, easy drag-and-drop
- **Cons:** Cost ($70/user/month Desktop, free Public with limitations)
- **Best For:** Professional presentations, executive dashboards

**Option 2: Power BI**
- **Pros:** Microsoft ecosystem integration, $10/user/month
- **Cons:** Steeper learning curve
- **Best For:** Organizations using Microsoft 365

**Option 3: Looker Studio (Google)**
- **Pros:** Free, cloud-based, easy sharing
- **Cons:** Less sophisticated visualizations
- **Best For:** Budget-conscious, quick deployment

### Data Refresh Strategy

**Real-Time (Ideal):**
```python
# Example: Python script with database connection
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:pass@host:5432/db')
df = pd.read_sql('SELECT * FROM coffee_sales', engine)
# Write to dashboard data source
```

**Scheduled Batch:**
```bash
# Cron job: Daily at midnight
0 0 * * * /path/to/update_dashboard.sh
```

### Interactivity Features

**Global Filters:**
- Date Range Picker (all pages)
- Product Category Multi-Select
- Segment Filter
- Day Type (Weekday/Weekend)

**Page-Specific Filters:**
- Cohort: Month selector
- Segment: ML segment selector
- Product: Product name search

**Actions:**
- Click KPI card → Navigate to detail page
- Click segment bubble → Filter all visuals
- Click product → Show product detail popup
- Hover any chart → Show detailed tooltip

---

## IMPLEMENTATION GUIDE

### Phase 1: Data Preparation (Days 1-2)

**Tasks:**
1. Clean and validate coffee_sales dataset
2. Create calculated fields:
   - Daily Revenue Run Rate
   - Cohort assignments
   - Segment classifications
3. Generate aggregated tables:
   - Daily summary table
   - Product performance table
   - Cohort matrix table
   - Segment summary table

**Deliverable:** `dashboard_data_final.csv` with all required fields

### Phase 2: Dashboard Build (Days 3-7)

**Day 3-4: Executive Dashboard**
- Build KPI cards with conditional formatting
- Create revenue trend line chart
- Build hourly pattern area chart
- Add top products table

**Day 5: Cohort Dashboard**
- Create cohort retention heatmap
- Build cohort size bar chart
- Add cohort trend lines
- Implement cohort metrics cards

**Day 6: Segmentation Dashboard**
- Build segment scatter plot
- Create segment distribution pies
- Add segment comparison table
- Implement segment drill-down

**Day 7: Product & Operations Dashboards**
- Product mix evolution chart
- Tree map for products
- Hourly heatmap for operations
- Staffing optimization display

### Phase 3: Testing & Refinement (Days 8-10)

**Testing Checklist:**
- [ ] All filters work across pages
- [ ] Drill-down actions function correctly
- [ ] Tooltips display accurate information
- [ ] Export to PDF/Excel works
- [ ] Mobile responsiveness (if applicable)
- [ ] Performance (load time < 3 seconds)

**User Acceptance Testing:**
- Executive review: High-level KPIs clear
- Manager review: Actionable insights visible
- Analyst review: Drill-down depth sufficient

### Phase 4: Deployment & Training (Days 11-12)

**Deployment:**
1. Publish dashboard to Tableau Server / Power BI Service
2. Set up automated data refresh
3. Configure user access permissions
4. Create dashboard link/bookmark

**Training:**
- Executive: 30-minute walkthrough of Page 1
- Manager: 60-minute session on Pages 1-3
- Analyst: 90-minute deep dive on all pages
- Create user guide PDF with screenshots

---

## DASHBOARD LINK & ACCESS

**Live Dashboard URL:** [To be created - Tableau Public/Power BI]

**Example Implementation:**
```
https://public.tableau.com/app/profile/coffee.analytics/viz/CoffeeSalesDashboard
```

**Access Instructions:**
1. Navigate to dashboard URL
2. Select date range (default: last 30 days)
3. Explore KPIs on Executive Dashboard (Page 1)
4. Use navigation tabs to access deep-dive pages
5. Click any visualization to filter
6. Export reports using toolbar options

---

## MAINTENANCE & UPDATES

### Daily Maintenance
- Verify data refresh completed successfully
- Check for data quality issues (nulls, outliers)
- Monitor dashboard performance (load times)

### Weekly Reviews
- Review KPI trends vs targets
- Identify anomalies requiring investigation
- Update segment definitions if needed

### Monthly Updates
- Add new products to product master list
- Refresh ML segmentation model
- Update target benchmarks based on performance
- Review and optimize slow-loading visualizations

---

## SUCCESS METRICS

**Dashboard Adoption:**
- Target: 80% of managers use dashboard weekly
- Measure: Login tracking, page views

**Data-Driven Decisions:**
- Target: 3+ business decisions influenced by dashboard per month
- Measure: Decision log, feedback surveys

**Performance Impact:**
- Target: 10% revenue increase within 6 months
- Measure: KPI tracking, before/after analysis

---

**Document Prepared By:** Data Analytics Intern  
**Date:** February 19, 2026  
**Version:** 1.0  
**Next Review:** March 19, 2026
