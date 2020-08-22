from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout



class Myapp(App):
    def build(self):
        layout = BoxLayout()
        bt = Button(text='Olá, mundo')
        layout.add_widget(bt)
        return layout

def main():
    Myapp().run()


if __name__ == '__main__':
    main()
