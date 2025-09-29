stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800,
    "AMZN": 3500
}

portfolio = {}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue
    quantity = int(input(f"Enter number of shares for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

total_value = 0
print("\n Your Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\n Total Investment Value: ${total_value}")

save = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio:\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
    print(" Portfolio saved to portfolio.txt")