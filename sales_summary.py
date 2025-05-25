import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_database():
    """Connect to the SQLite database"""
    try:
        conn = sqlite3.connect('sales_data.db')
        print("Successfully connected to the database.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def run_sales_queries(conn):
    """Run SQL queries and return results as DataFrames"""
    # Query 1: Total quantity and revenue by product
    query1 = """
    SELECT 
        product, 
        SUM(quantity) AS total_quantity, 
        SUM(quantity * price) AS total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
    """
    
    # Query 2: Overall summary
    query2 = """
    SELECT 
        COUNT(DISTINCT product) AS num_products,
        SUM(quantity) AS total_units_sold,
        SUM(quantity * price) AS overall_revenue
    FROM sales
    """
    
    # Execute queries and create DataFrames
    df1 = pd.read_sql_query(query1, conn)
    df2 = pd.read_sql_query(query2, conn)
    
    return df1, df2

def display_results(df1, df2):
    """Display the query results"""
    print("\n=== Sales by Product ===")
    print(df1.to_string(index=False))
    
    print("\n=== Overall Sales Summary ===")
    print(f"Number of products sold: {df2.iloc[0]['num_products']}")
    print(f"Total units sold: {df2.iloc[0]['total_units_sold']}")
    print(f"Total revenue: ${df2.iloc[0]['overall_revenue']:,.2f}")

def plot_sales_data(df):
    """Create a bar chart of sales by product"""
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', x='product', y='total_revenue', legend=False)
    plt.title('Total Revenue by Product')
    plt.ylabel('Revenue ($)')
    plt.xlabel('Product')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save and show the plot
    plt.savefig('sales_chart.png')
    print("\nSales chart saved as 'sales_chart.png'")
    plt.show()

def main():
    """Main function to run the sales summary"""
    # Connect to database
    conn = connect_to_database()
    if not conn:
        return
    
    # Run queries
    sales_by_product, overall_summary = run_sales_queries(conn)
    
    # Display results
    display_results(sales_by_product, overall_summary)
    
    # Plot the data
    plot_sales_data(sales_by_product)
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()