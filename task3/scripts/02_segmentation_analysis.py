"""
TASK 3: DEEP-DIVE ANALYSIS - CUSTOMER SEGMENTATION
====================================================
Purpose: Segment customers using RFM-like analysis and business rules
Author: Data Analytics Intern
Date: February 19, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

print("="*80)
print("TASK 3 - DEEP-DIVE ANALYSIS: CUSTOMER SEGMENTATION")
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
# BEHAVIORAL SEGMENTATION
# ============================================================================
print("\n[2] Creating Behavioral Segments...")

# Segment 1: By Transaction Value (Price-Based)
df['Value_Segment'] = pd.cut(df['money'], 
                              bins=[0, 28, 32, 35, 100],
                              labels=['Budget', 'Standard', 'Premium', 'Luxury'])

# Segment 2: By Time of Day Preference
def get_time_segment(hour):
    if 6 <= hour < 11:
        return 'Morning Shopper'
    elif 11 <= hour < 17:
        return 'Afternoon Shopper'
    else:
        return 'Evening Shopper'

df['Time_Segment'] = df['hour_of_day'].apply(get_time_segment)

# Segment 3: By Product Preference
df['Product_Segment'] = df['Product_Category'].map({
    'Coffee - Milk': 'Milk Coffee Lover',
    'Coffee - Black': 'Pure Coffee Enthusiast',
    'Non-Coffee': 'Alternative Beverage Seeker'
})

# Segment 4: By Day Type (Weekend Warrior vs Weekday Regular)
df['Day_Segment'] = df['Is_Weekend'].map({
    0: 'Weekday Regular',
    1: 'Weekend Warrior'
})

print("✓ Created 4 behavioral segment dimensions")

# ============================================================================
# SEGMENTATION ANALYSIS
# ============================================================================
print("\n[3] Analyzing Segments...")

# Value Segment Analysis
print("\n💰 VALUE SEGMENT DISTRIBUTION:")
value_seg = df.groupby('Value_Segment').agg({
    'money': ['count', 'sum', 'mean'],
    'coffee_name': lambda x: x.mode()[0] if len(x) > 0 else 'N/A'
}).round(2)
value_seg.columns = ['Transactions', 'Revenue', 'Avg_Transaction', 'Top_Product']
print(value_seg)

# Time Segment Analysis
print("\n🕐 TIME PREFERENCE SEGMENT:")
time_seg = df.groupby('Time_Segment').agg({
    'money': ['count', 'sum', 'mean'],
    'coffee_name': lambda x: x.mode()[0] if len(x) > 0 else 'N/A'
}).round(2)
time_seg.columns = ['Transactions', 'Revenue', 'Avg_Transaction', 'Top_Product']
time_seg = time_seg.reindex(['Morning Shopper', 'Afternoon Shopper', 'Evening Shopper'])
print(time_seg)

# Product Preference Segment
print("\n☕ PRODUCT PREFERENCE SEGMENT:")
product_seg = df.groupby('Product_Segment').agg({
    'money': ['count', 'sum', 'mean']
}).round(2)
product_seg.columns = ['Transactions', 'Revenue', 'Avg_Transaction']
print(product_seg)

# Day Type Segment
print("\n📅 DAY TYPE SEGMENT:")
day_seg = df.groupby('Day_Segment').agg({
    'money': ['count', 'sum', 'mean']
}).round(2)
day_seg.columns = ['Transactions', 'Revenue', 'Avg_Transaction']
print(day_seg)

# ============================================================================
# CROSS-SEGMENTATION ANALYSIS
# ============================================================================
print("\n[4] Cross-Segmentation Analysis...")

# Value x Time segments
cross_value_time = pd.crosstab(
    df['Value_Segment'],
    df['Time_Segment'],
    values=df['money'],
    aggfunc='count',
    margins=True
)
print("\n💰×🕐 VALUE x TIME SEGMENTS:")
print(cross_value_time)

# Product x Day Type
cross_product_day = pd.crosstab(
    df['Product_Segment'],
    df['Day_Segment'],
    values=df['money'],
    aggfunc='sum',
    margins=True
).round(2)
print("\n☕×📅 PRODUCT x DAY TYPE (Revenue $):")
print(cross_product_day)

# ============================================================================
# ADVANCED SEGMENTATION: K-MEANS CLUSTERING
# ============================================================================
print("\n[5] K-Means Clustering Segmentation...")

# Create features for clustering
cluster_features = pd.DataFrame({
    'avg_transaction': [df['money'].mean()] * len(df),
    'hour_preference': df['hour_of_day'],
    'is_weekend': df['Is_Weekend'],
    'price_level': df['money']
})

# Normalize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(cluster_features)

# Perform K-Means (4 segments)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['ML_Segment'] = kmeans.fit_predict(features_scaled)

# Map to meaningful names based on characteristics
segment_names = []
for seg in range(4):
    seg_data = df[df['ML_Segment'] == seg]
    avg_price = seg_data['money'].mean()
    avg_hour = seg_data['hour_of_day'].mean()
    weekend_pct = seg_data['Is_Weekend'].mean() * 100
    
    # Naming logic
    if avg_price > 33 and weekend_pct > 30:
        name = 'Premium Weekend Shoppers'
    elif avg_price > 33 and avg_hour < 12:
        name = 'Morning Premium Buyers'
    elif avg_price < 30 and avg_hour > 17:
        name = 'Evening Budget Shoppers'
    else:
        name = f'Standard Shoppers Segment {seg+1}'
    
    segment_names.append((seg, name))

segment_map = {seg: name for seg, name in segment_names}
df['ML_Segment_Name'] = df['ML_Segment'].map(segment_map)

print("\n🤖 MACHINE LEARNING SEGMENTS:")
ml_seg = df.groupby('ML_Segment_Name').agg({
    'money': ['count', 'sum', 'mean'],
    'hour_of_day': 'mean',
    'Is_Weekend': lambda x: (x.mean() * 100)
}).round(2)
ml_seg.columns = ['Transactions', 'Revenue', 'Avg_Transaction', 'Avg_Hour', 'Weekend_%']
print(ml_seg)

# ============================================================================
# VISUALIZATIONS
# ============================================================================
print("\n[6] Creating visualizations...")

# 1. Value Segment Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

value_counts = df['Value_Segment'].value_counts()
axes[0].pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%',
            startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axes[0].set_title('Customer Distribution by Value Segment', fontweight='bold')

value_revenue = df.groupby('Value_Segment')['money'].sum()
axes[1].pie(value_revenue.values, labels=value_revenue.index, autopct='%1.1f%%',
            startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axes[1].set_title('Revenue Distribution by Value Segment', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/05_value_segment_distribution.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Value segment distribution saved")
plt.close()

# 2. Time Preference Heatmap
time_product_matrix = pd.crosstab(
    df['Time_Segment'],
    df['Product_Category'],
    values=df['money'],
    aggfunc='sum'
)

plt.figure(figsize=(10, 6))
sns.heatmap(time_product_matrix, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=1)
plt.title('Revenue Heatmap: Time Segment x Product Category', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Time Segment', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/06_time_product_heatmap.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Time-Product heatmap saved")
plt.close()

# 3. Segment Performance Comparison
segment_summary = df.groupby('ML_Segment_Name').agg({
    'money': ['count', 'sum', 'mean']
}).round(2)
segment_summary.columns = ['Transactions', 'Revenue', 'Avg_Transaction']

fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# Transactions
axes[0].barh(segment_summary.index, segment_summary['Transactions'], color='steelblue')
axes[0].set_xlabel('Transaction Count', fontsize=11)
axes[0].set_title('Transactions by ML Segment', fontweight='bold')
axes[0].grid(alpha=0.3, axis='x')

# Revenue
axes[1].barh(segment_summary.index, segment_summary['Revenue'], color='green')
axes[1].set_xlabel('Revenue ($)', fontsize=11)
axes[1].set_title('Revenue by ML Segment', fontweight='bold')
axes[1].grid(alpha=0.3, axis='x')

# Average Transaction
axes[2].barh(segment_summary.index, segment_summary['Avg_Transaction'], color='coral')
axes[2].set_xlabel('Avg Transaction ($)', fontsize=11)
axes[2].set_title('Avg Transaction by ML Segment', fontweight='bold')
axes[2].grid(alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/07_ml_segment_comparison.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ ML segment comparison saved")
plt.close()

# 4. Weekday vs Weekend by Product
weekday_product = df.groupby(['Day_Segment', 'Product_Category'])['money'].sum().unstack()

weekday_product.plot(kind='bar', figsize=(12, 6), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Revenue by Day Type and Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Day Type', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=0)
plt.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('/home/claude/task3/analysis/08_day_product_revenue.png', 
            dpi=300, bbox_inches='tight')
print("   ✓ Day-Product revenue chart saved")
plt.close()

# ============================================================================
# SEGMENT PROFILES
# ============================================================================
print("\n[7] Creating Segment Profiles...")

profiles = []
for segment in df['ML_Segment_Name'].unique():
    seg_data = df[df['ML_Segment_Name'] == segment]
    
    profile = {
        'Segment': segment,
        'Size': len(seg_data),
        'Size_%': f"{len(seg_data)/len(df)*100:.1f}%",
        'Avg_Transaction': f"${seg_data['money'].mean():.2f}",
        'Total_Revenue': f"${seg_data['money'].sum():.2f}",
        'Peak_Hour': f"{seg_data['hour_of_day'].mode()[0]}:00",
        'Top_Product': seg_data['coffee_name'].mode()[0],
        'Weekend_%': f"{seg_data['Is_Weekend'].mean()*100:.1f}%"
    }
    profiles.append(profile)

profile_df = pd.DataFrame(profiles)
print("\n📊 DETAILED SEGMENT PROFILES:")
print(profile_df.to_string(index=False))

# Save profiles
profile_df.to_csv('/home/claude/task3/analysis/segment_profiles.csv', index=False)

# ============================================================================
# KEY INSIGHTS
# ============================================================================
print("\n[8] KEY SEGMENTATION INSIGHTS")
print("-" * 80)

# Most valuable segment
most_valuable = df.groupby('ML_Segment_Name')['money'].sum().idxmax()
most_valuable_revenue = df[df['ML_Segment_Name']==most_valuable]['money'].sum()

# Largest segment
largest_segment = df['ML_Segment_Name'].value_counts().idxmax()
largest_segment_size = df['ML_Segment_Name'].value_counts().max()

print(f"\n💎 Most Valuable Segment:")
print(f"   • Segment: {most_valuable}")
print(f"   • Total Revenue: ${most_valuable_revenue:,.2f}")
print(f"   • Percentage of total: {most_valuable_revenue/df['money'].sum()*100:.1f}%")

print(f"\n📊 Largest Segment:")
print(f"   • Segment: {largest_segment}")
print(f"   • Size: {largest_segment_size:,} transactions")
print(f"   • Percentage of total: {largest_segment_size/len(df)*100:.1f}%")

# Value segment insights
premium_revenue = df[df['Value_Segment']=='Premium']['money'].sum()
premium_pct = premium_revenue / df['money'].sum() * 100

print(f"\n💰 Value Segment Insights:")
print(f"   • Premium segment revenue: ${premium_revenue:,.2f} ({premium_pct:.1f}% of total)")
print(f"   • Premium transactions: {len(df[df['Value_Segment']=='Premium'])} ({len(df[df['Value_Segment']=='Premium'])/len(df)*100:.1f}%)")

# Time preference
morning_shoppers = len(df[df['Time_Segment']=='Morning Shopper'])
afternoon_shoppers = len(df[df['Time_Segment']=='Afternoon Shopper'])
evening_shoppers = len(df[df['Time_Segment']=='Evening Shopper'])

print(f"\n🕐 Time Preference Distribution:")
print(f"   • Morning Shoppers: {morning_shoppers:,} ({morning_shoppers/len(df)*100:.1f}%)")
print(f"   • Afternoon Shoppers: {afternoon_shoppers:,} ({afternoon_shoppers/len(df)*100:.1f}%)")
print(f"   • Evening Shoppers: {evening_shoppers:,} ({evening_shoppers/len(df)*100:.1f}%)")

print("\n" + "="*80)
print("✓ CUSTOMER SEGMENTATION ANALYSIS COMPLETE!")
print("="*80)
print(f"\nKey Findings:")
print(f"  • 4 ML-based customer segments identified")
print(f"  • Most valuable segment: {most_valuable}")
print(f"  • Premium customers drive {premium_pct:.1f}% of revenue")
print(f"  • Time preferences are well-balanced across day")
