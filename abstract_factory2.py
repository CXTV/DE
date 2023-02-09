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


class PaymentFoctory(ABC):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFacotry(PaymentFoctory):
    def create_payment(self):
        return AliPay()

class PaypalPayFacotry(PaymentFoctory):
    def create_payment(self):
        return PaypalPay()



ali_pay_factory = AlipayFacotry()
ali_pay = ali_pay_factory.create_payment()
ali_pay._pay()