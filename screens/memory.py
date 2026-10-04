from .const import *


class Memory():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.index = 0
 
    def rufie(self):
        self.index = (4 * (self.p1 + self.p2 + self.p3) - 200) / 10
        return self.index

    def minimal(self):
        n = (min(15,self.age) - 7) // 2
        level = 21-1.5*n
        return level

    def get_lvl(self):
        self.index = self.rufie()
        level = self.minimal()
        steps = [0, 4, 5, 5.5, 0]
        self.score = 0
        for step in steps:
            level -= step
            if level <= self.index:
                return self.score
            self.score += 1
        self.score -= 1
        return self.score

    def __str__(self):
        self.get_lvl()
        s = f"{self.name},\nВаш индекс руфье: {self.index}.\nРаботоспособность сердца: {RES[self.score]}"
        return s