from abc import ABC,abstractmethod


class Payment(ABC):   
    @abstractmethod
    def _pay(self):
        pass


class AliPay(Payment):
    def _pay(self):
        print("Paying by Ali...")


class PaypalPay(Payment):
    def _pay(self):
        print("Pay by Paypal...")


class PayMethod(ABC):
    @abstractmethod
    def __init__(self,pay_method:Payment) -> None:
        self._pay_method = pay_method

    @abstractmethod
    def pay(self):
        pass


class OnlinePay(PayMethod):
    def __init__(self,pay_method:Payment) -> None:
        self._pay_method = pay_method

    def pay(self):
        print("Paying by Online...")
        self._pay_method._pay()
        return
    
class BankPay(PayMethod):
    def __init__(self,pay_method:Payment) -> None:
        self._pay_method = pay_method

    def pay(self):
        print("Paying by Bank...")
        self._pay_method._pay()
#         return

    
# alipay =AliPay()
# pay_online = OnlinePay(alipay)
# pay_Bank = BankPay(alipay)
# pay_online.pay()
# pay_Bank.pay()

import sys
print(sys.path)

