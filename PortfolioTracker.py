# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

total_investment = 0
portfolio = []

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in the price list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        portfolio.append({
            "stock": stock,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"{stock}: {quantity} × ${price} = ${investment}")

    except ValueError:
        print("Please enter a valid quantity.")

print("\n===== Portfolio Summary =====")

for item in portfolio:
    print(
        f"{item['stock']} - "
        f"Quantity: {item['quantity']}, "
        f"Price: ${item['price']}, "
        f"Value: ${item['investment']}"
    )

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save portfolio to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== Stock Portfolio Summary =====\n")

        for item in portfolio:
            file.write(
                f"{item['stock']} - "
                f"Quantity: {item['quantity']}, "
                f"Price: ${item['price']}, "
                f"Value: ${item['investment']}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")