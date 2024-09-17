# coding:utf-8
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6 import QtWidgets

from ui.afterthegame import Ui_afterthegame


class AfterthegameInterface(Ui_afterthegame, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_clear_clicked(self):
        # 遍历布局中的所有控件并重置它们的状态
        checkbox_names = ['checkBox_1', 'checkBox_2', 'checkBox_3', 'checkBox_4']
        lineedit_names = ['poyi', 'poyi_2', 'poyi_3', 'poyi_4', 'banzi', 'banzi_2', 'banzi_3', 'banzi_4', 'banzi_5',
                          'jiuren', 'jiuren_2', 'jiuren_3', 'jiuren_4', 'zhiliao', 'zhiliao_2', 'zhiliao_3',
                          'zhiliao_4', 'liugui', 'liugui_2', 'liugui_3', 'liugui_4', 'mimaji', 'jizhong', 'jidao',
                          'zhenshe']

        [self.findChild(QtWidgets.QCheckBox, name).setChecked(False) for name in checkbox_names]
        [self.findChild(QtWidgets.QLineEdit, name).clear() for name in lineedit_names]
