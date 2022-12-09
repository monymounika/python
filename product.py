product1=int(input("Enter amount for product 1:"))
product2=int(input("Enter amount for product 2:"))
product3=int(input("enter amount for product 3:"))
if((product1<=0) or (product2<=0) or (product3<=0)):
    print("please enter a positive number")
else:
    print("the product quality with price: ")
    total=product1*200 + product2*300 + product3*400
    entries= {product1: 200, product2: 300, product3:400}
    print(entries)
    x=open("data.txt","a")
    print("the amount of all products")
    print("the amount of all products",file=x)
    for i,p in entries.items():
        print(i,p)
        print(i,p,file=x)
    print("the amount that you need: ")
    print("the amount that you need: ",file=x)
    print(total)
    print(total,file=x)
