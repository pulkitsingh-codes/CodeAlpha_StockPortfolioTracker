# Simple Stock Portfolio Tracker

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 420
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, "-", stock_prices[stock])

# Ask how many stocks the user wants to enter
number = int(input("\nHow many stocks do you want to buy? "))

for i in range(number):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Please enter a valid quantity.")
            continue

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        print("Stock:", stock_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Investment:", investment)

    else:
        print("Stock not available!")

print("\n----------------------------")
print("Total Investment:", total_investment)
print("----------------------------")

# Save result in a text file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Report\n")
file.write("Total Investment: " + str(total_investment))

file.close()

print("\nPortfolio saved successfully!")