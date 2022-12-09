totalProduct=0
product1=int(input("Enter amount for product 1:"))
product2=int(input("Enter amount for product 2:"))
product3=int(input("enter amount for product 3:"))
product1Amount=product1*400
product2Amount=product1*50
product3Amount=product1*60
totalProduct=product1Amount+product2Amount+product3Amount
print("print the total the user needs to pay=", totalProduct)

if((product1<=0) or (product2<=0) or (product3<=0)):
    print("please enter a positive number")
else:
    totalProduct=product1Amount+product2Amount+product3Amount
    entries={product1:100, product2:200, product2Amount:300}
    print("the amount of all products")
    entries1={product1:product1Amount, product2:product2Amount, product3:product3Amount}
    for k,v in enteries.items():
        print(k,v)
    print(entries1)
    print("the total amount should be paid by the user is", totalProduct)