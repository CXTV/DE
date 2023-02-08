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

#版本一：普通工厂
class OnlinePay_LOW:
    def creat_payment(self,method):
        if method =='alipay':
            return AliPay()
        elif method =='paypal':
            return PaypalPay()
        else:
            print("NO SUCH PAY METHOD!")

#版本二:依赖注入
class OnlinePay:
    def __init__(self,pay_method:Payment) -> None:
        self._pay_method = pay_method

    def pay_online(self):
        self._pay_method._pay()
        return
    
alipay =AliPay()
pay1 = OnlinePay(alipay)
pay1.pay_online()

