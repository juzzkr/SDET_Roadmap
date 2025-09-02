from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class Creditcardpay(Payment):
    def pay(self, amount):
        return f"Paid ${amount} through Creditcard"
        
class Upipay(Payment):
    def pay(self, amount):
        return f"Paid ${amount} through UPI"
        
pay1 = Creditcardpay()
pay2 = Upipay()

print(pay1.pay(100))
print(pay2.pay(300))
