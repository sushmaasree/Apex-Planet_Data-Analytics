"""
TASK 3: DEEP-DIVE ANALYSIS - COHORT ANALYSIS
=============================================
Purpose: Analyze customer behavior patterns over time using cohort methodology
Author: Data Analytics Intern
Date: February 19, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

print("="*80)
print("TASK 3 - DEEP-DIVE ANALYSIS: COHORT ANALYSIS")
print("="*80)

# ============================================================================
# LOAD DATA
# ============================================================================
print("\n[1] Loading dataset...")
df = pd.read_csv('/home/claude/task3/Coffee_Sales_Clean.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['Date'])
print(f"✓ Dataset loaded: {len(df):,} transactions")

# ============================================================================
# COHORT DEFINITION: MONTH-BASED COHORTS
# ============================================================================
print("\n[2] Creating Monthly Cohorts...")

# Define cohort as the first month a customer-like pattern appears
# Since we don't have customer IDs, we'll use date-based cohorts
df['Cohort'] = df['Date'].dt.to_period('M')
df['Order_Month'] = df['Date'].dt.to_period('M')

# Calculate metrics by cohort and month
cohort_data = df.groupby(['Cohort', 'Order_Month']).agg({
    'money': ['sum', 'count', 'mean']
}).reset_index()

cohort_data.columns = ['Cohort', 'Order_Month', 'Revenue', 'Transactions', 'Avg_Transaction']

# Calculate period number (months since cohort start)
cohort_data['Period'] = (cohort_data['Order_Month'] - cohort_data['Cohort']).apply(lambda x: x.n)

print(f"✓ Created {df['Cohort'].nunique()} monthly cohorts")
print(f"✓ Date range: {df['Cohort'].min()} to {df['Cohort'].max()}")

# ============================================================================
# COHORT ANALYSIS METRICS
# ============================================================================
print("\n[3] Calculating Cohort Metrics...")

# Pivot table for transactions
cohort_transactions = cohort_data.pivot_table(
    index='Cohort',
    columns='Period',
    values='Transactions',
    fill_value=0
)

# Pivot table for revenue
cohort_revenue = cohort_data.pivot_table(
    index='Cohort',
    columns='Period',
    values='Revenue',
    fill_value=0
)

# Calculate retention-like metric (transactions in subsequent months)
cohort_retention = cohort_transactions.divide(cohort_transactions[0], axis=0) * 100

print("\nCohort Transaction Retention (%):")
print(cohort_retention.round(1))

# ============================================================================
# COHORT ANALYSIS SUMMARY
# ============================================================================
print("\n[4] Cohort Analysis Summary")
print("-" * 80)

# Get first 3 months performance for each cohort
summary_stats = []
for cohort in cohort_transactions.index[:5]:  # Top 5 cohorts
    cohort_str = str(cohort)
    initial_trans = cohort_transactions.loc[cohort, 0]
    initial_revenue = cohort_revenue.loc[cohort, 0]
    
    # Get months 1, 2, 3 if available
    month_1_trans = cohort_transactions.loc[cohort, 1] if 1 in cohort_transactions.columns else 0
    month_2_trans = cohort_transactions.loc[cohort, 2] if 2 in cohort_transactions.columns else 0
    
    summary_stats.append({
        'Cohort': cohort_str,
        'Initial_Transactions': initial_trans,
        'Initial_Revenue': initial_revenue,
        'Month_1_Transactions': month_1_trans,
        'Month_2_Transactions': month_2_trans,
        'Retention_M1': (month_1_trans / initial_trans * 100) if initial_trans > 0 else 0,
        'Retention_M2': (month_2_trans / initial_trans * 100) if initial_trans > 0 else 0
    })

summary_df = pd.DataFrame(summary_stats)
print("\nTop 5 Cohort Performance:")
print(summary_df.to_string(index=False))

# ============================================================================
# VISUALIZATIONS
# ============================================================================
print("\n[5] Creating visualizations...")

# 1. Cohort Retention Heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(cohort_retention, annot=True, fmt='.0f', cmap='RdYlGn', 
            linewidths=0.5, vmin=0, vmax=100)
plt.title('Cohort Analysis: Monthly Transaction Retention (%)', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Months Since First Transaction', fontsize=12)
plt.ylabel('Cohort (First Transaction Month)', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/01_cohort_retention_heatmap.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Cohort retention heatmap saved")
plt.close()

# 2. Cohort Revenue Trends
plt.figure(figsize=(14, 8))
for cohort in cohort_revenue.index[:6]:  # First 6 cohorts
    cohort_line = cohort_revenue.loc[cohort]
    plt.plot(cohort_line.index, cohort_line.values, 
             marker='o', linewidth=2, label=str(cohort))

plt.xlabel('Months Since Cohort Start', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.title('Cohort Revenue Trends Over Time', fontsize=14, fontweight='bold')
plt.legend(title='Cohort', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/02_cohort_revenue_trends.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Cohort revenue trends saved")
plt.close()

# 3. Average Transaction Value by Cohort
cohort_atv = cohort_data.pivot_table(
    index='Cohort',
    columns='Period',
    values='Avg_Transaction',
    fill_value=0
)

plt.figure(figsize=(14, 8))
sns.heatmap(cohort_atv, annot=True, fmt='.2f', cmap='Blues', 
            linewidths=0.5, vmin=0)
plt.title('Average Transaction Value by Cohort ($)', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Months Since First Transaction', fontsize=12)
plt.ylabel('Cohort (First Transaction Month)', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/03_cohort_atv_heatmap.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Cohort ATV heatmap saved")
plt.close()

# 4. Cohort Size Distribution
plt.figure(figsize=(12, 6))
cohort_sizes = cohort_transactions[0].sort_values(ascending=False)
bars = plt.bar(range(len(cohort_sizes)), cohort_sizes.values, 
               color='steelblue', edgecolor='black')
plt.xticks(range(len(cohort_sizes)), 
           [str(c) for c in cohort_sizes.index], rotation=45, ha='right')
plt.xlabel('Cohort Month', fontsize=12)
plt.ylabel('Initial Transactions', fontsize=12)
plt.title('Cohort Size Distribution (Initial Month Transactions)', 
          fontsize=14, fontweight='bold')
plt.grid(alpha=0.3, axis='y')

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/04_cohort_size_distribution.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Cohort size distribution saved")
plt.close()

# ============================================================================
# KEY INSIGHTS
# ============================================================================
print("\n[6] KEY COHORT INSIGHTS")
print("-" * 80)

# Calculate overall metrics
total_initial = cohort_transactions[0].sum()
avg_initial_revenue = cohort_revenue[0].mean()
avg_retention_m1 = cohort_retention[1].mean() if 1 in cohort_retention.columns else 0
avg_retention_m2 = cohort_retention[2].mean() if 2 in cohort_retention.columns else 0

print(f"\n📊 Overall Cohort Metrics:")
print(f"   • Total customers acquired: {total_initial:,.0f} transactions")
print(f"   • Average initial revenue: ${avg_initial_revenue:,.2f}")
print(f"   • Average Month 1 retention: {avg_retention_m1:.1f}%")
print(f"   • Average Month 2 retention: {avg_retention_m2:.1f}%")

# Best and worst performing cohorts
best_cohort = cohort_revenue[0].idxmax()
worst_cohort = cohort_revenue[0].idxmin()

print(f"\n🏆 Best Performing Cohort:")
print(f"   • Cohort: {best_cohort}")
print(f"   • Initial Revenue: ${cohort_revenue.loc[best_cohort, 0]:,.2f}")
print(f"   • Initial Transactions: {cohort_transactions.loc[best_cohort, 0]:.0f}")

print(f"\n⚠️ Weakest Performing Cohort:")
print(f"   • Cohort: {worst_cohort}")
print(f"   • Initial Revenue: ${cohort_revenue.loc[worst_cohort, 0]:,.2f}")
print(f"   • Initial Transactions: {cohort_transactions.loc[worst_cohort, 0]:.0f}")

# Seasonal patterns
print(f"\n📅 Seasonal Patterns:")
q1_cohorts = [c for c in cohort_transactions.index if c.month in [1,2,3]]
q2_cohorts = [c for c in cohort_transactions.index if c.month in [4,5,6]]
q3_cohorts = [c for c in cohort_transactions.index if c.month in [7,8,9]]
q4_cohorts = [c for c in cohort_transactions.index if c.month in [10,11,12]]

if q1_cohorts:
    print(f"   • Q1 cohorts avg initial transactions: {cohort_transactions.loc[q1_cohorts, 0].mean():.0f}")
if q2_cohorts:
    print(f"   • Q2 cohorts avg initial transactions: {cohort_transactions.loc[q2_cohorts, 0].mean():.0f}")
if q3_cohorts:
    print(f"   • Q3 cohorts avg initial transactions: {cohort_transactions.loc[q3_cohorts, 0].mean():.0f}")
if q4_cohorts:
    print(f"   • Q4 cohorts avg initial transactions: {cohort_transactions.loc[q4_cohorts, 0].mean():.0f}")

# ============================================================================
# SAVE COHORT DATA
# ============================================================================
print("\n[7] Saving cohort analysis data...")

# Save detailed cohort data
cohort_data.to_csv('/home/claude/task3/analysis/cohort_detailed_data.csv', index=False)
cohort_retention.to_csv('/home/claude/task3/analysis/cohort_retention_matrix.csv')
cohort_revenue.to_csv('/home/claude/task3/analysis/cohort_revenue_matrix.csv')

print("   ✓ Cohort detailed data saved")
print("   ✓ Retention matrix saved")
print("   ✓ Revenue matrix saved")

print("\n" + "="*80)
print("✓ COHORT ANALYSIS COMPLETE!")
print("="*80)
print("\nKey Findings:")
print(f"  • {df['Cohort'].nunique()} monthly cohorts analyzed")
print(f"  • Average Month 1 retention: {avg_retention_m1:.1f}%")
print(f"  • Best cohort: {best_cohort} (${cohort_revenue.loc[best_cohort, 0]:,.0f})")
print(f"  • Seasonal patterns identified across quarters")
