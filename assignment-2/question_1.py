# If cost price and selling price of an item is input through the keyboard, write a program to
# determine whether the seller has made profit or incurred loss. Also determine how much
# profit he made or loss he incurred.

cost_price=int(input("Enter the cost of an item :"))
selling_price=int(input("Enter the selling price of an item :"))
if cost_price > selling_price:
    print("Loss he incurred :",cost_price-selling_price)
elif selling_price > cost_price:
    print("Profit he made :",selling_price-cost_price)
else:
    print("no profit or lose :)")