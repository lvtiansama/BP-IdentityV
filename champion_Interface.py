# coding:utf-8
import json
import os
import appdirs

from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect

from ui.champion import Ui_champion

_translate = QCoreApplication.translate
app_name = "BP_Identity_3d"
app_author = "Lvtiansama"
data_dir = os.path.join(appdirs.user_data_dir(appname=app_name, appauthor=app_author), "Team_Data")

class ChampionInterface(Ui_champion, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_teamup_clicked(self):
        players = (self.player, self.player_2, self.player_3,
                   self.player_4, self.player_5, self.player_6)

        for player in players:
            player.clear()

        name_list = self.refresh_player(self.combobox.currentText())
        name_list.insert(0, '')

        for player_widget in players:
            for name in name_list:
                player_widget.addItem(name)

        self.teamname.setText(self.combobox.currentText())

    def refresh_player(self, teamname):
        if teamname is None or teamname == "":
            return
        try:
            with open(os.path.join(data_dir, f"{teamname}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading: {e}")
            self.msg(_translate("champion", "呜~出错了~"), _translate("champion", "读取战队选手数据时发生错误！"),
                     _translate("msgbox", "我知道了"))

        if data['player'] and isinstance(data['player'], list):
            name_list = [player['name'] for player in data['player'] if 'name' in player]
        else:
            name_list = []

        return name_list