

================================================================================
SQL QUERIES FOR BUSINESS INTELLIGENCE
================================================================================

QUESTION 1: What are the top 5 products by revenue in the last 6 months?
--------------------------------------------------------------------------------
SELECT 
    coffee_name,
    COUNT(*) as total_sales,
    ROUND(SUM(money), 2) as total_revenue,
    ROUND(AVG(money), 2) as avg_price,
    ROUND(SUM(money) * 100.0 / (SELECT SUM(money) FROM coffee_sales), 2) as revenue_percentage
FROM coffee_sales
WHERE Date >= DATE('now', '-6 months')
GROUP BY coffee_name
ORDER BY total_revenue DESC
LIMIT 5;


QUESTION 2: What is the monthly user acquisition trend?
--------------------------------------------------------------------------------
SELECT 
    strftime('%Y-%m', Date) as year_month,
    Month_name,
    COUNT(DISTINCT Date) as active_days,
    COUNT(*) as total_transactions,
    ROUND(SUM(money), 2) as monthly_revenue,
    ROUND(AVG(money), 2) as avg_transaction_value,
    ROUND(SUM(money) / COUNT(DISTINCT Date), 2) as avg_daily_revenue
FROM coffee_sales
GROUP BY year_month, Month_name
ORDER BY year_month;


QUESTION 3: Which hour of the day generates the highest revenue?
--------------------------------------------------------------------------------
SELECT 
    hour_of_day,
    Hour_Category,
    COUNT(*) as transaction_count,
    ROUND(SUM(money), 2) as total_revenue,
    ROUND(AVG(money), 2) as avg_transaction,
    ROUND(SUM(money) * 100.0 / (SELECT SUM(money) FROM coffee_sales), 2) as revenue_pct
FROM coffee_sales
GROUP BY hour_of_day, Hour_Category
ORDER BY total_revenue DESC
LIMIT 1;


QUESTION 4: What is the weekend vs weekday revenue comparison?
--------------------------------------------------------------------------------
SELECT 
    CASE 
        WHEN Is_Weekend = 1 THEN 'Weekend'
        ELSE 'Weekday'
    END as day_type,
    COUNT(*) as total_transactions,
    ROUND(SUM(money), 2) as total_revenue,
    ROUND(AVG(money), 2) as avg_transaction,
    ROUND(SUM(money) / COUNT(DISTINCT Date), 2) as avg_daily_revenue
FROM coffee_sales
GROUP BY Is_Weekend
ORDER BY total_revenue DESC;


QUESTION 5: Which products are most popular during morning hours?
--------------------------------------------------------------------------------
SELECT 
    coffee_name,
    Product_Category,
    COUNT(*) as morning_sales,
    ROUND(SUM(money), 2) as morning_revenue,
    ROUND(AVG(money), 2) as avg_price,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM coffee_sales WHERE Time_of_Day = 'Morning'), 2) as pct_of_morning_sales
FROM coffee_sales
WHERE Time_of_Day = 'Morning'
GROUP BY coffee_name, Product_Category
ORDER BY morning_sales DESC
LIMIT 5;


QUESTION 6: What is the revenue trend by quarter?
--------------------------------------------------------------------------------
SELECT 
    Year,
    Quarter,
    COUNT(*) as total_transactions,
    ROUND(SUM(money), 2) as quarterly_revenue,
    ROUND(AVG(money), 2) as avg_transaction,
    COUNT(DISTINCT Date) as active_days,
    ROUND(SUM(money) / COUNT(DISTINCT Date), 2) as avg_daily_revenue
FROM coffee_sales
GROUP BY Year, Quarter
ORDER BY Year, Quarter;


QUESTION 7: Which day of the week has the highest average transaction value?
--------------------------------------------------------------------------------
SELECT 
    Weekday,
    Weekdaysort,
    COUNT(*) as total_transactions,
    ROUND(SUM(money), 2) as total_revenue,
    ROUND(AVG(money), 2) as avg_transaction_value,
    ROUND(MIN(money), 2) as min_transaction,
    ROUND(MAX(money), 2) as max_transaction
FROM coffee_sales
GROUP BY Weekday, Weekdaysort
ORDER BY avg_transaction_value DESC;


QUESTION 8: What are the top 3 product categories by sales volume?
--------------------------------------------------------------------------------
SELECT 
    Product_Category,
    COUNT(*) as total_units_sold,
    COUNT(DISTINCT coffee_name) as product_varieties,
    ROUND(SUM(money), 2) as total_revenue,
    ROUND(AVG(money), 2) as avg_price,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM coffee_sales), 2) as volume_percentage
FROM coffee_sales
GROUP BY Product_Category
ORDER BY total_units_sold DESC
LIMIT 3;


QUESTION 9: What is the hourly sales distribution for weekdays vs weekends?
--------------------------------------------------------------------------------
SELECT 
    hour_of_day,
    CASE WHEN Is_Weekend = 1 THEN 'Weekend' ELSE 'Weekday' END as day_type,
    COUNT(*) as transaction_count,
    ROUND(SUM(money), 2) as revenue,
    ROUND(AVG(money), 2) as avg_transaction
