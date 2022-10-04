'''
Author:Rohit Chhabiraj Yadav
Email:cmrohityadav23@gmail.com
'''
balance = 10000 #preloaded amount in your account
print("""
Welcome to RCY Bank ATM""")
pin=int(input("Enter the pin number:"))
if(pin==1234):

    print("""
Welcome to RCY Bank ATM

Choose Options

1)BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT

""")
option = int(input("Select the Option:"))

if(option == 1):
    print("Your balance is ", balance)
elif(option==2):
    withdraw = float(input("Enter amount to withdraw "))
    if(balance > withdraw):
        total = balance - withdraw
        print("success")
        print("your Current  balance is :",total)
    else:
        print("insufficient Balance")
elif(option==3):
    deposit = float(input("Enter amount to deposit "))
    totalbalance = balance + deposit
    print("success")
    print("total balnace now is: ", totalbalance)
elif(option==4):
    exit()
else:
    print("no selected Options")
    