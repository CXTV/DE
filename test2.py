#reduce coupling 
from abc import ABC,abstractmethod

class People(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class Chinese(People):
    
    def say_hello(self):
        print('I am chinese')
        return 

class Janpese(People):
    
    def say_hello(self):
        print('I am Janpese')
        return 

class American(People):
    
    def say_hello(self):
        print('I am American')
        return 

class MakePeopleFactory(ABC):
    @abstractmethod
    def make_baby(slef):
        pass

class MakeHighQualityBaby(MakePeopleFactory):

    def make_baby(slef):
        return American()

class MakeLowQualityBaby(MakePeopleFactory):

    def make_baby(slef):
        return Janpese()


def people_factort(people:People):
    people.say_hello()


def make_baby_by_factory():
    return 


c1 = Chinese()
j1 = Janpese()
people_factort(j1)


