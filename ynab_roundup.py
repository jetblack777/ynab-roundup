import requests
import math
import datetime

# Read the API key from key.txt
with open('key.txt', 'r') as file:
    YNAB_API_KEY = file.read().strip()

# YNAB API endpoint and headers
base_url = "https://api.youneedabudget.com/v1"
headers = {"Authorization": f"Bearer {YNAB_API_KEY}"}

# Get today's date and the date for one month ago
today = datetime.date.today()
days = 90 #Modify this variable to change the amount of days you want to look back on
one_month_ago = today - datetime.timedelta(days=days) 

# Function to fetch transactions from the YNAB API for the past month
def fetch_transactions():
    budget_id = "last-used"  # Assuming we are using the last accessed budget, can be changed
    endpoint = f"{base_url}/budgets/{budget_id}/transactions"
    params = {"since_date": one_month_ago.isoformat()} 

    response = requests.get(endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()["data"]["transactions"]
    else:
        print("Failed to fetch transactions:", response.status_code, response.text)
        return []

# Function to calculate the sum of rounding differences (debits only, excluding transfers)
def calculate_roundup_amount(transactions, debug=False):
    total_roundup = 0
    
    for transaction in transactions:
        # Exclude transfers and process only debits (negative amounts)
        if transaction['amount'] < 0 and not transaction['transfer_account_id']:
            original_amount = abs(transaction['amount']) / 1000 
            rounded_amount = math.ceil(original_amount)
            roundup_amount = rounded_amount - original_amount
            total_roundup += roundup_amount

            
        """if debug:                                                           
                print(f"Transaction: {transaction['payee_name'] or 'Unknown'}")
                print(f"Original Amount: ${original_amount:.2f}")
                print(f"Rounded Amount: ${rounded_amount:.2f}")
                print(f"Roundup Difference: ${roundup_amount:.2f}")
                print("-" * 40) """
            
    return total_roundup

# Fetch the transactions and calculate the roundup amount with debug enabled
transactions = fetch_transactions()
total_roundup = calculate_roundup_amount(transactions, debug=True)

print(f"Total round up amount for the past {days} days: ${total_roundup:.2f}")
