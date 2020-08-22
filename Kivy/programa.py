from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Layout1(BoxLayout):
    pass


class Multicalc(App):
    def build(self):
        return Layout1()


Multicalc().run()