# coding:utf-8
from datetime import datetime

from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from ui.frame import Ui_frame


class FrameInterface(Ui_frame, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_upButton_clicked(self):
        _translate = QCoreApplication.translate
        selected_items = self.framelist.selectedItems()
        if not selected_items:
            w = MessageBox(_translate("frame", "喂！你要注入什么？"), _translate("frame", "你没有在列表选中任何的画面！"), self.window())
            w.yesButton.setText(_translate("msgbox", "对不起这就回去选"))
            w.cancelButton.hide()
            w.buttonLayout.insertStretch(1)
            w.exec()
        else:
            selected_item = selected_items[0].text()
            self.now_framename.setText(selected_item)
            self.status.setText(_translate("frame", "切换状态：正在切换"))
            self.toggle_reason.setText(_translate("frame", "上次切换原因：用户手动注入"))  # 用户手动注入、倒计时归零自动切换、初始化
            self.toggle_time.setText(_translate("frame", "上次切换时间：") + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))