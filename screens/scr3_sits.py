from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from .const import *

from .background import Background
from .timer import Timer
from .beat import Sits

class Scr30Sits(Background):

    def __init__(self, name='sits_30'):
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
        self.btn.set_disabled(True)

        self.text_scr2 = Sits(TIMER_SITS,text=TXT_SCR3_SITS)


        self.timer = Timer(text='45 секунд')
        self.timer.bind(done=self.time_finish)
        # self.timer.bind(done=self.text_scr2.animation.stop)

        self.btn_start_timer = Button(text="Запустить таймер")

        self.btn_start_timer.on_press = self.start_timer
        
        sits_line = BoxLayout()
        sits_line.add_widget(self.text_scr2)


        btn_line1 = BoxLayout(
            size_hint=(0.5,.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn_line1.add_widget(self.btn_start_timer)
        btn_line1.add_widget(self.btn)
        

        main_line = BoxLayout(
            orientation="vertical",
        )

        main_line.add_widget(sits_line)
        main_line.add_widget(self.timer)
        main_line.add_widget(btn_line1)


        self.add_widget(main_line)

    def set_name(self):
        self.manager.get_screen('count_pulse').memory = self.memory
        self.next()
                            
    def on_enter(self):
        self.timer.text = '0 секунд'
        self.btn_start_timer.set_disabled(False)
        self.btn.set_disabled(True)


    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'count_pulse'

    def change_color(self,button,value):
        if value == "down":  
            button.background_color = GREEN
        else:
            button.background_color = DEFAULT

    def start_timer(self):
        self.text_scr2.start()
        self.btn_start_timer.set_disabled(True)
        self.timer.restart(TIMER_SITS)

    def time_finish(self, *args):
        self.btn_start_timer.set_disabled(False)
        self.btn.set_disabled(False)
        self.timer.event.cancel()