FROM coffee_sales
GROUP BY hour_of_day, Is_Weekend
ORDER BY day_type, hour_of_day;


QUESTION 10: Which month showed the highest growth rate compared to previous month?
--------------------------------------------------------------------------------
WITH monthly_revenue AS (
    SELECT 
        strftime('%Y-%m', Date) as year_month,
        Month_name,
        Monthsort,
        ROUND(SUM(money), 2) as monthly_revenue
    FROM coffee_sales
    GROUP BY year_month, Month_name, Monthsort
),
growth_calc AS (
    SELECT 
        year_month,
        Month_name,
        monthly_revenue,
        LAG(monthly_revenue) OVER (ORDER BY year_month) as prev_month_revenue,
        ROUND(
            (monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY year_month)) * 100.0 / 
            LAG(monthly_revenue) OVER (ORDER BY year_month), 
        2) as growth_rate
    FROM monthly_revenue
)
SELECT * FROM growth_calc
WHERE prev_month_revenue IS NOT NULL
ORDER BY growth_rate DESC
LIMIT 1;


QUESTION 11: What is the price category distribution across different times of day?
--------------------------------------------------------------------------------
SELECT 
    Time_of_Day,
    Price_Category,
    COUNT(*) as transaction_count,
    ROUND(SUM(money), 2) as revenue,
    ROUND(AVG(money), 2) as avg_transaction,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Time_of_Day), 2) as pct_within_timeperiod
FROM coffee_sales
GROUP BY Time_of_Day, Price_Category
ORDER BY Time_of_Day, transaction_count DESC;


QUESTION 12: Which products have consistent sales across all days of the week?
--------------------------------------------------------------------------------
SELECT 
    coffee_name,
    COUNT(DISTINCT Weekday) as days_sold,
    COUNT(*) as total_sales,
    ROUND(AVG(daily_sales), 2) as avg_daily_sales,
    ROUND(STDEV(daily_sales), 2) as sales_volatility
FROM (
    SELECT 
        coffee_name,
        Weekday,
        COUNT(*) as daily_sales
    FROM coffee_sales
    GROUP BY coffee_name, Weekday
) daily_product_sales
GROUP BY coffee_name
HAVING days_sold = 7
ORDER BY sales_volatility ASC;


QUESTION 13: What percentage of revenue comes from premium products?
--------------------------------------------------------------------------------
SELECT 
    Price_Category,
    COUNT(*) as transaction_count,
    ROUND(SUM(money), 2) as category_revenue,
    ROUND(SUM(money) * 100.0 / (SELECT SUM(money) FROM coffee_sales), 2) as revenue_percentage,
    ROUND(AVG(money), 2) as avg_transaction_value
FROM coffee_sales
GROUP BY Price_Category
ORDER BY category_revenue DESC;


QUESTION 14: What are the peak sales hours for each product category?
--------------------------------------------------------------------------------
WITH category_hourly AS (
    SELECT 
        Product_Category,
        hour_of_day,
        COUNT(*) as hourly_sales,
        ROUND(SUM(money), 2) as hourly_revenue,
        ROW_NUMBER() OVER (PARTITION BY Product_Category ORDER BY COUNT(*) DESC) as rank
    FROM coffee_sales
    GROUP BY Product_Category, hour_of_day
)
SELECT 
    Product_Category,
    hour_of_day as peak_hour,
    hourly_sales,
    hourly_revenue
FROM category_hourly
WHERE rank = 1
ORDER BY hourly_sales DESC;


QUESTION 15: What is the average transaction value by month and year?
--------------------------------------------------------------------------------
SELECT 
    Year,
    Month_name,
    Monthsort,
    COUNT(*) as total_transactions,
    ROUND(SUM(money), 2) as monthly_revenue,
    ROUND(AVG(money), 2) as avg_transaction_value,
    ROUND(MIN(money), 2) as min_transaction,
    ROUND(MAX(money), 2) as max_transaction,
    ROUND(STDEV(money), 2) as transaction_volatility
FROM coffee_sales
GROUP BY Year, Month_name, Monthsort
ORDER BY Year, Monthsort;

================================================================================
END OF SQL QUERIES
================================================================================

NOTES:
------
1. All queries are optimized for performance with appropriate GROUP BY and ORDER BY
2. Queries use aggregation functions (COUNT, SUM, AVG) for business metrics
3. Window functions (LAG, ROW_NUMBER) used for advanced analysis
4. Percentage calculations normalized to total revenue for context
5. Queries focus on filtering, aggregation, and multi-table joins logic

USAGE:
------
- These queries can be executed in SQLite, PostgreSQL, or MySQL with minor syntax adjustments
- Replace 'coffee_sales' with your actual table name
- Ensure Date column is in proper date format
- Index recommendations: (Date), (coffee_name), (hour_of_day), (Product_Category)

