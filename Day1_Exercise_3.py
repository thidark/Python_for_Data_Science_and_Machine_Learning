balance=1000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")        
print("4. Exit")

while(1):
    option=int(input("Enter your choice: ")) 
    if(option==1):
        print(f"Your balance is: {balance}")
    elif(option==2):
        amount=int(input("Enter deposit amount: "))
        balance+=amount
        print("Deposit successful!")
        print(f"New balance: ${balance}")
    elif(option==3):
        amount=int(input("Enter withdraw amount: "))
        if(amount>balance):
            print("Insufficient balance")
        else:
            balance-=amount
            print("Withdraw successful!")
            print(f"New balance: ${balance}")
    elif(option==4):
        exit()
    
    