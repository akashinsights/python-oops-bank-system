from abc import ABC,abstractmethod

class Bank(ABC):
    def __init__(self,name,balance,minimum_balance):
        self.name=name
        self.__balance=balance
        self.__minimum_balance=minimum_balance
        


    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass
    
    @abstractmethod
    def transfer(self,amount,number):
        pass
     
    def _update_balance(self,amount):
        self.__balance+=amount
    def get_private_balance(self):
        return self.__balance
    def get_minimum_balance(self):
        return self.__minimum_balance

class SavingsAccount(Bank):
    def get_balance(self):
        print(f"{self.name} balance is {self.get_private_balance()}")

    def deposit(self, amount):
        self._update_balance(amount)
        print(f"deposited amount is {amount}")

    def withdraw(self, amount):
        if amount <=self.get_private_balance():
            self._update_balance (-amount)
            print(f"withdrawn {amount}")
        else :
            print("not eligible for withdraw")

    def transfer(self, amount, number):
        if amount<=self.get_private_balance()-amount>=self.get_minimum_balance():
            self._update_balance(-amount)
            print(f"{amount}is transferring to{number} ")
        else:
            print("please check your minimum balance")
        

acc=SavingsAccount("Akash",5000,1000)
acc.get_balance()
acc.deposit(2000)
acc.withdraw(3000)
acc.get_balance() 
acc.transfer(1700,1234567890)  



