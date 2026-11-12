import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
file_path = "Consumer_Complaints.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(file_path, sheet_name=xls.sheet_names[0])
sns.set_theme(style="whitegrid")

print("--- 1. DATASET OVERVIEW ---")
print(f"Total Complaints Analyzed: {len(df):,}")

# 2. Analysis: Seasonal Patterns
df['Month_Name'] = df['Date submitted'].dt.strftime('%B')
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
monthly_counts = df['Month_Name'].value_counts().reindex(months_order)

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, marker='o', linewidth=2.5, color='#2b5c8f')
plt.title('Monthly Consumer Complaints (Seasonality)', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Complaints', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_1_seasonality.png', dpi=300)
plt.close()

# 3. Analysis: Top Products & Issues
top_products = df['Product'].value_counts().head(5)
top_product_name = top_products.index[0]
top_issues = df[df['Product'] == top_product_name]['Issue'].value_counts().head(3)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 5 Most Complained Products', fontsize=14, fontweight='bold')
plt.xlabel('Number of Complaints', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.savefig('chart_2_products.png', dpi=300)
plt.close()

# 4. Analysis: Resolutions
resolutions = df['Company response to consumer'].value_counts()
plt.figure(figsize=(9, 5))
sns.barplot(x=resolutions.values, y=resolutions.index, palette='Blues_r')
plt.title('How Complaints Are Resolved', fontsize=14, fontweight='bold')
plt.xlabel('Number of Complaints', fontsize=12)
plt.ylabel('Resolution Type', fontsize=12)
plt.tight_layout()
plt.savefig('chart_3_resolutions.png', dpi=300)
plt.close()

# 5. Analysis: Untimely Responses
untimely = df[df['Timely response?'] == 'No']
untimely_products = untimely['Product'].value_counts().head(5)

plt.figure(figsize=(10, 5))
sns.barplot(x=untimely_products.values, y=untimely_products.index, palette='Reds_r')
plt.title('Top 5 Products with Untimely Responses', fontsize=14, fontweight='bold')
plt.xlabel('Untimely Complaints', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.savefig('chart_4_untimely.png', dpi=300)
plt.close()

print("\nAll 4 charts have been successfully generated and saved as PNG files!")
