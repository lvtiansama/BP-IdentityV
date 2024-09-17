# coding:utf-8
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect

from ui.home import Ui_home


class HomeInterface(Ui_home, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setupUi(self, parent)
