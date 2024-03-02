price_input = input("Enter PS5 price: ")

price = float(price_input)

price = price + (price * 0.10)
print(f"Price after raise {price}")

price = price - (price * 0.10)
print(f"Price after fall {price}")