# DEEP-DIVE ANALYSIS REPORT
## Coffee Sales Business Intelligence

**Project:** Task 3 - Deep-Dive Analysis & Interactive Dashboarding  
**Date:** February 19, 2026  
**Analyst:** Data Analytics Intern

---

## EXECUTIVE SUMMARY

This deep-dive analysis examines complex, multi-faceted business problems in the coffee sales dataset through cohort analysis and customer segmentation. The analysis reveals critical insights about customer behavior, revenue patterns, and segment-specific opportunities that drive strategic decision-making.

**Key Deliverables:**
- 5 Core KPIs with formulas and business rationale
- Cohort analysis revealing seasonal acquisition patterns
- Customer segmentation identifying 4 distinct customer groups
- Interactive dashboard specification for ongoing monitoring

---

## SECTION 1: CORE KPI FRAMEWORK

### KPI Overview

We have defined 5 core Key Performance Indicators that provide comprehensive visibility into business performance:

| KPI | Current Value | Target | Status |
|-----|---------------|--------|--------|
| Daily Revenue Run Rate (DRR) | $294.61 | $339.00 | 🟡 Monitor |
| Average Transaction Value (ATV) | $31.65 | $34.82 | 🟢 Good |
| Product Mix Performance (PMP) | 68% Milk / 16% Non-Coffee / 15% Black | 65% / 20% / 15% | 🟡 Rebalance |
| Peak Hour Utilization Rate (PHUR) | 25.3% | 24-28% | 🟢 Optimal |
| Revenue Consistency Index (RCI) | 69.6% | 75.0% | 🟡 Improve |

### KPI #1: Daily Revenue Run Rate (DRR)

**Formula:**
```
DRR = Total Revenue / Number of Operating Days
DRR = $112,245.58 / 381 = $294.61 per day
```

**Business Rationale:**
- Predicts future revenue and identifies performance trends
- Essential for budget planning, staffing, and inventory decisions
- Enables comparison across different time periods

**Key Insights:**
- **Peak Months:** October ($448/day), March ($294/day)
- **Low Months:** April ($191/day), January ($229/day)
- **Seasonal Pattern:** Q1 and Q4 strongest (31.6% and 27.4%), Q2 weakest (19.2%)
- **Opportunity:** 15% growth target = $339/day run rate

**Actionable Recommendations:**
1. Launch spring promotions in Q2 to address 35% performance gap vs Q1
2. Introduce seasonal drinks during low-revenue months
3. Implement dynamic pricing during off-peak days

---

### KPI #2: Average Transaction Value (ATV)

**Formula:**
```
ATV = Total Revenue / Total Transactions
ATV = $112,245.58 / 3,547 = $31.65
```

**Business Rationale:**
- Measures revenue per customer visit and upsell effectiveness
- Validates pricing strategy and product bundling success
- Indicates staff training effectiveness on premium products

**Segmentation Analysis:**
- **Premium transactions:** $35.76 avg (39.9% of sales → 46% of revenue)
- **Mid-range transactions:** $32.82 avg (26.2% of sales)
- **Standard transactions:** $27.92 avg (33.9% of sales)

**Time-Based Patterns:**
- Morning: $30.42 avg
- Afternoon: $31.64 avg
- Night: $32.89 avg (+8% vs morning)

**Actionable Recommendations:**
1. Evening promotion focus (highest ATV at $32.89)
2. Morning bundle deals to increase ATV by 8%
3. Staff training on premium product upselling (currently driving 46% of revenue from 40% of transactions)

---

### KPI #3: Product Mix Performance (PMP)

**Formula:**
```
PMP = (Category Revenue / Total Revenue) × 100
```

**Current Mix:**
| Category | Revenue | % of Total | Units | Avg Price | Risk Level |
|----------|---------|------------|-------|-----------|------------|
| Coffee - Milk | $76,450 | 68.1% | 2,339 | $32.68 | ⚠️ High Dependency |
| Non-Coffee | $18,455 | 16.4% | 515 | $35.83 | ✅ High Margin Opportunity |
| Coffee - Black | $17,341 | 15.4% | 693 | $25.02 | ✅ Stable Base |

**Business Rationale:**
- Ensures balanced revenue streams
- Reduces dependency risk (currently 68% from one category)
- Identifies high-margin product opportunities

**Key Finding:** Non-coffee items have highest average price ($35.83) and show 138% increase in evening vs morning sales

**Actionable Recommendations:**
1. Target 20% revenue from non-coffee (currently 16.4%)
2. Evening marketing campaign for hot chocolate and cocoa
3. Introduce seasonal non-coffee items to diversify portfolio

---

### KPI #4: Peak Hour Utilization Rate (PHUR)

