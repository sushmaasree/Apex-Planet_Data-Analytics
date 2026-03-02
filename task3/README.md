# ☕ Coffee Sales Deep-Dive Analysis & Dashboard

## Project Overview
Advanced analytics project performing deep-dive analysis on coffee sales data to answer complex business problems. Includes KPI framework, cohort analysis, customer segmentation, and interactive dashboard specification.

**Task:** Deep-Dive Analysis & Interactive Dashboarding  
**Timeline:** 12 Days  
**Dataset:** 3,547 coffee transactions (March 2024 - March 2025)  
**Tools:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, SQL

---

## Objectives
- Define 3-5 core KPIs with formulas and business rationale
- Perform deep-dive analysis (cohort and segmentation)
- Build specification for interactive dashboard
- Provide actionable business recommendations

---

## Key Deliverables

### 1. Core KPI Framework (5 KPIs)
- **Daily Revenue Run Rate (DRR):** $294.61 (target: $339)
- **Average Transaction Value (ATV):** $31.65 (target: $34.82)
- **Product Mix Performance (PMP):** 68% Coffee-Milk, 16% Non-Coffee, 15% Black Coffee
- **Peak Hour Utilization Rate (PHUR):** 25.3% (optimal: 24-28%)
- **Revenue Consistency Index (RCI):** 69.6% (target: 75%)

### 2. Cohort Analysis
- Analyzed 13 monthly cohorts (March 2024 - March 2025)
- Best performing: October 2024 ($13,891 revenue, 426 transactions)
- Seasonal patterns identified: Q4 strongest (+12% vs Q1), Q2 weakest (-25%)

### 3. Customer Segmentation
- 4 ML-based segments using K-Means clustering
- **Most Valuable:** Standard Shoppers Segment 2 (29.2%, $35,680 revenue)
- **Premium Buyers:** Morning Premium Buyers (22.7%, $34.32 avg)
- **Weekend Warriors:** 100% weekend shoppers (24.8%, $27,870 revenue)

### 4. Interactive Dashboard Specification
- 5-page dashboard design (Executive, Cohort, Segmentation, Product, Operations)
- Technical specs for Tableau/Power BI implementation
- Real-time KPI monitoring framework

---

## Project Structure

```
task3/
├── README.md                          # This file
├── reports/
│   ├── KPI_Definitions.md             # Detailed KPI documentation
│   └── Deep_Dive_Analysis_Report.md   # Comprehensive analysis report
├── dashboard/
│   └── Dashboard_Specification.md     # Interactive dashboard specs
├── scripts/
│   ├── 01_cohort_analysis.py          # Cohort analysis script
│   └── 02_segmentation_analysis.py    # Customer segmentation script
└── analysis/
    ├── cohort_detailed_data.csv       # Cohort metrics
    ├── cohort_retention_matrix.csv    # Retention heatmap data
    ├── segment_profiles.csv           # Segment characteristics
    └── [8 visualization charts]       # Analysis charts
```

---

## Key Findings

### Revenue Insights
- **Total Revenue:** $112,245.58 across 381 days
- **Average Daily Revenue:** $294.61
- **Peak Performance:** October 2024 ($448/day avg)
- **Seasonal Gap:** Q2 35% below Q1 (major opportunity)

### Cohort Patterns
- **Q4 Dominance:** 315 avg initial transactions (+12% vs Q1)
- **Q2 Weakness:** 211 avg transactions (-25% vs Q1)
- **Consistency:** Q1 and Q3 similar (280 vs 284)

### Customer Segments
| Segment | Size | Revenue | Avg Trans | Peak Hour |
|---------|------|---------|-----------|-----------|
| Standard 2 | 29.2% | $35,680 | $34.44 | 19:00 |
| Standard 3 | 24.8% | $27,870 | $31.74 | 12:00 |
| Standard 4 | 23.4% | $21,102 | $25.46 | 11:00 |
| Morning Premium | 22.7% | $27,593 | $34.32 | 10:00 |

### Strategic Opportunities
1. **Off-Peak Optimization:** 27.3% of transactions occur off-peak (potential +20%)
2. **Weekend Growth:** Current 25% of revenue (target 30%)
3. **Non-Coffee Expansion:** 16.4% of revenue (target 20%)
4. **Premium Upselling:** 40% of transactions drive 46% of revenue

---

## Business Recommendations

### Priority 1: Revenue Growth (0-30 Days)
**Initiatives:**
1. Off-peak promotion campaign (+$6,100/month)
2. Premium upselling program (+$5,600/month)
3. Weekend expansion initiative (+$5,600/month)

**Expected Impact:** +$17,300 monthly revenue (+15.4%)

