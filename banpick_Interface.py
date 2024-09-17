# coding:utf-8
from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from ui.banpick import Ui_banpick

_translate = QCoreApplication.translate

class BanpickInterface(Ui_banpick, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setupUi(self, parent)
        self.surs = self._parent.surs
        self.killers = self._parent.killers

    def msg(self,title, content, yesbutton):
        w = MessageBox(title, content, self.window())
        w.yesButton.setText(yesbutton)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    @pyqtSlot()
    def on_upsur_clicked(self):
        if self.sur.text() in self.surs:
            self._parent.afterthegameInterface.sur.setText(self.sur.text())
            self.msg(_translate("banpick", "OK"), _translate("banpick", f"求生者1 {self.sur.text()} 已上场"),
                     _translate("msgbox", "我知道了"))
        else:
            self.msg(_translate("banpick", "呜呜，找不到啊~"), _translate("banpick", f"未在数据库中找到名为：{self.sur.text()} 的求生者"),
                     _translate("msgbox", "我知道了"))

    @pyqtSlot()
    def on_upsur_2_clicked(self):
        if self.sur_2.text() in self.surs:
            self._parent.afterthegameInterface.sur_2.setText(self.sur_2.text())
            self.msg(_translate("banpick", "OK"), _translate("banpick", f"求生者2 {self.sur_2.text()} 已上场"),
                     _translate("msgbox", "我知道了"))
        else:
            self.msg(_translate("banpick", "呜呜，找不到啊~"), _translate("banpick", f"未在数据库中找到名为：{self.sur_2.text()} 的求生者"),
                     _translate("msgbox", "我知道了"))

    @pyqtSlot()
    def on_upsur_3_clicked(self):
        if self.sur_3.text() in self.surs:
            self._parent.afterthegameInterface.sur_3.setText(self.sur_3.text())
            self.msg(_translate("banpick", "OK"), _translate("banpick", f"求生者3 {self.sur_3.text()} 已上场"),
                     _translate("msgbox", "我知道了"))
        else:
            self.msg(_translate("banpick", "呜呜，找不到啊~"), _translate("banpick", f"未在数据库中找到名为：{self.sur_3.text()} 的求生者"),
                     _translate("msgbox", "我知道了"))

    @pyqtSlot()
    def on_upsur_4_clicked(self):
        if self.sur_4.text() in self.surs:
            self._parent.afterthegameInterface.sur_4.setText(self.sur_4.text())
            self.msg(_translate("banpick", "OK"), _translate("banpick", f"求生者4 {self.sur_4.text()} 已上场"),
                     _translate("msgbox", "我知道了"))
        else:
            self.msg(_translate("banpick", "呜呜，找不到啊~"), _translate("banpick", f"未在数据库中找到名为：{self.sur_4.text()} 的求生者"),
                     _translate("msgbox", "我知道了"))

    @pyqtSlot()
    def on_upkill_clicked(self):
        if self.killer.text() in self.killers:
            self._parent.afterthegameInterface.killer.setText(self.killer.text())
            self.msg(_translate("banpick", "OK"), _translate("banpick", f"监管者 {self.killer.text()} 已上场"),
                     _translate("msgbox", "我知道了"))
        else:
            self.msg(_translate("banpick", "呜呜，找不到啊~"), _translate("banpick", f"未在数据库中找到名为：{self.killer.text()} 的监管者"),
                     _translate("msgbox", "我知道了"))

    @pyqtSlot()
    def on_player_changed(self):
        self._parent.afterthegameInterface.player_2.setText(self.player.text())

    @pyqtSlot()
    def on_player_2_changed(self):
        self._parent.afterthegameInterface.player_3.setText(self.player_2.text())

    @pyqtSlot()
    def on_player_3_changed(self):
        self._parent.afterthegameInterface.player_4.setText(self.player_3.text())

    @pyqtSlot()
    def on_player_4_changed(self):
        self._parent.afterthegameInterface.player_5.setText(self.player_4.text())

    @pyqtSlot()
    def on_player_5_changed(self):
        self._parent.afterthegameInterface.player.setText(self.player_5.text())

    @pyqtSlot()
    def on_clear_clicked(self):
        boxnames = (self.sur, self.sur_2, self.sur_3, self.sur_4, self.bansur, self.bansur_2,
                   self.bansur_3, self.bansur_4, self.bansur_5, self.bansur_6, self.bansur_7,
                   self.banall, self.banall_2, self.banall_3, self.banall_4, self.banall_5, self.banall_6,
                   self.killer, self.bankill, self.bankill_2, self.bankill_3)

        for boxname in boxnames:
            boxname.clear()
        self._parent.afterthegameInterface.sur.setText(_translate("afterthegame", "未pick角色"))
        self._parent.afterthegameInterface.sur_2.setText(_translate("afterthegame", "未pick角色"))
        self._parent.afterthegameInterface.sur_3.setText(_translate("afterthegame", "未pick角色"))
        self._parent.afterthegameInterface.sur_4.setText(_translate("afterthegame", "未pick角色"))
        self._parent.afterthegameInterface.killer.setText(_translate("afterthegame", "未pick角色"))