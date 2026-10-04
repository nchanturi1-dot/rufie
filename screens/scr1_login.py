from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from .background import Background

from .const import *
from .memory import *


class ScrLogin(Background):
    def __init__(self, name='login'):
        super().__init__(name=name)

        self.btn = Button(
            text="enter",
            background_normal='',
            background_down='',
            background_color=DEFAULT,
            size_hint=(0.3, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
        self.btn.bind(state=self.change_color)

        self.btn.on_press = self.check_login

        self.text_scr2 = Label(text=TXT_INSTRUCTION)
        self.text_name = Label(text="Имя")
        self.input_name = TextInput(hint_text='На русском')
        self.text_age = Label(text="Возраст")
        self.input_age = TextInput(hint_text='от 7 до 99')

              


        input_line1 = BoxLayout(
            size_hint=(0.8,.2)
        )
        input_line1.add_widget(self.text_name)
        input_line1.add_widget(self.input_name)

        input_line2 = BoxLayout(
                    size_hint=(0.8,.2)
                )
        input_line2.add_widget(self.text_age)
        input_line2.add_widget(self.input_age)


        main_line = BoxLayout(
            orientation="vertical",
        )

        main_line.add_widget(self.text_scr2)
        main_line.add_widget(input_line1)
        main_line.add_widget(input_line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def check_login(self):
        name = self.input_name.text
        if not name.strip():
            self.input_name.background_color = RED
        else:
            self.input_name.background_color = WHITE
            age = self.input_age.text
            if not age.strip():
                self.input_age.background_color = RED
            else:
                self.input_age.background_color = WHITE
                if age.isdigit():
                    age = int(age)
                    if 7 <= age <= 120:
                        memory = Memory(name,age)
                        self.manager.get_screen('before_sits').memory = memory
                        self.next()
                                
    def on_enter(self):
        self.input_name.text = ''
        self.input_age.text = ''



    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'before_sits'

    def change_color(self,button,value):
        if value == "down":  
            button.background_color = GREEN
        else:
            button.background_color = DEFAULT