### Priority 2: Product Mix (1-3 Months)
**Initiatives:**
1. Evening non-coffee campaign (+$4,000/month)
2. Seasonal menu development (Q2 focus)
3. Portfolio diversification (reduce 68% dependency)

**Expected Impact:** More resilient revenue mix, +$12,000 in Q2

### Priority 3: Segment Strategy (3-6 Months)
**Segment-Specific Programs:**
- Evening high-value customers: VIP access, premium releases
- Weekend warriors: Family bundles, loyalty rewards
- Budget-conscious: Value deals, subscription service
- Morning premium: Early-bird specials, corporate partnerships

---

## KPI Dashboard Framework

### Daily Monitoring
- Daily Revenue Run Rate vs Target
- Transaction count by hour
- Product mix % (real-time)
- Peak hour performance

### Weekly Reports
- Cohort acquisition trends
- Segment performance comparison
- Weekend vs weekday analysis
- Product category evolution

### Monthly Reviews
- KPI achievement dashboard
- Segment growth tracking
- Revenue consistency trends
- Initiative impact assessment

---

## Usage

### Run Analysis Scripts
```bash
# Cohort analysis
python scripts/01_cohort_analysis.py

# Customer segmentation
python scripts/02_segmentation_analysis.py
```

### View Results
- **Reports:** `reports/` directory (KPIs, Deep-Dive Report)
- **Dashboard Spec:** `dashboard/Dashboard_Specification.md`
- **Analysis Data:** `analysis/` directory (CSV files + charts)

---

## Dashboard Implementation

### Recommended Platform
**Option 1:** Tableau Public/Desktop
- Best visualizations, easy to use
- Professional presentation quality

**Option 2:** Power BI  
- Microsoft integration
- $10/user/month

**Option 3:** Looker Studio (Google)
- Free, cloud-based
- Quick deployment

### Implementation Steps
1. **Data Prep (Days 1-2):** Clean data, create calculated fields
2. **Build (Days 3-7):** Create 5 dashboard pages
3. **Test (Days 8-10):** UAT, performance optimization
4. **Deploy (Days 11-12):** Publish, train users

**Expected Timeline:** 12 days from data to live dashboard

---

## Expected Business Impact

### 12-Month Projections
| Metric | Current | Target | Growth |
|--------|---------|--------|--------|
| Annual Revenue | $112,246 | $134,695 | +20% |
| Daily Run Rate | $294.61 | $353.53 | +20% |
| Avg Transaction | $31.65 | $34.82 | +10% |
| Weekend % | 25.0% | 30.0% | +5pp |

### Revenue Bridge (+$22,449 Annual Growth)
- Off-Peak Optimization: +$7,320 (33%)
- Premium Upselling: +$6,720 (30%)
- Weekend Expansion: +$6,720 (30%)
- Q2 Seasonal Campaign: +$1,689 (7%)

### ROI Analysis
- Investment: $12,000 (marketing, training, technology)
- Year 1 Net: Break-even in 16 months
- Ongoing: $8,980 annual profit contribution

---

## Technical Details

### Analysis Methods
- **Cohort Analysis:** Monthly cohort grouping, retention tracking
- **K-Means Clustering:** 4 segments, StandardScaler normalization
- **Statistical Analysis:** Mean, median, std dev, correlation
- **Time Series:** Trend analysis, seasonality detection

### Visualizations Created
1. Cohort retention heatmap
2. Cohort revenue trends
3. Cohort ATV heatmap
4. Cohort size distribution
5. Value segment distribution
6. Time-product heatmap
7. ML segment comparison
8. Day-product revenue chart

---

## Success Criteria

**3-Month Targets:**
-  DRR increase to $310/day (+5%)
-  Weekend revenue to 27.5% (+2.5pp)
-  Off-peak transactions +10%

**6-Month Targets:**
-  DRR increase to $325/day (+10%)
-  Non-coffee revenue to 18% (+1.6pp)
-  ATV increase to $33.00 (+4.3%)

**12-Month Targets:**
-  DRR increase to $353/day (+20%)
-  Weekend revenue to 30% (+5pp)
-  RCI improvement to 73% (+3.4pp)

---

## Conclusion

This deep-dive analysis reveals a stable coffee shop with significant growth opportunities. Five core KPIs provide performance visibility, cohort analysis identifies seasonal patterns, and segmentation reveals four distinct customer groups to target.

**Key Takeaways:**
1. Strong fundamentals with 20% growth potential
2. Q4 strongest, Q2 weakest (seasonal opportunity)
3. Evening/weekend segments = highest growth
4. Premium customers (40%) drive 46% of revenue
5. Off-peak optimization can add $7,320 annual revenue

**Next Steps:** Implement dashboard, launch priority initiatives, monitor KPIs weekly

---

**Status:**  Complete  
**Date:** February 19, 2026  
**Analyst:** Data Analytics Intern
