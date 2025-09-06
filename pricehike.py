import pandas as pd

# Sample dataset
data = {
    'Product': ['Soap', 'Shampoo', 'Rice Bag', 'Milk', 'Chocolate'],
    'Printed_Price': [40, 120, 500, 50, 30],   # MRP
    'Sold_Price': [45, 115, 520, 50, 35]       # Actual selling price
}

df = pd.DataFrame(data)

# Check if sold price is greater than printed price
df['Overpriced'] = df['Sold_Price'] > df['Printed_Price']

# Show products sold at higher price
overpriced_products = df[df['Overpriced'] == True]

print("Full Dataset:\n", df)
print("\nProducts sold above printed price:\n", overpriced_products)
