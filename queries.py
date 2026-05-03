def avg_price_by_city():
    return """
    SELECT City, AVG(Price) as Avg_Price
    FROM listings
    GROUP BY City
    """

def sales_trend():
    return """
    SELECT strftime('%Y-%m', Sale_Date) as Month,
           COUNT(*) as Sales
    FROM sales
    GROUP BY Month
    """

def property_type_distribution():
    return """
    SELECT Property_Type, COUNT(*) as Count
    FROM listings
    GROUP BY Property_Type
    """

def top_agents():
    return """
    SELECT Name, Deals_Closed
    FROM agents
    ORDER BY Deals_Closed DESC
    LIMIT 5
    """