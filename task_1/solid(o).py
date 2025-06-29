from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def pay(self):
        return "Paid using credit card"
    

class PayPalPayment(Payment):
    def pay(self):
        return "Paid using PayPal"
    

class CryptoPayment(Payment):
    def pay(self):
        return "Paid using Crypto"
    

class PaymentProcessor:
    def __init__(self, payment):
        self.payment = payment

    def pay(self):
        return self.payment.pay()
    

credit_card = CreditCardPayment()
pay_pal = PayPalPayment()
crypto = CryptoPayment()

payment_processor = PaymentProcessor(crypto)
print(payment_processor.pay())