import csv
import random
from datetime import datetime, timedelta

# Updated inventory data (item_id, item_name, initial_quantity)
inventory_data = [
    (1, 'Rice', 100),
    (2, 'Milk', 50),
    (3, 'Bread', 75),
    (4, 'Eggs', 60),
    (5, 'Bananas', 40),
    (6, 'Potatos', 80),
    (7, 'Redbull', 200),
    (8, 'Cadbury',120),
    # Add more items as needed
]

# Function to generate random transactions
def generate_transaction():
    item_id, _, initial_quantity = random.choice(inventory_data)
    transaction_type = random.choice(['Purchase', 'Sale'])
    quantity = random.randint(1, 20)

    # Calculate the new quantity based on the transaction type
    if transaction_type == 'Purchase':
        new_quantity = initial_quantity + quantity
    else:
        new_quantity = max(0, initial_quantity - quantity)

    # Generate a random date for the transaction within the last month
    transaction_date = datetime.now() - timedelta(days=random.randint(1, 30))

    return {
        'item_id': item_id,
        'item_name': inventory_data[item_id - 1][1],
        'transaction_type': transaction_type,
        'quantity': quantity,
        'transaction_date': transaction_date.strftime('%Y-%m-%d'),
        'initial_quantity': initial_quantity,
        'new_quantity': new_quantity,
    }

# Generate 100 transactions
transactions = [generate_transaction() for _ in range(800)]

# Write transactions to a CSV file
csv_file_path = 'inventory_transactions.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Transaction_ID', 'Date', 'Item_ID', 'Item_Name', 'Transaction_Type', 'Quantity', 'Initial_Quantity', 'New_Quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i, transaction in enumerate(transactions, 1):
        writer.writerow({
            'Transaction_ID': i,
            'Date': transaction['transaction_date'],
            'Item_ID': transaction['item_id'],
            'Item_Name': transaction['item_name'],
            'Transaction_Type': transaction['transaction_type'],
            'Quantity': transaction['quantity'],
            'Initial_Quantity': transaction['initial_quantity'],
            'New_Quantity': transaction['new_quantity'],
        })

print(f'Transactions written to {csv_file_path}')
