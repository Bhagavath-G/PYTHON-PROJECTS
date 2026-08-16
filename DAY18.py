
'''PROJECT 18'''

balance = 96000
amount = int(input("ENTER WITHDRAW AMOUNT:"))

if amount <=balance:
    balance -= amount
    print("WITHDRAW SUCCESSFULL")
    print("Remaining Balance",balance)
else:
    print("INSUFFICIENT BALANCE")
