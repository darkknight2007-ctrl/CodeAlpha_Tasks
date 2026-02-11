"""
Stock Portfolio Tracker
A simple program to track stock investments with hardcoded prices
"""

# Hardcoded stock prices (as of example date)
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
    """Display all available stocks and their prices"""
    print("\n" + "="*50)
    print("AVAILABLE STOCKS")
    print("="*50)
    print(f"{'Stock':<10} {'Price ($)':<15}")
    print("-"*50)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} ${price:<14.2f}")
    print("="*50 + "\n")

def get_portfolio():
    """Get user's portfolio input"""
    portfolio = {}
    
    print("Enter your stock holdings (type 'done' when finished)")
    print("Format: Enter stock symbol, then quantity")
    
    while True:
        # Get stock symbol
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock == 'DONE':
            break
        
        # Validate stock exists
        if stock not in STOCK_PRICES:
            print(f"❌ '{stock}' is not in our database. Please choose from available stocks.")
            continue
        
        # Get quantity
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive. Try again.")
                continue
            
            # Add or update portfolio
            if stock in portfolio:
                portfolio[stock] += quantity
                print(f"✓ Updated {stock} holding to {portfolio[stock]} shares")
            else:
                portfolio[stock] = quantity
                print(f"✓ Added {quantity} shares of {stock}")
                
        except ValueError:
            print("❌ Invalid quantity. Please enter a whole number.")
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """Calculate total value of portfolio"""
    total_value = 0
    stock_details = []
    
    print("\n" + "="*70)
    print("PORTFOLIO SUMMARY")
    print("="*70)
    print(f"{'Stock':<10} {'Quantity':<12} {'Price':<15} {'Total Value':<15}")
    print("-"*70)
    
    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = quantity * price
        total_value += value
        
        print(f"{stock:<10} {quantity:<12} ${price:<14.2f} ${value:<14.2f}")
        stock_details.append({
            'stock': stock,
            'quantity': quantity,
            'price': price,
            'value': value
        })
    
    print("-"*70)
    print(f"{'TOTAL PORTFOLIO VALUE:':<52} ${total_value:,.2f}")
    print("="*70 + "\n")
    
    return total_value, stock_details

def save_to_file(portfolio, total_value, stock_details, file_format='txt'):
    """Save portfolio to a file (txt or csv)"""
    
    if file_format == 'txt':
        filename = '/mnt/user-data/outputs/portfolio_summary.txt'
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"{'Stock':<10} {'Quantity':<12} {'Price':<15} {'Total Value':<15}\n")
            f.write("-"*70 + "\n")
            
            for detail in stock_details:
                f.write(f"{detail['stock']:<10} {detail['quantity']:<12} "
                       f"${detail['price']:<14.2f} ${detail['value']:<14.2f}\n")
            
            f.write("-"*70 + "\n")
            f.write(f"{'TOTAL PORTFOLIO VALUE:':<52} ${total_value:,.2f}\n")
            f.write("="*70 + "\n")
        
        print(f"✓ Portfolio saved to {filename}")
        
    elif file_format == 'csv':
        filename = '/mnt/user-data/outputs/portfolio_summary.csv'
        with open(filename, 'w') as f:
            # Write header
            f.write("Stock,Quantity,Price,Total Value\n")
            
            # Write data
            for detail in stock_details:
                f.write(f"{detail['stock']},{detail['quantity']},"
                       f"{detail['price']:.2f},{detail['value']:.2f}\n")
            
            # Write total
            f.write(f"TOTAL,,,{total_value:.2f}\n")
        
        print(f"✓ Portfolio saved to {filename}")

def main():
    """Main program function"""
    print("\n" + "🔹"*35)
    print("     STOCK PORTFOLIO TRACKER")
    print("🔹"*35)
    
    # Display available stocks
    display_available_stocks()
    
    # Get user portfolio
    portfolio = get_portfolio()
    
    # Check if portfolio is empty
    if not portfolio:
        print("\n⚠ No stocks added. Exiting program.")
        return
    
    # Calculate and display portfolio value
    total_value, stock_details = calculate_portfolio_value(portfolio)
    
    # Ask user if they want to save
    save_choice = input("\nWould you like to save this portfolio? (yes/no): ").lower().strip()
    
    if save_choice in ['yes', 'y']:
        format_choice = input("Choose format (txt/csv): ").lower().strip()
        
        if format_choice in ['txt', 'csv']:
            save_to_file(portfolio, total_value, stock_details, format_choice)
        else:
            print("Invalid format. Saving as txt by default.")
            save_to_file(portfolio, total_value, stock_details, 'txt')
    
    print("\n✓ Thank you for using Stock Portfolio Tracker!\n")

# Run the program
if __name__ == "__main__":
    main()
