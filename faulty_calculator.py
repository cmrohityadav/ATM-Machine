print("welcome to Faulty Calculator")
x1=int(input("Enter the Number\n"))
x=(input("Enter the Operators +,*,/,-  \n"))
x2=int(input("Enter the Number\n"))
if x=="+":
    if x1+x2==65:
        print("77")
    else:
        print(x1+x2)
elif x=="*":
    if 45*3==135:
        print("555")
    else:
        print(x1*x2)
elif x=="/":
    if 56/6==6:
        print("4")
    else:
        print(x1/x2)

else:
    print(x1-x2)



