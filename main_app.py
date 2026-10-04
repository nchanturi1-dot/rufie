
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager



from screens.scr1_login import ScrLogin
from screens.scr2_p1 import ScrBeforeSits
from screens.scr3_sits import Scr30Sits
from screens.scr4_p2_p3 import ScrCount
from screens.scr5_res import ScrRecommends

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScrLogin())
        sm.add_widget(ScrBeforeSits())
        sm.add_widget(Scr30Sits())
        sm.add_widget(ScrCount())
        sm.add_widget(ScrRecommends())
        return sm


app = MyApp()
app.run()