class atm(object):
    UserDet = input("Enter your name- ")
    print("Hello " + UserDet +  "!!")
    print("Welcome " + UserDet + " to SBI ATM bank.")

    def __init__(self, name, cashWithdrawed, amountLeft, pin):
        self.name = name
        self.cashWithdrawed = cashWithdrawed
        self.amountLeft = amountLeft
        self.pin = pin

    #def Name(self):
        #print("Welcome " + UserDet + "to SBI ATM bank.")

    
    def CashWithdrawed(self):
        print("Cash withdrawed is 10,000" )

    def AmountLeft(self):
        print("Amount Left is 100")

    def Pin(self):
        print("Your pin is: ******")

sbi = atm("SBI,", 1000 , 100, "******")

#print(sbi.Name())
print(sbi.CashWithdrawed())
print(sbi.AmountLeft())
print(sbi.Pin())
print(sbi.name, sbi.cashWithdrawed, sbi.amountLeft, sbi.pin)
