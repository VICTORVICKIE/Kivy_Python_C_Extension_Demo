from kivy.app import App
from kivy.uix.label import Label

from custom_lib import custom_module

class MyApp(App):

    def build(self):
        return Label(text=custom_module.custom_hello())


if __name__ == '__main__':
    MyApp().run()