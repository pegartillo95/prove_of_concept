import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


#Classes for the popups
class LR_Popup(Popup):
    pass

class MainScreen(FloatLayout):
    layout_content=ObjectProperty(None)
    algorithms_list=ObjectProperty()

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

    #Functions to add algorithms to the algorithms list
    def add_linear_reg(self):
        self.algorithms_list.adapter.data.extend(["Linear regression"])
        self.algorithms_list._trigger_reset_populate()

    def add_logistic_regression(self):
        self.algorithms_list.adapter.data.extend(["Logistic regression"])
        self.algorithms_list._trigger_reset_populate()

    def add_SVM(self):
        self.algorithms_list.adapter.data.extend(["Support vector machine"])
        self.algorithms_list._trigger_reset_populate()

    def add_K_means(self):
        self.algorithms_list.adapter.data.extend(["K means"])
        self.algorithms_list._trigger_reset_populate()

    #Open popups to change the parameters of concrete algorithm
    def open_LR_Popup(self):
        the_popup = LR_Popup()
        the_popup.open()

class proveApp(App):
    def build(self):
        return MainScreen()

prove = proveApp()
prove.run()