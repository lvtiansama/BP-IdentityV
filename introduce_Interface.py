# coding:utf-8
import json
import os
import appdirs

from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QTableWidgetItem
from PyQt6.QtCore import QCoreApplication, pyqtSlot
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from ui.introduce import Ui_introduce

_translate = QCoreApplication.translate
app_name = "BP_Identity_3d"
app_author = "Lvtiansama"
data_dir = os.path.join(appdirs.user_data_dir(appname=app_name, appauthor=app_author), "Team_Data")

class IntroduceInterface(Ui_introduce, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setupUi(self, parent)

    def msg(self,title, content, yesbutton):
        w = MessageBox(title, content, self.window())
        w.yesButton.setText(yesbutton)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    def setbpplayer(self, Bool):
        bpplayers = (self._parent.banpickInterface.player, self._parent.banpickInterface.player_2, self._parent.banpickInterface.player_3,
                     self._parent.banpickInterface.player_4)

        name_list = self.refresh_player(self.main_combobox.currentText())
        name_list.insert(0, '')
        sur_name_list = self.refresh_player(self.sub_combobox.currentText())
        sur_name_list.insert(0, '')

        for player in bpplayers:
            player.clear()
        self._parent.banpickInterface.player_5.clear()

        if Bool == True:
            for name in name_list:
                self._parent.banpickInterface.player_5.addItem(name)

            for player_widget in bpplayers:
                for name in sur_name_list:
                    player_widget.addItem(name)

        elif Bool == False:
            for name in sur_name_list:
                self._parent.banpickInterface.player_5.addItem(name)

            for player_widget in bpplayers:
                for name in name_list:
                    player_widget.addItem(name)

    @pyqtSlot()
    def on_main_button_clicked(self):
        players = (self.main_player, self.main_player_2, self.main_player_3,
                   self.main_player_4, self.main_player_5, self.main_player_6)
        self._parent.scoreInterface.table_score.setItem(0, 0, QTableWidgetItem(self.main_combobox.currentText()))
        self._parent.scoreInterface.mainname.setText(self.main_combobox.currentText())
        self.main_team.setText(self.main_combobox.currentText())

        for player in players:
            player.clear()

        name_list = self.refresh_player(self.main_combobox.currentText())
        name_list.insert(0, '')

        for player_widget in players:
            for name in name_list:
                player_widget.addItem(name)

        self.setbpplayer(self._parent.scoreInterface.radioButton.isChecked())



    @pyqtSlot()
    def on_sub_button_clicked(self):
        players = (self.sub_player, self.sub_player_2, self.sub_player_3,
                   self.sub_player_4, self.sub_player_5, self.sub_player_6)
        self._parent.scoreInterface.table_score.setItem(1, 0, QTableWidgetItem(self.sub_combobox.currentText()))
        self._parent.scoreInterface.subname.setText(self.sub_combobox.currentText())
        self.sub_team.setText(self.sub_combobox.currentText())

        for player in players:
            player.clear()

        name_list = self.refresh_player(self.sub_combobox.currentText())
        name_list.insert(0, '')

        for player_widget in players:
            for name in name_list:
                player_widget.addItem(name)

        self.setbpplayer(self._parent.scoreInterface.radioButton.isChecked())

    def refresh_player(self, teamname):
        if teamname is None or teamname == "":
            return
        try:
            with open(os.path.join(data_dir, f"{teamname}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading: {e}")
            self.msg(_translate("introduce", "呜~出错了~"), _translate("introduce", "读取战队选手数据时发生错误！"),
                     _translate("msgbox", "我知道了"))

        if data['player'] and isinstance(data['player'], list):
            name_list = [player['name'] for player in data['player'] if 'name' in player]
        else:
            name_list = []

        return name_list
