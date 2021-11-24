from kivy.app import App
from kivy.uix.label import label

class TestApp(App):
    def build(self):
        return Label(text='Hello World')

App().run()