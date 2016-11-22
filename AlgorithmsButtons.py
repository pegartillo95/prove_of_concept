from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty


#classes for the algorithms buttons
class AlgorithmListButton(ListItemButton):
    pass

class LR_ListButton(AlgorithmListButton):
    text = "Linear Regression"