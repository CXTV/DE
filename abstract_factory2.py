from abc import ABC,abstractmethod

class Payment:
    @abstractmethod
    def pay(self):
        pass

class Alipay(Payment):
    def pay(self):
        print("paying by ali")
        return

class Paypal(Payment):
    def pay(self):
        print("paying by paypal...")

class Bank:
    def cost(self):
        print("paying by bank....")

class NewBankPay(Payment,Bank):
    def pay(self):
        self.cost()


class Check_payment:
    def __init__(self,payment:Payment) -> None:
        self.__payment = payment
        self.pay_flag = 1
        self.check_pay()

    def __call__(self, ) -> None:
        print("I am __call__")
        return 

    def check_pay(self):
        print("checking the payment is right or not...")
        if self.pay_flag:
            print("PAYING APROVED..WATING PAYING...")
            self.__payment.pay()
        else:
            print("Something wrong with the payment.")

ali_pay = Alipay()

new_bank_pay = NewBankPay()

Check_payment(new_bank_pay)




