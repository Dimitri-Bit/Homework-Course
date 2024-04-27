discount_input = input("Enter discount (example: 20): ")
price_input = input("Enter price: ")

discount = int(discount_input)
discount = discount / 100

price = int(price_input)
price = price - (price * discount)

print(f"Original price {price_input} with discount of {discount_input} and final price is {price}")