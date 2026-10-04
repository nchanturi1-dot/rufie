from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty

from kivy.animation import Animation

class Sits(Label):
    repeats = NumericProperty(0)
    done = BooleanProperty(False)
    def __init__(self,total,**kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.now = total
        self.text = f"Осталось: {self.now} приседаний"
        self.animation = Animation(font_size=18,duration=0.3) + \
                         Animation(font_size=35,duration=0.7)
        self.animation.on_progress = self.next

    def start(self):
        self.repeats = 0
        self.done = False
        self.animation.repeat = True
        self.animation.start(self)


    def next(self,*args):
        print(args)
        if args[1] == 1:
            self.repeats += 1
            if self.repeats >= self.total:
                self.done = True
                self.animation.stop(self)
                self.text = "Готово!"
            else:
                
                self.now -= 1
                self.text = f"Осталось: {self.now} приседаний"
            
        