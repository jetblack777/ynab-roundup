# YNAB Round Up Savings & Invest

**YNAB RoundUp Savings & Invest** is a Python tool designed to help you save or invest your spare change by rounding up your transactions in YNAB (You Need A Budget) to the nearest dollar. It calculates the difference between each transaction and the next dollar, allowing you to easily boost your savings or investments.

## Features
- **Seamless YNAB Integration:** Automatically pulls transactions from YNAB using your API key.
- **Rounds Up Debits Only:** Focuses on expenses, excluding credits (income) and transfers.
- **Simple Summary:** Provides the total roundup amount for saving or investing.

## Requirements
- Python 3.x
- A YNAB account
- YNAB API key

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/jetblack777/ynab-roundup.git
    cd ynab-roundup
    ```

2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

3. Create a `key.txt` file in the project directory and add your YNAB API key:
    ```
    YOUR_YNAB_API_KEY
    ```
    > You can find your API key in your YNAB account under **Account Settings > Developer Settings**. Make sure to keep this key safe and keep it private!

## Usage

1. Open the terminal and navigate to the project directory:
    ```bash
    cd ynab-roundup
    ```

2. Run the script to fetch and process your YNAB transactions:
    ```bash
    python ynab_roundup.py
    ```

3. The script will:
    - Fetch all your debit transactions from the last 30 days (or a user defined amount).
    - Exclude any transfers or credits.
    - Round up each debit transaction to the nearest dollar.
    - Calculate the total roundup amount.
    - Output the total savings/investment potential to the terminal.

### How it works

1. The script reads the YNAB API key from `key.txt`.
2. It fetches transactions from the last 30 days (or user specified amount) using the YNAB API.
3. For each transaction that is a debit (negative amount) and not a transfer:
   - It calculates the difference between the transaction amount and its rounded-up value.
   - This difference is added to the total roundup amount.
4. The script prints the total roundup amount for the period.

## Customization

- You can modify the `days` variable to change the time period for fetching transactions.
- Uncomment the debug print statements in the `calculate_roundup_amount` function to see detailed information for each transaction.

## Note

This script uses the "last-used" budget in your YNAB account. If you want to specify a different budget, modify the `budget_id` variable in the `fetch_transactions` function.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/jetblack777/ynab-roundup/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer

**YNAB Round Up Savings & Invest** is a tool designed to assist with rounding up YNAB transactions to the nearest dollar for saving or investing purposes. While the tool aims to provide accurate and useful information, the following disclaimers apply:

1. **Accuracy of Data**: The tool relies on data retrieved from the YNAB API. While efforts are made to ensure the accuracy of the data processed, there is no guarantee that the information will be completely accurate or up-to-date. Always verify the results independently.

2. **Financial Advice**: This tool does not provide financial advice or recommendations. The calculations and roundups performed by the script are purely for informational purposes and should not be construed as financial guidance. Consult a financial advisor for personalized advice.

3. **Data Security**: Your YNAB API key is used to access transaction data. Ensure that your API key and the `key.txt` file is kept secure and private. The developers of this tool are not responsible for any unauthorized access or misuse of your API key.

4. **Liability**: The developers of this tool are not liable for any direct, indirect, incidental, or consequential damages arising from the use or inability to use the tool, including but not limited to financial losses or inaccuracies in transaction data.

5. **Use at Your Own Risk**: By using this tool, you acknowledge and accept that you are solely responsible for any actions taken based on the information provided. Use the tool at your own risk.

6. **Updates and Maintenance**: The tool may be updated or modified over time. While efforts will be made to maintain its functionality, there is no guarantee of continuous support or updates.

---

