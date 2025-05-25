
Sales Analysis with SQLite and Python:

Project Structure

├── create_database.py      # Script to create and populate the database
├── sales_summary.py        # Main analysis script


Prerequisites:

- Python 3.6+
- VS Code (or any Python IDE)
- Required Python packages:
  - pandas
  - matplotlib
  - sqlite3 (built into Python)

Installation:

1. Clone this repository or create the files manually in VS Code
2. Install required packages:

```bash
pip install pandas matplotlib
```

How to Use:

1. First, run the database creation script:
```bash
python create_database.py
```
This will create `sales_data.db` with sample sales data.

2. Then run the analysis script:
```bash
python sales_summary.py
```

Expected Output:

The script will:
1. Print sales summary to the console:
   - Sales by product (product, total quantity, total revenue)
   - Overall summary (number of products, total units sold, total revenue)
2. Display a bar chart of revenue by product
3. Save the chart as `sales_chart.png`

Sample Output:

Successfully connected to the database.

=== Sales by Product ===
    product  total_quantity  total_revenue
     Phone             17       11899.83
    Laptop              8        7999.92
    Tablet             12        4199.88
Headphones             25        2499.75

=== Overall Sales Summary ===
Number of products sold: 4
Total units sold: 62
Total revenue: $26,599.38

Sales chart saved as 'sales_chart.png'

Customizing the Project:

To use your own data:
1. Modify the sample data in `create_database.py`
2. Or create your own SQLite database with a table named "sales" containing:
   - product (TEXT)
   - quantity (INTEGER)
   - price (REAL)
   - sale_date (TEXT)

 Dependencies:

- pandas - for data manipulation
- matplotlib - for visualization
- sqlite3 - for database operations (Python built-in)

