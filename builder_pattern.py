from dataclasses import dataclass
from abc import ABC,abstractmethod

#产品
@dataclass
class Player:
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

#具体建造者
class SexyGirl(Builder):
    
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self):
        self.player.face = "baby face"
    
    def build_hair(self):
        self.player.hair = "brown body"     

    def build_body(self):
        self.player.body = "hot body"

#具体建造折
class Monster(Builder):
    
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self):
        self.player.body = "Monster face"
    
    def build_hair(self):
        self.player.hair = "Monster hair"     

    def build_body(self):
        self.player.body = "Monster body"

#指挥者
class BuildDirector: ##控制顺序
    def build_charecher(self,builder:Builder):
        builder.build_hair()
        builder.build_face()
        builder.build_body()
        return builder.player

sexy_girl = SexyGirl()
director = BuildDirector()
p = director.build_charecher(sexy_girl)
print(vars(p)) #查看所有类属性的所有值！