**Formula:**
```
PHUR = (Peak Hour Transactions / Total Transactions) × 100
PHUR = 898 / 3,547 × 100 = 25.3%
```

**Hourly Distribution:**
- **Peak Hours:** 10 AM (323), 16 PM (298), 14 PM (277) = 898 transactions (25.3%)
- **Off-Peak:** 6-9 AM and 20-22 PM = 968 transactions (27.3%)

**Business Rationale:**
- Optimizes staffing levels and reduces wait times
- Maximizes revenue during high-traffic periods
- Identifies capacity utilization opportunities

**Staffing Recommendations:**
- **Peak Hours (10-11 AM, 14-16 PM):** 3-4 staff members
- **Standard Hours:** 2-3 staff members  
- **Off-Peak Hours:** 1-2 staff members

**Actionable Recommendations:**
1. Happy hour pricing 7-9 AM and 8-10 PM
2. Loyalty rewards for off-peak visits
3. Increase off-peak transactions by 20% (add 194 daily transactions)

---

### KPI #5: Revenue Consistency Index (RCI)

**Formula:**
```
RCI = 1 - (Standard Deviation / Mean)
RCI = 1 - (89.47 / 294.61) = 0.696 = 69.6%
```

**Consistency Analysis:**
- **Daily Revenue RCI:** 69.6% (moderate consistency)
- **Transaction Value RCI:** 84.6% (high consistency)
- **Month-to-Month RCI:** 65.4% (seasonal impact)

**Business Rationale:**
- Predicts cash flow stability
- Reduces forecasting risk
- Enables confident financial planning

**Risk Factors:**
- ⚠️ Seasonal Variation: Q2 -35% below Q1
- ⚠️ Day of Week: Sunday -27% below Tuesday
- ✅ Time of Day: Highly balanced (95.7% RCI)

**Actionable Recommendations:**
1. Seasonal promotions to smooth Q2 dip
2. Weekend-specific bundles to boost Sunday performance
3. Target 75% RCI through stabilization initiatives

---

## SECTION 2: COHORT ANALYSIS

### Methodology

Monthly cohort analysis examining customer acquisition patterns and performance over time. Each cohort represents customers acquired in a specific month.

### Key Findings

**Cohort Performance:**
- **Total Cohorts:** 13 monthly cohorts (March 2024 - March 2025)
- **Best Performing:** October 2024 ($13,891 revenue, 426 transactions)
- **Weakest Performing:** April 2024 ($5,719 revenue, 168 transactions)

**Seasonal Acquisition Patterns:**
| Quarter | Avg Initial Transactions | Performance |
|---------|-------------------------|-------------|
| Q1 | 280 | Strong |
| Q2 | 211 | Weak (-25% vs Q1) |
| Q3 | 284 | Strong (recovery) |
| Q4 | 315 | Strongest (+12% vs Q1) |

### Cohort Insights

**1. Q4 Dominance:**
- Q4 cohorts show 12% higher acquisition vs Q1
- October alone captured 426 transactions (highest single month)
- Holiday season and weather factors likely drive performance

**2. Q2 Weakness:**
- Q2 cohorts 25% below Q1 baseline
- April particularly weak (168 transactions)
- Spring/early summer slowdown pattern identified

**3. Consistency Pattern:**
- Q1 and Q3 show similar acquisition levels (280 vs 284)
- Suggests semi-annual peak pattern
- Indicates predictable seasonal cycles

### Cohort-Based Recommendations

**Immediate Actions:**
1. **Q2 Acquisition Campaign:** Launch spring promotion to capture 280+ transactions per month
2. **Q4 Optimization:** Maintain excellence with seasonal drinks and extended hours
3. **Cohort Tracking:** Implement monthly cohort dashboard for real-time monitoring

**Strategic Initiatives:**
1. Develop cohort-specific retention programs
2. Create seasonal acquisition playbooks based on historical patterns
3. Forecast annual revenue using cohort trending

---

## SECTION 3: CUSTOMER SEGMENTATION

### Segmentation Framework

We applied multiple segmentation approaches to understand customer diversity:

1. **Behavioral Segmentation** (Rule-Based)
2. **Machine Learning Segmentation** (K-Means Clustering)

### Machine Learning Segments (K-Means, N=4)

| Segment | Size | % of Total | Avg Transaction | Total Revenue | Peak Hour | Weekend % |
|---------|------|------------|-----------------|---------------|-----------|-----------|
| **Standard Shoppers 2** | 1,036 | 29.2% | $34.44 | $35,680 | 19:00 | 0.0% |
| **Standard Shoppers 3** | 878 | 24.8% | $31.74 | $27,870 | 12:00 | 100.0% |
| **Standard Shoppers 4** | 829 | 23.4% | $25.46 | $21,102 | 11:00 | 1.3% |
| **Morning Premium Buyers** | 804 | 22.7% | $34.32 | $27,593 | 10:00 | 0.0% |

