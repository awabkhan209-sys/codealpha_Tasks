stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

stock = input("Stock ka naam likho: ").upper()
quantity = int(input("Quantity likho: "))

total = stock_prices[stock] * quantity

print("Total investment:", total)

with open("portfolio.txt", "w") as file:
    file.write("Stock: " + stock + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: " + str(total))
