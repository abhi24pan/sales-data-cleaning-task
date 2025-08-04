import pandas as pd

# Load the raw sales dataset
df = pd.read_csv("sales_data_200_raw.csv")

# 1. Handle missing values
df['Region'].fillna('Unknown', inplace=True)
df['Sales Rep'].fillna('Unknown', inplace=True)
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)

# Recalculate total price after filling missing quantity
df['Total Price'] = df['Quantity'] * df['Unit Price']

# 2. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 3. Standardize text values
df['Region'] = df['Region'].str.strip().str.title()
df['Sales Rep'] = df['Sales Rep'].str.strip().str.title()

# 4. Convert 'Order Date' to consistent datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=True)

# 5. Rename columns (lowercase and replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 6. Fix data types
df['quantity'] = df['quantity'].astype(int)
df['unit_price'] = df['unit_price'].astype(float)
df['total_price'] = df['total_price'].astype(float)

# 7. Save the cleaned dataset
df.to_csv("sales_data_200_cleaned.csv", index=False)

print("✅ Sales data cleaned and saved as 'sales_data_200_cleaned.csv'")
