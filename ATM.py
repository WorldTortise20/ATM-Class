class ATM (object):
    def __init__(self, pin, account_holder_name):
        self.pin = pin
        self.account_holder_name = account_holder_name

    def cashWithdrawal(a):
        a = int(input("How much do you want to withdraw? Current balance: "+ str(100000)))
        if a>100000:
            print("Can't withdraw the cash. Exceeding by $"+ str((a-100000)))
        else:
            print("Withdrawal successful! Balance remaining: " + str(100000-a))
        
    def inputCash(b):
        b = input("How much cash do you want to enter?")
        print("$"+str(b)+ " entered!")

aPerson = ATM(2718, "Math")
print("Pin Number: "+ str(aPerson.pin))
print("Account holder: " + str(aPerson.account_holder_name))
aPerson.cashWithdrawal()
aPerson.inputCash()
