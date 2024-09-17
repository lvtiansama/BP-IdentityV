# coding:utf-8
from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QFileDialog
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from PIL import Image

from ui.countdown import Ui_countdown


class CountdownInterface(Ui_countdown, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    def msg(self,title, content, yesbutton):
        w = MessageBox(title, content, self.window())
        w.yesButton.setText(yesbutton)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    def getpath(self):
        try:
            file_name, imgType = QFileDialog.getOpenFileName(
                self,
                f"请选择倒计时背景图",
                "",
                "PNG图片 (*.png);;JPG图片 (*.jpg)"
            )
            if file_name:
                return file_name
            else:
                return None
        except Exception as e:
            return None

    @pyqtSlot()
    def on_path_button_clicked(self):
        _translate = QCoreApplication.translate
        path = self.getpath()

        try:
            img = Image.open(path)
            width, height = img.size
        except IOError:
            self.msg(_translate("countdown", "呜~出错了~"),
                     _translate("countdown", "图片没有被正确打开！（文件不存在、路径错误、文件格式错误、权限问题等）"),
                     _translate("msgbox", "我知道了"))
            return None

        # 检查图片尺寸是否符合要求
        if width != 1920 or height != 1080:
            self.msg(_translate("countdown", "欸，奇怪的图片~"),
                     _translate("countdown", "图片没不符合要求！\n（1920*1080）"),
                     _translate("msgbox", "我知道了"))
            return None

        self.path_label.setText(str(path))
        self.msg(_translate("countdown", "上传成功"),
                 _translate("countdown", f"图片 {path} 已经被上传"),
                 _translate("msgbox", "我知道了"))