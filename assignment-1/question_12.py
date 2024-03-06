# . If the total selling price of 15 items and the total profit earned on them is input through the
# keyboard, write a program to find the cost price of one item.

sp=int(input("Enter the selling price : "))
tp=int(input("Enter the total profit :"))
item=int(input("Enter the item :"))
one_item=(sp-tp)//item
print("The cost of one item is ",one_item)

