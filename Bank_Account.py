class BankAccount:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.history=[]
       

    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance+=amount
        self.history.append(f"Deposited :{amount}")  # can't assign to an index in a list that does not exist yet. hence use append method..
            

        
    def withdraw(self,amount):
            
        

            if amount>self.balance :
                raise ValueError("Invalid Amount for withdrawal.")  # only error is raised like a real error but it is handled via try except so whatever error is raised that is handled and the error msg is shown .
            if amount<0:
                raise ValueError("Amount must be greater than zero.")
            self.balance-=amount
            self.history.append(f"withdraw :{amount}")
            

             
            return f"Withdraw money : Rs {amount}" 
    

    def get_balance(self):
        return f"{self.owner} has Balance: {self.balance}"
        

    def transaction_history(self):
        return self.history

       
    def get_history(self):


        print(f"The transaction History for {self.owner}: \n")
        for transaction in self.history:
            print(f" - {transaction}")

     

acc1=BankAccount("Ravi",1000)
print(acc1.owner,acc1.balance)
try:  # use try except only at time of checking this test cases not inside the class .  also one try except block for one error code ..otherwise all below these will not get executed.

    acc1.deposit(500)

    print(acc1.withdraw(200))
    acc1.withdraw(5000)  # should fail
   
except ValueError as e :
    print(f"Error : {e}")  # here e is the error msg .

try:
    acc1.deposit(-100)   # should fail
except ValueError as e :
    print(f"Error : {e}")

print(acc1.get_balance())
print(acc1.transaction_history())
acc1.get_history()