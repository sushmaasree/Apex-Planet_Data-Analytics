"""
TASK 2: MULTIVARIATE ANALYSIS & CORRELATION
============================================
Purpose: Explore relationships between variables using advanced visualizations
Author: Data Analytics Intern
Date: February 12, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

print("="*80)
print("TASK 2 - STEP 3: MULTIVARIATE ANALYSIS & CORRELATION")
print("="*80)

# Load data
print("\n[1] Loading dataset...")
df = pd.read_csv('/home/claude/Coffee_Sales_Analysis_Ready.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['Date'])
print(f"✓ Dataset loaded: {len(df):,} transactions")

# ============================================================================
# CORRELATION ANALYSIS
# ============================================================================
print("\n[2] CORRELATION ANALYSIS")
print("-" * 80)

# Select numerical columns for correlation
numerical_cols = ['money', 'hour_of_day', 'Weekdaysort', 'Monthsort', 
                  'Quarter', 'Week_of_Year', 'Day_of_Month', 'Is_Weekend']
corr_matrix = df[numerical_cols].corr()

print("\n📊 CORRELATION MATRIX (Key Relationships):")
print("\nStrong Correlations (|r| > 0.3):")
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_val = corr_matrix.iloc[i, j]
        if abs(corr_val) > 0.3:
            print(f"   {corr_matrix.columns[i]} ↔ {corr_matrix.columns[j]}: {corr_val:.3f}")

# Create correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=1)
plt.title('Correlation Matrix - Numerical Variables', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/06_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("\n   ✓ Correlation heatmap saved")

# ============================================================================
# BIVARIATE ANALYSIS: PRICE VS VARIABLES
# ============================================================================
print("\n[3] BIVARIATE ANALYSIS: Revenue Relationships")
print("-" * 80)

# Price by Hour of Day
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Revenue by Hour
axes[0, 0].scatter(df['hour_of_day'], df['money'], alpha=0.5, s=20)
axes[0, 0].set_xlabel('Hour of Day', fontsize=11)
axes[0, 0].set_ylabel('Transaction Amount ($)', fontsize=11)
axes[0, 0].set_title('Revenue vs Hour of Day', fontsize=12, fontweight='bold')
axes[0, 0].grid(alpha=0.3)

# Add trend line
z = np.polyfit(df['hour_of_day'], df['money'], 1)
p = np.poly1d(z)
axes[0, 0].plot(df['hour_of_day'].sort_values(), p(df['hour_of_day'].sort_values()), 
                "r--", linewidth=2, label='Trend')
axes[0, 0].legend()

# 2. Revenue by Day of Week
weekday_means = df.groupby('Weekdaysort')['money'].mean()
axes[0, 1].plot(weekday_means.index, weekday_means.values, marker='o', linewidth=2, 
                markersize=8, color='green')
axes[0, 1].set_xlabel('Day of Week (1=Mon, 7=Sun)', fontsize=11)
axes[0, 1].set_ylabel('Average Transaction ($)', fontsize=11)
axes[0, 1].set_title('Average Revenue by Day of Week', fontsize=12, fontweight='bold')
axes[0, 1].grid(alpha=0.3)
axes[0, 1].set_xticks(range(1, 8))

# 3. Revenue by Month
monthly_avg = df.groupby('Monthsort')['money'].mean()
axes[1, 0].bar(monthly_avg.index, monthly_avg.values, color='coral', edgecolor='black')
axes[1, 0].set_xlabel('Month', fontsize=11)
axes[1, 0].set_ylabel('Average Transaction ($)', fontsize=11)
axes[1, 0].set_title('Average Revenue by Month', fontsize=12, fontweight='bold')
axes[1, 0].grid(alpha=0.3, axis='y')

# 4. Revenue Distribution by Product Category
df.boxplot(column='money', by='Product_Category', ax=axes[1, 1])
axes[1, 1].set_xlabel('Product Category', fontsize=11)
axes[1, 1].set_ylabel('Transaction Amount ($)', fontsize=11)
axes[1, 1].set_title('Revenue Distribution by Product Category', fontsize=12, fontweight='bold')
plt.suptitle('')  # Remove default title

plt.tight_layout()
plt.savefig('/home/claude/task2/charts/07_bivariate_analysis.png', dpi=300, bbox_inches='tight')
print("   ✓ Bivariate analysis charts saved")
plt.close()

# ============================================================================
# PRODUCT CATEGORY VS TIME OF DAY ANALYSIS
# ============================================================================
print("\n[4] PRODUCT CATEGORY vs TIME OF DAY")
print("-" * 80)

# Create crosstab
crosstab = pd.crosstab(df['Product_Category'], df['Time_of_Day'], 
                       values=df['money'], aggfunc='sum')
crosstab_pct = pd.crosstab(df['Product_Category'], df['Time_of_Day'], 
                           normalize='index') * 100

print("\nRevenue by Product Category and Time of Day:")
print(crosstab.round(2))

# Visualize as heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(crosstab, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=1)
plt.title('Revenue: Product Category vs Time of Day', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Time of Day', fontsize=12)
plt.ylabel('Product Category', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/08_category_time_heatmap.png', dpi=300, bbox_inches='tight')
print("   ✓ Category vs Time heatmap saved")
plt.close()

# ============================================================================
# WEEKDAY VS HOUR ANALYSIS (Advanced Heatmap)
# ============================================================================
print("\n[5] WEEKDAY vs HOUR ANALYSIS")
print("-" * 80)

# Create pivot table
hour_day_revenue = df.pivot_table(values='money', index='hour_of_day', 
                                   columns='Weekday', aggfunc='sum')

# Reorder columns
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hour_day_revenue = hour_day_revenue[weekday_order]

plt.figure(figsize=(12, 8))
sns.heatmap(hour_day_revenue, cmap='viridis', annot=True, fmt='.0f', linewidths=0.5)
plt.title('Revenue Heatmap: Hour vs Weekday', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Hour of Day', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/09_hour_weekday_heatmap.png', dpi=300, bbox_inches='tight')
print("   ✓ Hour vs Weekday heatmap saved")
plt.close()

# ============================================================================
# SCATTER PLOTS: MARKETING SPEND EQUIVALENT
# ============================================================================
print("\n[6] ADVANCED SCATTER PLOTS")
print("-" * 80)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Product popularity vs average price
product_stats = df.groupby('coffee_name').agg({
    'money': ['count', 'mean', 'sum']
}).round(2)
product_stats.columns = ['Count', 'Avg_Price', 'Revenue']

axes[0].scatter(product_stats['Avg_Price'], product_stats['Count'], 
                s=product_stats['Revenue']/50, alpha=0.6, color='purple')
for idx, product in enumerate(product_stats.index):
    axes[0].annotate(product, 
                     (product_stats['Avg_Price'].iloc[idx], 
                      product_stats['Count'].iloc[idx]),
                     fontsize=8, alpha=0.7)
axes[0].set_xlabel('Average Price ($)', fontsize=11)
axes[0].set_ylabel('Sales Count', fontsize=11)
axes[0].set_title('Product Popularity vs Price\n(Bubble size = Revenue)', 
                  fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)

# Time of Day vs Average Transaction
time_hour = df.groupby(['Time_of_Day', 'hour_of_day']).agg({
    'money': ['mean', 'count']
}).reset_index()
time_hour.columns = ['Time_of_Day', 'Hour', 'Avg_Price', 'Count']

colors = {'Morning': 'gold', 'Afternoon': 'orange', 'Night': 'navy'}
for period in ['Morning', 'Afternoon', 'Night']:
    period_data = time_hour[time_hour['Time_of_Day'] == period]
    axes[1].scatter(period_data['Hour'], period_data['Avg_Price'], 
                    s=period_data['Count']*2, alpha=0.6, 
                    color=colors[period], label=period)
axes[1].set_xlabel('Hour of Day', fontsize=11)
axes[1].set_ylabel('Average Transaction ($)', fontsize=11)
axes[1].set_title('Hour vs Average Transaction by Period\n(Bubble size = Transaction count)', 
                  fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/task2/charts/10_advanced_scatter_plots.png', dpi=300, bbox_inches='tight')
print("   ✓ Advanced scatter plots saved")
plt.close()

# ============================================================================
# PAIR PLOT (Selected Variables)
# ============================================================================
print("\n[7] PAIR PLOT ANALYSIS")
print("-" * 80)

# Select key variables
pair_data = df[['money', 'hour_of_day', 'Weekdaysort', 'Is_Weekend']].sample(500)
pair_plot = sns.pairplot(pair_data, diag_kind='kde', plot_kws={'alpha': 0.6})
pair_plot.fig.suptitle('Pair Plot: Key Variables Relationships', 
                       fontsize=14, fontweight='bold', y=1.02)
plt.savefig('/home/claude/task2/charts/11_pair_plot.png', dpi=300, bbox_inches='tight')
print("   ✓ Pair plot saved")
plt.close()

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================
print("\n[8] KEY FINDINGS FROM MULTIVARIATE ANALYSIS")
print("-" * 80)

# Calculate key statistics
peak_hour_revenue = df.groupby('hour_of_day')['money'].sum().idxmax()
peak_day_revenue = df.groupby('Weekday')['money'].sum().idxmax()
best_product_combo = df.groupby(['Product_Category', 'Time_of_Day'])['money'].sum().idxmax()

print(f"\n📊 Key Insights:")
print(f"   • Peak revenue hour: {peak_hour_revenue}:00")
print(f"   • Best performing day: {peak_day_revenue}")
print(f"   • Best product-time combo: {best_product_combo[0]} during {best_product_combo[1]}")
print(f"   • Weekend revenue: ${df[df['Is_Weekend']==1]['money'].sum():,.2f}")
print(f"   • Weekday revenue: ${df[df['Is_Weekend']==0]['money'].sum():,.2f}")

# Correlation insights
money_hour_corr = df['money'].corr(df['hour_of_day'])
money_weekend_corr = df['money'].corr(df['Is_Weekend'])
print(f"\n📈 Correlation Insights:")
print(f"   • Revenue vs Hour: {money_hour_corr:.3f}")
print(f"   • Revenue vs Weekend: {money_weekend_corr:.3f}")

print("\n" + "="*80)
print("✓ MULTIVARIATE ANALYSIS & CORRELATION COMPLETE!")
print("="*80)
print("\nGenerated Visualizations:")
print("   1. Correlation heatmap")
print("   2. Bivariate analysis (4 charts)")
print("   3. Category vs Time heatmap")
print("   4. Hour vs Weekday heatmap")
print("   5. Advanced scatter plots")
print("   6. Pair plot")
