from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from .background import Background

from .const import *
from .timer import Timer

class ScrBeforeSits(Background):

    def __init__(self, name='before_sits'):
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
        self.btn.set_disabled(True)
        self.btn.on_press = self.check_pulse

        self.text_scr2 = Label(text=TXT_SCR2_P1)
        self.timer = Timer(text='15 секунд')
        self.timer.bind(done=self.time_finish)
        self.text_pulse = Label(text="Введите  результат:")
        self.input_pulse = TextInput(hint_text='А мы все подсчитаем (от 8 - 40)')
        self.btn_start_timer = Button(text="Запустить таймер")

        self.btn_start_timer.on_press = self.start_timer


        input_line1 = BoxLayout(
                    size_hint=(0.8,.2)
                )
        input_line1.add_widget(self.text_pulse)
        input_line1.add_widget(self.input_pulse)

        btn_line1 = BoxLayout(
            size_hint=(0.5,.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn_line1.add_widget(self.btn_start_timer)
        btn_line1.add_widget(self.btn)
        

        main_line = BoxLayout(
            orientation="vertical",
        )

        main_line.add_widget(self.text_scr2)
        main_line.add_widget(self.timer)
        main_line.add_widget(input_line1)
        main_line.add_widget(btn_line1)


        self.add_widget(main_line)

    def check_pulse(self):
        p1 = self.input_pulse.text
        if not p1.strip():
            self.input_pulse.border = (4, 4, 4, 4)
        else:
            if p1.isdigit():
                p1 = int(p1)
                if 7<=p1<=40:
                    self.memory.p1 = p1
                    self.manager.get_screen('sits_30').memory = self.memory
                    self.next()
                            
    def on_enter(self):
        self.input_pulse.text = ''
        self.input_pulse.set_disabled(True)
        self.timer.text = '0 секунд'
        self.btn_start_timer.set_disabled(False)
        self.btn.set_disabled(True)


    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'sits_30'

    def change_color(self,button,value):
        if value == "down":  
            button.background_color = GREEN
        else:
            button.background_color = DEFAULT

    def start_timer(self):
        self.btn_start_timer.set_disabled(True)
        self.timer.restart(TIMER_P1)       

    def time_finish(self, *args):
        self.btn_start_timer.set_disabled(False)
        self.btn.set_disabled(False)
        self.timer.event.cancel()
        self.input_pulse.set_disabled(False)

