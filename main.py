x = int(input("enter the first number"))
y = int(input("enter the second number"))
if x>y:
    print(x,"is greater than",y)
elif y>x:
    print(y,"is greater than",x)
elif x==y:
    print(x,"is equal to", y)
else:
    print("something went wrong")        