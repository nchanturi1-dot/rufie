from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from .background import Background

from .const import *

class ScrRecommends(Background):

    def __init__(self, name='recommendations'):
        super().__init__(name=name)
        self.memory = ObjectProperty()

        self.btn = Button(
            text="Продолжить",
            background_normal='',
            background_down='',
            background_color=DEFAULT,
            # size_hint=(0.3, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
        self.btn.bind(state=self.change_color)
        self.btn.on_press = self.set_name

        self.text_scr4 = Label(text=TXT_INDEX)

        main_line = BoxLayout(
            orientation="vertical",
        )

        main_line.add_widget(self.text_scr4)
        main_line.add_widget(self.btn)



        self.add_widget(main_line)

    def set_name(self):
        self.next()
                            
    def on_enter(self):
        self.text_scr4.text = str(self.memory)


    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'login'

    def change_color(self,button,value):
        if value == "down":  
            button.background_color = GREEN
        else:
            button.background_color = DEFAULT
            