from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from .background import Background

from .const import *
from .timer import Timer

class ScrCount(Background):

    def __init__(self, name='count_pulse'):
        super().__init__(name=name)
        self.memory = ObjectProperty()

        self.timer_number = 0

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

        self.text_scr2 = Label(text=TXT_SCR4_P3)

        self.timer_1 = Timer(text="15 сек")
        self.timer_2 = Timer(text="30 сек")
        self.timer_3 = Timer(text="15 сек")

        self.timer_1.bind(done=self.time1_finish)
        self.timer_2.bind(done=self.time2_finish)
        self.timer_3.bind(done=self.time3_finish)

        self.text_p2 = Label(text="Результат")
        self.input_p2 = TextInput(hint_text='от 10 до 50')

        self.text_p3 = Label(text="Результат после отдыха")
        self.input_p3 = TextInput(hint_text='от 7 до 40')

        self.btn_start_timer = Button(text="Запустить таймер")
        self.btn_start_timer.on_press = self.start_timer
        
        

        timer_line = BoxLayout(
            size_hint=(0.8,.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        timer_line.add_widget(self.timer_1)
        timer_line.add_widget(self.timer_2)
        timer_line.add_widget(self.timer_3)

        input_line1 = BoxLayout(
            size_hint=(0.8,.2)
        )
        input_line1.add_widget(self.text_p2)
        input_line1.add_widget(self.input_p2)

        input_line2 = BoxLayout(
                    size_hint=(0.8,.2)
                )
        input_line2.add_widget(self.text_p3)
        input_line2.add_widget(self.input_p3)

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
        main_line.add_widget(timer_line)
        main_line.add_widget(input_line1)
        main_line.add_widget(input_line2)
        main_line.add_widget(btn_line1)

        self.add_widget(main_line)

    def check_pulse(self):
        p2 = self.input_p2.text
        p3 = self.input_p3.text
        if not p2.strip():
            self.input_p2.border = (4, 4, 4, 4)
        elif not p3.strip():
            self.input_p3.border = (4, 4, 4, 4)
        else:
            if p2.isdigit() and p3.isdigit():
                p2 = int(p2)
                p3 = int(p3)
                if 10<=p2<=50 and 7<=p3<=40:
                    self.memory.p2 = p2
                    self.memory.p3 = p3
                    self.manager.get_screen('recommendations').memory = self.memory
                    self.next()
                            
    def on_enter(self):
        self.input_p2.text = ''
        self.input_p3.text = ''
        self.timer_1.text = '0 секунд'
        self.timer_2.text = '0 секунд'
        self.timer_3.text = '0 секунд'
        self.btn_start_timer.set_disabled(False)
        self.btn.set_disabled(True)

        self.input_p2.set_disabled(True)
        self.input_p3.set_disabled(True)


    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'recommendations'

    def change_color(self,button,value):
        if value == "down":  
            button.background_color = GREEN
        else:
            button.background_color = DEFAULT

    def start_timer(self):
        self.timer_number += 1
        self.btn_start_timer.set_disabled(True)
        if self.timer_number == 1:
            self.timer_1.restart(TIMER_P2)
        elif self.timer_number == 2:
            self.timer_2.restart(TIMER_REST)
        elif self.timer_number == 3:
            self.timer_3.restart(TIMER_P3)
        else:
            self.timer_number = 0
            self.btn_start_timer.set_disabled(True)

    def time1_finish(self, *args):
        self.input_p2.set_disabled(False)
        self.btn_start_timer.set_disabled(False)
        self.timer_1.event.cancel()

    def time2_finish(self, *args):
        self.btn_start_timer.set_disabled(False)
        self.timer_2.event.cancel()

    def time3_finish(self, *args):
        self.input_p3.set_disabled(False)
        self.btn_start_timer.set_disabled(False)
        self.timer_3.event.cancel()
        self.btn.set_disabled(False)