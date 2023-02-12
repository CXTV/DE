from abc import ABC,abstractmethod

class Payment:
    @abstractmethod
    def pay(self):
        pass

class AliPay(Payment):
    def pay(self):
        print("pay by alimama...")
    
class GongShangBankPay:
    def cost(slef):
        print("pay by GongShang...")

class ZhongGuoBankPay:
    def cost(slef):
        print("pay by ZhongGuo...")



###简易版本使用多继承完成
# class NewBankPay(Payment,BankPay):
#     def pay(self):
#         self.cost()

class PaymentAdapter(Payment):
    def __init__(self,payment:Payment) -> None:
        self._payment = payment

    def pay(self):
        self._payment.cost()


g_bank_pay = PaymentAdapter(GongShangBankPay())
z_bank_pay = PaymentAdapter(ZhongGuoBankPay())
g_bank_pay.pay()
z_bank_pay.pay()

