# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be
# withdrawn is input through the keyboard in hundreds, find the total number of currency
# notes of each denomination the cashier will have to give to the withdrawer.
amount=int(input("Enter The Amount : "))
hundreds=(amount // 100)
fifty_notes=(amount % 100) // 50
ten_notes=((amount % 100) % 50)// 10
print("Required notes of hundred : ",hundreds);
print("Required notes of fifty : ",fifty_notes);
print("Required notes of ten : ",ten_notes);