import csv
from datetime import datetime

class GoldTracker:
    def __init__(self, csv_file_path):
        self.csv_file = csv_file_path
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.transactions = list(reader)
        except FileNotFoundError:
            # Create the CSV file if it doesn't exist
            self.save_data()

    def save_data(self):
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['ID', 'Date', 'Putted Money', 'Buying Money', 'Selling Money', 'Buy Price', 'Actual Price', 'Sell Price', 'Weight (g)', 'Karat']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)

    def add_transaction(self, putted_money, buying_money, buy_price, actual_price, sell_price_per_gram, weight, karat):
        transaction_id = len(self.transactions) + 1
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_transaction = {
            'ID': transaction_id,
            'Date': date,
            'Putted Money': putted_money,
            'Buying Money': buying_money,
            'Selling Money': None,
            'Buy Price': buy_price,
            'Actual Price': actual_price,
            'Sell Price': sell_price_per_gram,
            'Weight (g)': weight,
            'Karat': karat
        }

        self.transactions.append(new_transaction)
        self.save_data()

    def put_money(self, putted_money):
        transaction_id = len(self.transactions) + 1
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_transaction = {
            'ID': transaction_id,
            'Date': date,
            'Putted Money': putted_money,
            'Buying Money': None,
            'Selling Money': None,
            'Buy Price': None,
            'Actual Price': None,
            'Sell Price': None,
            'Weight (g)': None,
            'Karat': None
        }

        self.transactions.append(new_transaction)
        self.save_data()

    def sell_transaction(self, transaction_id, sell_price_per_gram, sell_price):
        for transaction in self.transactions:
            if int(transaction['ID']) == transaction_id:
                transaction['Selling Money'] = sell_price
                transaction['Sell Price'] = sell_price_per_gram
                self.save_data()
                break

    def calculate_totals(self):
        putted_money_total = sum(float(transaction['Putted Money']) if transaction['Putted Money'] and transaction['Putted Money'].strip() else 0 for transaction in self.transactions)
        buying_money_total = sum(float(transaction['Buying Money']) if transaction['Buying Money'] and transaction['Buying Money'].strip() else 0 for transaction in self.transactions)
        profit_money_total = sum(float(transaction['Selling Money']) if transaction['Selling Money'] is not None else 0 for transaction in self.transactions)

        return putted_money_total, buying_money_total, profit_money_total


# Example usage:
csv_file_path = r'C:\Users\shiko\Desktop\Gold.csv'  # Replace with your file path
gold_tracker = GoldTracker(csv_file_path)

while True:
    choice = input("Do you want to put money, buy, sell, or exit? Enter 'put', 'buy', 'sell', or 'exit': ").lower()

    if choice == 'exit':
        break
    elif choice == 'put':
        putted_money = float(input("Enter Putted Money: $"))
        gold_tracker.put_money(putted_money)
    elif choice == 'buy':
        # No input for putted money in the 'buy' branch
        buying_money = float(input("Enter Buying Money: $"))
        buy_price = float(input("Enter Buy Price per gram: $"))
        actual_price = float(input("Enter Actual Price per gram: $"))
        sell_price_per_gram = None
        weight = float(input("Enter Weight (g): "))
        karat = int(input("Enter Karat (18/21/24): "))

        gold_tracker.add_transaction(None, buying_money, buy_price, actual_price, sell_price_per_gram, weight, karat)
    elif choice == 'sell':
        transaction_id = int(input("Enter Transaction ID to sell: "))
        sell_price_per_gram = float(input("Enter Sell Price per gram: $"))
        sell_price = float(input("Enter Selling Price: $"))

        gold_tracker.sell_transaction(transaction_id, sell_price_per_gram, sell_price)

# Calculate totals
putted_total, buying_total, profit_total = gold_tracker.calculate_totals()
print(f"\nTotal Putted Money: ${putted_total}")
print(f"Total Buying Money: ${buying_total}")
print(f"Total Profit Money: ${profit_total}")
