from dataclasses import dataclass
from abc import ABC,abstractmethod

#产品1
@dataclass
class Player:
    face:str = None
    hair:str = None
    body:str = None

#产品2
@dataclass
class Player2:
    face:str = None
    hair:str = None
    body:str = None

#抽象建造者
class Builder(ABC):
    
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_hair(self):
        pass    
    
    @abstractmethod
    def build_body(self):
        pass

#具体建造者1
class SexyGirl(Builder):
    
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self):
        self.player.face = "baby face"
        return self 
     
    def build_hair(self):
        self.player.hair = "brown hair"     
        return self 
    
    def build_body(self):
        self.player.body = "hot body"
        return self 
    
#具体建造着2
class Monster(Builder):
    
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self):
        self.player.body = "Monster face"
        return self 
    
    def build_hair(self):
        self.player.hair = "Monster hair"     
        return self ## 返回自己可以类似于java的链式调用
    
    def build_body(self):
        self.player.body = "Monster body"
        return self
    
#指挥者
class BuildDirector: ##控制顺序

    def build_charecher1(self,builder:Builder):
        builder.build_face().build_body().build_hair()
        return builder.player
    
    def build_charecher2(self,builder:Builder):
        builder.build_body().build_hair().build_face()
        return builder.player
    
sexy_girl = SexyGirl()
director = BuildDirector()
p = director.build_charecher2(sexy_girl)
print(vars(p)) #打印出p的所有方法
print(isinstance(p,Player)) #判断实例是否属于某个实例1
print(type(p) is Builder) #判断实例是否属于某个实例2
