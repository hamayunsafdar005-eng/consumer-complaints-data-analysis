import pandas as pd

# 1. Load the dataset
file_path = "Consumer_Complaints.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(file_path, sheet_name=xls.sheet_names[0])

print("--- Dataset Overview ---")
print(f"Total rows: {len(df)}, Total columns: {len(df.columns)}")

# 2. Seasonal Patterns
df['Month_Name'] = df['Date submitted'].dt.strftime('%B')
monthly_counts = df['Month_Name'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])
print("\n--- Monthly Complaints (Seasonality) ---")
print(monthly_counts)

# 3. Top Products and Issues
top_products = df['Product'].value_counts()
print("\n--- Top 5 Products ---")
print(top_products.head(5))

top_product_name = top_products.index[0]
print(f"\nTop Issues for '{top_product_name}':")
print(df[df['Product'] == top_product_name]['Issue'].value_counts().head(5))

# 4. Typical Resolutions
print("\n--- Company Response to Consumer (Resolutions) ---")
print(df['Company response to consumer'].value_counts(normalize=True) * 100)

# 5. Untimely Responses Analysis
untimely = df[df['Timely response?'] == 'No']
print(f"\n--- Untimely Responses Insights ---")
print(f"Total Untimely: {len(untimely)} ({len(untimely)/len(df)*100:.2f}%)")
print("Top products with untimely responses:")
print(untimely['Product'].value_counts().head(3))