### Segment Profiles

**Segment 1: Standard Shoppers 2** (Most Valuable)
- **Size:** 1,036 transactions (29.2%)
- **Revenue:** $35,680 (31.8% of total)
- **Characteristics:** Evening shoppers (19:00 peak), high-value transactions ($34.44)
- **Top Product:** Latte
- **Strategy:** Premium evening bundles, loyalty rewards, extended hours

**Segment 2: Standard Shoppers 3** (Weekend Warriors)
- **Size:** 878 transactions (24.8%)
- **Revenue:** $27,870 (24.8% of total)
- **Characteristics:** 100% weekend shoppers, lunch peak (12:00)
- **Top Product:** Americano with Milk
- **Strategy:** Weekend promotions, brunch menu, family bundles

**Segment 3: Standard Shoppers 4** (Budget-Conscious)
- **Size:** 829 transactions (23.4%)
- **Revenue:** $21,102 (18.8% of total)
- **Characteristics:** Lower ATV ($25.46), mid-morning peak (11:00)
- **Top Product:** Americano
- **Strategy:** Value bundles, loyalty discounts, upsell training

**Segment 4: Morning Premium Buyers** (High-Value Early Birds)
- **Size:** 804 transactions (22.7%)
- **Revenue:** $27,593 (24.6% of total)
- **Characteristics:** Early peak (10:00), premium products ($34.32)
- **Top Product:** Latte
- **Strategy:** Morning specials, early-bird rewards, premium focus

### Behavioral Segmentation Insights

**By Value Tier:**
- **Premium** (15.3%): $35.76 avg, drives 15.9% of revenue
- **Standard** (33.9%): $27.92 avg
- **Mid-Range** (26.2%): $32.82 avg

**By Time Preference:**
- **Morning Shoppers** (25.3%): $30.42 avg, coffee-focused
- **Afternoon Shoppers** (42.0%): $31.64 avg, balanced mix
- **Evening Shoppers** (32.7%): $32.89 avg, higher non-coffee preference

**By Product Preference:**
- **Milk Coffee Lovers** (65.9%): Largest segment, $32.68 avg
- **Alternative Beverage Seekers** (14.5%): $35.83 avg (highest!)
- **Pure Coffee Enthusiasts** (19.5%): $25.02 avg

### Cross-Segment Opportunities

**High-Value Combinations:**
1. **Evening × Premium:** Largest revenue opportunity ($35+ ATV)
2. **Weekend × Alternative Beverages:** Growing segment (138% evening increase)
3. **Morning × Milk Coffee:** Stable, high-volume base

**Growth Targets:**
1. Convert 10% of Budget-Conscious to Standard (+$2,110 revenue)
2. Grow Weekend Warriors segment by 15% (+132 transactions)
3. Increase Alternative Beverage segment from 14.5% to 20% (+$7,000 revenue)

---

## SECTION 4: STRATEGIC RECOMMENDATIONS

### Priority 1: Revenue Growth (0-30 Days)

**Initiative 1: Off-Peak Promotion Campaign**
- **Target:** Increase 6-9 AM and 8-10 PM transactions by 20%
- **Action:** Happy hour pricing ($2 off), loyalty double points
- **Expected Impact:** +194 daily transactions, +$6,100 monthly revenue

**Initiative 2: Premium Upselling Program**
- **Target:** Increase premium transaction % from 39.9% to 45%
- **Action:** Staff training, product sampling, bundle creation
- **Expected Impact:** +$5,600 monthly revenue

**Initiative 3: Weekend Warrior Expansion**
- **Target:** Grow weekend revenue from 25% to 30% of weekly total
- **Action:** Weekend-specific bundles, extended Saturday hours, family promotions
- **Expected Impact:** +$5,600 weekend revenue per month

### Priority 2: Product Mix Optimization (1-3 Months)

**Initiative 1: Evening Non-Coffee Campaign**
- **Target:** Grow non-coffee revenue from 16.4% to 20%
- **Action:** Evening marketing, seasonal specials, combo deals
- **Expected Impact:** +$4,000 monthly revenue

**Initiative 2: Seasonal Menu Development**
- **Target:** Smooth Q2 revenue dip (currently -35% vs Q1)
- **Action:** Spring/summer drink menu, iced coffee expansion
- **Expected Impact:** +$8,000 in Q2 revenue (April-June)

**Initiative 3: Product Portfolio Diversification**
- **Target:** Reduce coffee-milk dependency from 68% to 65%
- **Action:** Introduce 2-3 new non-coffee items, test food pairings
- **Expected Impact:** More resilient revenue mix

### Priority 3: Customer Segmentation Strategy (3-6 Months)

