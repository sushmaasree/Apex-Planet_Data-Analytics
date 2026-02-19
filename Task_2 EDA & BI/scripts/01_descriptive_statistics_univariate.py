"""
TASK 2: EXPLORATORY DATA ANALYSIS - DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS
==================================================================================
Purpose: Calculate key summary statistics and understand distributions
Author: Data Analytics Intern
Date: February 12, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*80)
print("TASK 2 - STEP 1: DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS")
print("="*80)

# ============================================================================
# LOAD DATA
# ============================================================================
print("\n[1] Loading cleaned dataset...")
df = pd.read_csv('/home/claude/Coffee_Sales_Analysis_Ready.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['Date'])
print(f"✓ Dataset loaded: {len(df):,} transactions")

# ============================================================================
# NUMERICAL VARIABLES ANALYSIS
# ============================================================================
print("\n[2] NUMERICAL VARIABLES ANALYSIS")
print("-" * 80)

# Revenue Analysis
print("\n📊 REVENUE STATISTICS:")
print(f"   Total Revenue: ${df['money'].sum():,.2f}")
print(f"   Average Transaction: ${df['money'].mean():.2f}")
print(f"   Median Transaction: ${df['money'].median():.2f}")
print(f"   Std Deviation: ${df['money'].std():.2f}")
print(f"   Min Transaction: ${df['money'].min():.2f}")
print(f"   Max Transaction: ${df['money'].max():.2f}")
print(f"   25th Percentile: ${df['money'].quantile(0.25):.2f}")
print(f"   75th Percentile: ${df['money'].quantile(0.75):.2f}")

# Hour of Day Analysis
print("\n📊 HOUR OF DAY STATISTICS:")
print(f"   Average Hour: {df['hour_of_day'].mean():.1f}")
print(f"   Most Common Hour: {df['hour_of_day'].mode()[0]}:00")
print(f"   Operating Hours: {df['hour_of_day'].min()}:00 - {df['hour_of_day'].max()}:00")
print(f"   Peak Morning Hour: {df[df['Time_of_Day']=='Morning']['hour_of_day'].mode()[0]}:00")
print(f"   Peak Afternoon Hour: {df[df['Time_of_Day']=='Afternoon']['hour_of_day'].mode()[0]}:00")
print(f"   Peak Night Hour: {df[df['Time_of_Day']=='Night']['hour_of_day'].mode()[0]}:00")

# ============================================================================
# CATEGORICAL VARIABLES ANALYSIS
# ============================================================================
print("\n[3] CATEGORICAL VARIABLES ANALYSIS")
print("-" * 80)

# Product Analysis
print("\n☕ PRODUCT DISTRIBUTION:")
product_stats = df['coffee_name'].value_counts()
product_pct = (df['coffee_name'].value_counts(normalize=True) * 100).round(2)
for product in product_stats.index:
    count = product_stats[product]
    pct = product_pct[product]
    revenue = df[df['coffee_name']==product]['money'].sum()
    print(f"   {product:.<30} {count:>4} ({pct:>5.1f}%) - Revenue: ${revenue:>8,.2f}")

# Product Category Analysis
print("\n📦 PRODUCT CATEGORY DISTRIBUTION:")
category_stats = df['Product_Category'].value_counts()
category_pct = (df['Product_Category'].value_counts(normalize=True) * 100).round(2)
for category in category_stats.index:
    count = category_stats[category]
    pct = category_pct[category]
    revenue = df[df['Product_Category']==category]['money'].sum()
    print(f"   {category:.<30} {count:>4} ({pct:>5.1f}%) - Revenue: ${revenue:>8,.2f}")

# Time of Day Analysis
print("\n🕐 TIME OF DAY DISTRIBUTION:")
time_stats = df['Time_of_Day'].value_counts()
time_pct = (df['Time_of_Day'].value_counts(normalize=True) * 100).round(2)
for period in ['Morning', 'Afternoon', 'Night']:
    if period in time_stats.index:
        count = time_stats[period]
        pct = time_pct[period]
        revenue = df[df['Time_of_Day']==period]['money'].sum()
        avg_trans = df[df['Time_of_Day']==period]['money'].mean()
        print(f"   {period:.<15} {count:>4} ({pct:>5.1f}%) - Revenue: ${revenue:>8,.2f} - Avg: ${avg_trans:.2f}")

# Weekday Analysis
print("\n📅 WEEKDAY DISTRIBUTION:")
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for day in weekday_order:
    count = len(df[df['Weekday']==day])
    pct = (count / len(df) * 100)
    revenue = df[df['Weekday']==day]['money'].sum()
    print(f"   {day:.<10} {count:>4} ({pct:>5.1f}%) - Revenue: ${revenue:>8,.2f}")

# Weekend vs Weekday
print("\n🎯 WEEKEND vs WEEKDAY:")
weekend_count = df[df['Is_Weekend']==1]['money'].count()
weekday_count = df[df['Is_Weekend']==0]['money'].count()
weekend_revenue = df[df['Is_Weekend']==1]['money'].sum()
weekday_revenue = df[df['Is_Weekend']==0]['money'].sum()
print(f"   Weekday: {weekday_count:>4} transactions - Revenue: ${weekday_revenue:>8,.2f}")
print(f"   Weekend: {weekend_count:>4} transactions - Revenue: ${weekend_revenue:>8,.2f}")

# Price Category Analysis
print("\n💰 PRICE CATEGORY DISTRIBUTION:")
price_stats = df['Price_Category'].value_counts()
price_pct = (df['Price_Category'].value_counts(normalize=True) * 100).round(2)
for category in ['Standard', 'Mid-Range', 'Premium']:
    if category in price_stats.index:
        count = price_stats[category]
        pct = price_pct[category]
        revenue = df[df['Price_Category']==category]['money'].sum()
        print(f"   {category:.<15} {count:>4} ({pct:>5.1f}%) - Revenue: ${revenue:>8,.2f}")

# ============================================================================
# TEMPORAL ANALYSIS
# ============================================================================
print("\n[4] TEMPORAL ANALYSIS")
print("-" * 80)

# Monthly Analysis
print("\n📆 MONTHLY PERFORMANCE:")
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for month in month_order:
    month_data = df[df['Month_name']==month]
    if len(month_data) > 0:
        count = len(month_data)
        revenue = month_data['money'].sum()
        avg_daily = revenue / month_data['Date'].nunique()
        print(f"   {month}: {count:>4} transactions - ${revenue:>8,.2f} - Avg Daily: ${avg_daily:>7,.2f}")

# Quarterly Analysis
print("\n📊 QUARTERLY PERFORMANCE:")
for quarter in sorted(df['Quarter'].unique()):
    quarter_data = df[df['Quarter']==quarter]
    count = len(quarter_data)
    revenue = quarter_data['money'].sum()
    print(f"   Q{quarter} 2024: {count:>4} transactions - Revenue: ${revenue:>8,.2f}")

# ============================================================================
# CREATE VISUALIZATIONS
# ============================================================================
print("\n[5] Creating visualizations...")

# 1. Revenue Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df['money'], bins=30, edgecolor='black', alpha=0.7, color='skyblue')
plt.axvline(df['money'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${df["money"].mean():.2f}')
plt.axvline(df['money'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: ${df["money"].median():.2f}')
plt.xlabel('Transaction Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Transaction Amounts', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/01_revenue_distribution.png', dpi=300, bbox_inches='tight')
print("   ✓ Revenue distribution histogram saved")

# 2. Product Sales Bar Chart
plt.figure(figsize=(12, 6))
product_counts = df['coffee_name'].value_counts()
bars = plt.bar(range(len(product_counts)), product_counts.values, color='coral', edgecolor='black')
plt.xticks(range(len(product_counts)), product_counts.index, rotation=45, ha='right')
plt.xlabel('Coffee Product', fontsize=12)
plt.ylabel('Number of Sales', fontsize=12)
plt.title('Product Sales Distribution', fontsize=14, fontweight='bold')
# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/02_product_sales_bar.png', dpi=300, bbox_inches='tight')
print("   ✓ Product sales bar chart saved")

# 3. Hourly Sales Pattern
plt.figure(figsize=(12, 6))
hourly_sales = df.groupby('hour_of_day')['money'].agg(['sum', 'count'])
plt.subplot(1, 2, 1)
plt.bar(hourly_sales.index, hourly_sales['count'], color='steelblue', edgecolor='black')
plt.xlabel('Hour of Day', fontsize=11)
plt.ylabel('Number of Transactions', fontsize=11)
plt.title('Transaction Count by Hour', fontsize=12, fontweight='bold')
plt.grid(alpha=0.3)

plt.subplot(1, 2, 2)
plt.bar(hourly_sales.index, hourly_sales['sum'], color='green', edgecolor='black')
plt.xlabel('Hour of Day', fontsize=11)
plt.ylabel('Revenue ($)', fontsize=11)
plt.title('Revenue by Hour', fontsize=12, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/03_hourly_patterns.png', dpi=300, bbox_inches='tight')
print("   ✓ Hourly sales pattern saved")

# 4. Weekday Performance
plt.figure(figsize=(10, 6))
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekday_revenue = [df[df['Weekday']==day]['money'].sum() for day in weekday_order]
colors = ['#1f77b4']*5 + ['#ff7f0e']*2  # Blue for weekdays, orange for weekend
plt.bar(weekday_order, weekday_revenue, color=colors, edgecolor='black')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.title('Revenue by Day of Week', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/04_weekday_revenue.png', dpi=300, bbox_inches='tight')
print("   ✓ Weekday revenue chart saved")

# 5. Time of Day Pie Chart
plt.figure(figsize=(10, 8))
time_revenue = df.groupby('Time_of_Day')['money'].sum()
colors_pie = ['#FFD700', '#FF6B6B', '#4ECDC4']
plt.pie(time_revenue.values, labels=time_revenue.index, autopct='%1.1f%%',
        startangle=90, colors=colors_pie, textprops={'fontsize': 12})
plt.title('Revenue Distribution by Time of Day', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/task2/charts/05_time_of_day_pie.png', dpi=300, bbox_inches='tight')
print("   ✓ Time of day pie chart saved")

print("\n" + "="*80)
print("✓ DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS COMPLETE!")
print("="*80)
print(f"\nKey Findings:")
print(f"  • Most popular product: {df['coffee_name'].mode()[0]}")
print(f"  • Peak hour: {df['hour_of_day'].mode()[0]}:00")
print(f"  • Busiest day: {df['Weekday'].mode()[0]}")
print(f"  • Average transaction: ${df['money'].mean():.2f}")
print(f"  • Total revenue: ${df['money'].sum():,.2f}")
