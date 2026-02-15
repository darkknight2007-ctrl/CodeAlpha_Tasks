STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.25,
    "MSFT": 375.00,
    "AMZN": 155.80,
    "NVDA": 495.25,
    "META": 485.30
}

def display_available_stocks():
    print("\n" + "=" * 50)
    print("AVAILABLE STOCKS")
    print("=" * 50)
    print(f"{'Stock':<10}{'Price ($)':<15}")
    print("-" * 50)

    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10}${price:<14.2f}")

    print("=" * 50 + "\n")


def get_portfolio():
    portfolio = {}

    print("Enter your stock holdings (type 'done' to finish)")

    while True:
        stock = input("\nEnter stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(" Stock not available. Choose from listed stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print(" Quantity must be positive.")
                continue

            # Pythonic update
            portfolio[stock] = portfolio.get(stock, 0) + quantity
            print(f"{stock} holding updated to {portfolio[stock]} shares")

        except ValueError:
            print(" Please enter a valid whole number.")

    return portfolio


def calculate_portfolio_value(portfolio):
    total_value = sum(
        quantity * STOCK_PRICES[stock]
        for stock, quantity in portfolio.items()
    )

    print("\n" + "=" * 80)
    print("PORTFOLIO SUMMARY")
    print("=" * 80)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<15}{'Value':<15}{'Allocation':<12}")
    print("-" * 80)

    stock_details = []

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = quantity * price
        allocation = (value / total_value) * 100

        print(f"{stock:<10}{quantity:<8}${price:<14.2f}${value:<14.2f}{allocation:.2f}%")

        stock_details.append({
            "stock": stock,
            "quantity": quantity,
            "price": price,
            "value": value,
            "allocation": allocation
        })

    print("-" * 80)
    print(f"{'TOTAL PORTFOLIO VALUE:':<48}${total_value:,.2f}")
    print("=" * 80 + "\n")

    return total_value, stock_details


def save_to_file(stock_details, total_value, file_format="txt"):
    filename = f"portfolio_summary.{file_format}"

    if file_format == "txt":
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n\n")
            f.write(f"{'Stock':<10}{'Qty':<8}{'Price':<15}{'Value':<15}{'Allocation':<12}\n")
            f.write("-" * 80 + "\n")

            for d in stock_details:
                f.write(f"{d['stock']:<10}{d['quantity']:<8}"
                        f"${d['price']:<14.2f}${d['value']:<14.2f}"
                        f"{d['allocation']:.2f}%\n")

            f.write("-" * 80 + "\n")
            f.write(f"TOTAL VALUE: ${total_value:,.2f}\n")

    elif file_format == "csv":
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value,Allocation(%)\n")
            for d in stock_details:
                f.write(f"{d['stock']},{d['quantity']},"
                        f"{d['price']:.2f},{d['value']:.2f},"
                        f"{d['allocation']:.2f}\n")

            f.write(f"TOTAL,,,{total_value:.2f},\n")

    print(f" Portfolio saved as {filename}")


def main():
    print("\n" + "*" * 35)
    print("     STOCK PORTFOLIO TRACKER")
    print("*" * 35)

    display_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\n No stocks added.")
        return

    total_value, stock_details = calculate_portfolio_value(portfolio)

    save_choice = input("Save portfolio (yes/no): ").lower().strip()

    if save_choice in ("yes", "y"):
        format_choice = input("Choose format (txt/csv): ").lower().strip()
        if format_choice not in ("txt", "csv"):
            format_choice = "txt"
        save_to_file(stock_details, total_value, format_choice)

if __name__ == "__main__":
    while True:
        main()
        again = input("Run again? (yes/no): ").lower().strip()
        if again not in ("yes", "y"):
            print("\n✓ Exiting program....\n")
            break