**Segment-Specific Programs:**

1. **Standard Shoppers 2** (Evening, High-Value)
   - VIP evening access program
   - Premium product early release
   - Personalized recommendations

2. **Weekend Warriors** (Segment 3)
   - Family bundle promotions
   - Weekend loyalty rewards
   - Brunch menu expansion

3. **Budget-Conscious** (Segment 4)
   - Value meal deals
   - Subscription service ($25/week)
   - Upsell to mid-range products

4. **Morning Premium Buyers** (Segment 4)
   - Early-bird exclusive drinks
   - Quick-service lane
   - Corporate partnership program

### Priority 4: Operational Excellence (Ongoing)

**KPI Monitoring Framework:**
- **Daily:** DRR, ATV, transaction count vs targets
- **Weekly:** PHUR, weekend %, product mix
- **Monthly:** RCI, cohort performance, segment trends

**Technology Enablement:**
- Implement real-time dashboard (Tableau/Power BI)
- Automated daily KPI reports
- Predictive analytics for forecasting
- Customer behavior tracking system

---

## SECTION 5: EXPECTED BUSINESS IMPACT

### Revenue Projections (12-Month Horizon)

**Current Baseline:**
- Annual Revenue: $112,246
- Average Daily: $294.61
- Average Transaction: $31.65

**Target Performance (Year 1):**
| Metric | Current | Target | Growth |
|--------|---------|--------|--------|
| Annual Revenue | $112,246 | $134,695 | +20% |
| Daily Run Rate | $294.61 | $353.53 | +20% |
| Avg Transaction | $31.65 | $34.82 | +10% |
| Weekend Revenue % | 25.0% | 30.0% | +5pp |
| Off-Peak Volume | 27.3% | 32.8% | +5.5pp |

**Revenue Bridge (Path to +$22,449 Annual Growth):**
1. Off-Peak Optimization: +$7,320 (33% of growth)
2. Premium Upselling: +$6,720 (30% of growth)
3. Weekend Expansion: +$6,720 (30% of growth)
4. Q2 Seasonal Campaign: +$1,689 (7% of growth)

### Return on Investment

**Investment Required:**
- Marketing & Promotions: $5,000
- Staff Training: $2,000
- Technology (Dashboard): $3,000
- Menu Development: $2,000
- **Total:** $12,000

**Expected Return:**
- Additional Revenue: $22,449
- Additional Margin (40%): $8,980
- Net Benefit: $8,980 - $12,000 = -$3,020 (Year 1)
- **ROI:** Break-even in 16 months, then $8,980 annual profit

---

## SECTION 6: MONITORING & CONTINUOUS IMPROVEMENT

### Dashboard KPI Tracking

**Real-Time Metrics:**
- Current DRR vs Target ($294.61 → $339.00)
- Live transaction count by hour
- Product mix % (Real-time category distribution)
- Peak hour performance (Actual vs capacity)

**Weekly Reports:**
- Cohort acquisition trends
- Segment performance comparison
- Weekend vs weekday analysis
- Product category mix evolution

**Monthly Reviews:**
- KPI achievement dashboard
- Segment growth tracking
- Revenue consistency trends
- Initiative impact assessment

### Success Criteria

**3-Month Targets:**
- ✅ DRR increase to $310/day (+5%)
- ✅ Weekend revenue to 27.5% of weekly (+2.5pp)
- ✅ Off-peak transactions +10%

**6-Month Targets:**
- ✅ DRR increase to $325/day (+10%)
- ✅ Non-coffee revenue to 18% (+1.6pp)
- ✅ ATV increase to $33.00 (+4.3%)

**12-Month Targets:**
- ✅ DRR increase to $353/day (+20%)
- ✅ Weekend revenue to 30% of weekly (+5pp)
- ✅ RCI improvement to 73% (+3.4pp)

---

## CONCLUSION

This deep-dive analysis reveals a coffee shop with strong fundamentals but significant untapped opportunities. Five core KPIs provide comprehensive performance visibility, while cohort and segmentation analyses identify specific customer groups and behavior patterns to target.

**Key Takeaways:**
1. **Seasonal patterns** drive performance (Q4 strongest, Q2 weakest)
2. **Evening and weekend segments** represent highest growth potential
3. **Product mix diversification** reduces risk and increases margins
4. **Premium customers** (40% of transactions) drive 46% of revenue
5. **Operational optimization** of off-peak hours can add $7,320 annual revenue

By implementing the recommended strategies across segments and time periods, the business can achieve 20% revenue growth within 12 months while improving operational efficiency and customer satisfaction.

---

**Report Prepared By:** Data Analytics Intern  
**Date:** February 19, 2026  
**Version:** 1.0  
**Next Review:** March 19, 2026
