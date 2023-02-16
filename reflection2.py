
class Calculator:
    def add(self):
        print("add...")
    
    def minus(self):
        print("minus...")

    def multiple(self):
        print("multiple...")
    
    def divide(self):
        print("divide...")
    
    def calculate(self,method):
        if hasattr(self,method):
            func = getattr(self,method)
            func()

cal = Calculator()
cal.calculate("add")
