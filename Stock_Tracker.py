# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

# User input
num_stocks = int(input("How many stocks do you want to add? "))

for i in range(num_stocks):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity

        investment = stock_prices[stock] * quantity
        total_investment += investment

    else:
        print("Stock not found!")

# Display portfolio
print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(stock, ":", quantity, "shares =", value)

print("\nTotal Investment Value: $", total_investment)

# Optional file saving
save = input("\nSave result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares = ${value}\n")

        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("Portfolio saved as portfolio.txt")
