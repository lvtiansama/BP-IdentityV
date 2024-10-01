# coding:utf-8
import json
import os
import appdirs

from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QTableWidgetItem
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from ui.score import Ui_score

_translate = QCoreApplication.translate
app_name = "BP_Identity_3d"
app_author = "Lvtiansama"
data_dir = os.path.join(appdirs.user_data_dir(appname=app_name, appauthor=app_author), "Team_Data")

class ScoreInterface(Ui_score, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setupUi(self)

    def refresh_player(self, teamname):
        if teamname is None or teamname == "":
            return
        try:
            with open(os.path.join(data_dir, f"{teamname}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading: {e}")
            self.msg(_translate("library", "呜~出错了~"), _translate("introduce", "读取战队选手数据时发生错误！"),
                     _translate("msgbox", "我知道了"))

        if data['player'] and isinstance(data['player'], list):
            name_list = [player['name'] for player in data['player'] if 'name' in player]
        else:
            name_list = []

        return name_list

    def setbpplayer(self, Bool):
        main_bool = False
        sub_bool = False
        teamname_main = self._parent.introduceInterface.main_team.text()
        teamname_sub = self._parent.introduceInterface.sub_team.text()
        if teamname_main == "当前无战队上场":
            self.msg(_translate("library", "非法操作警告！"), _translate("library", "主场战队未上场！"),
                     _translate("msgbox", "我知道了"))
            main_bool = True
        elif teamname_sub == "当前无战队上场":
            self.msg(_translate("library", "非法操作警告！"), _translate("library", "客场战队未上场！"),
                     _translate("msgbox", "我知道了"))
            sub_bool = True

        bpplayers = (self._parent.banpickInterface.player, self._parent.banpickInterface.player_2, self._parent.banpickInterface.player_3,
                     self._parent.banpickInterface.player_4)

        if main_bool == True:
            name_list = []
        else:
            name_list = self.refresh_player(teamname_main)
        name_list.insert(0, '')


        if sub_bool == True:
            sur_name_list = []
        else:
            sur_name_list = self.refresh_player(teamname_sub)
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

    def clearafterthegeme_playername(self):
        self._parent.afterthegameInterface.player.setText(_translate("afterthegame", "未上场"))
        self._parent.afterthegameInterface.player_2.setText(_translate("afterthegame", "未上场"))
        self._parent.afterthegameInterface.player_3.setText(_translate("afterthegame", "未上场"))
        self._parent.afterthegameInterface.player_4.setText(_translate("afterthegame", "未上场"))
        self._parent.afterthegameInterface.player_5.setText(_translate("afterthegame", "未上场"))

    @pyqtSlot()
    def on_radioButton_clicked(self):
        self.subkillorsur.setText(_translate("score", "求生者方"))
        self.setbpplayer(True)
        self.clearafterthegeme_playername()

    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.subkillorsur.setText(_translate("score", "监管者方"))
        self.setbpplayer(False)
        self.clearafterthegeme_playername()

    def msg(self,title, content, yesbutton):
        w = MessageBox(title, content, self.window())
        w.yesButton.setText(yesbutton)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    @pyqtSlot()
    def on_bo_switch_clicked(self):
        if self.bo_id.text() == _translate("score", "赛程已结束"):
            self.msg(_translate("score", "欸？加赛了吗？"), _translate("score", "现在不能切换啦！"), _translate("msgbox", "我知道了"))
            return
        if self.radioButton.isChecked() == False:
            self.radioButton.setChecked(True)
            self.subkillorsur.setText(_translate("score", "求生者方"))
            self.setbpplayer(True)
            self.clearafterthegeme_playername()
        else:
            self.radioButton_2.setChecked(True)
            self.subkillorsur.setText(_translate("score", "监管者方"))
            self.setbpplayer(False)
            self.clearafterthegeme_playername()
        boid = self.bo_id.text()[:3]
        text = self.bo_id.text()[-2:]
        if text == '上半':
            text = _translate("score", "下半")
        elif text == '下半':
            text = _translate("score", "上半")
        self.bo_id.setText(boid + text)

    def setscore(self, killerscore, surscore):
        if self.bo_id.text() == _translate("score", "赛程已结束"):
            self.msg(_translate("score", "欸？加赛了吗？"), _translate("score", "不支持bo6！"), _translate("msgbox", "我知道了"))
            return
        text = self.bo_id.text()[2:4]
        lable_dist = {"1上": 1, "1下": 2, "2上": 3, "2下": 4, "3上": 5, "3下": 6, "4上": 7, "4下": 8, "5上": 9,
                      "5下": 10, }
        x = lable_dist[text]
        if self.radioButton.isChecked() == False:
            killerscore, surscore = surscore, killerscore

        self.table_score.setItem(0, x, QTableWidgetItem(killerscore))
        self.table_score.setItem(1, x, QTableWidgetItem(surscore))

        self.on_bo_switch_clicked()

    @pyqtSlot()
    def on_kill4_clicked(self):
        self.setscore('5', '0')

    @pyqtSlot()
    def on_kill3_clicked(self):
        self.setscore('3', '0')

    @pyqtSlot()
    def on_kill2_clicked(self):
        self.setscore('2', '2')

    @pyqtSlot()
    def on_go3_clicked(self):
        self.setscore('0', '3')

    @pyqtSlot()
    def on_go4_clicked(self):
        self.setscore('0', '5')

    def Get_a_small_score(self, item):
        if item is not None:
            return item.text()
        else:
            self.msg(_translate("score", "欸？算不出来了喵~"), _translate("score", "当前BO存在空数据！"), _translate("msgbox", "回去检查"))
            return ""

    @pyqtSlot()
    def on_bo_over_clicked(self):
        if self.bo_id.text() == _translate("score", "赛程已结束"):
            self.msg(_translate("score", "欸？加赛了吗？"), _translate("score", "不能结算BO6啦！"), _translate("msgbox", "我知道了"))
            return
        num = int(self.bo_id.text()[2])
        newnum = 'BO'+str(num + 1)
        num = num * 2 - 1
        mainup = self.Get_a_small_score(self.table_score.item(0, num))
        if mainup == "":
            return
        maindown = self.Get_a_small_score(self.table_score.item(0, num + 1))
        if maindown == "":
            return
        subup = self.Get_a_small_score(self.table_score.item(1, num))
        if subup == "":
            return
        subdowm = self.Get_a_small_score(self.table_score.item(1, num + 1))
        if subdowm == "":
            return

        mainscore = int(mainup) + int(maindown)
        subscore = int(subup) + int(subdowm)

        if mainscore > subscore:
            bigscore =str(int(self.mainscore.text()[1]) +1)
            self.mainscore.setText(self.mainscore.text()[0]+bigscore+self.mainscore.text()[2:])
            bigscore =str(int(self.subscore.text()[-1]) +1)
            self.subscore.setText(self.subscore.text()[0:-1]+bigscore)

        elif mainscore < subscore:
            bigscore =str(int(self.subscore.text()[1]) +1)
            self.subscore.setText(self.subscore.text()[0]+bigscore+self.subscore.text()[2:])
            bigscore =str(int(self.mainscore.text()[-1]) +1)
            self.mainscore.setText(self.mainscore.text()[0:-1]+bigscore)

        elif mainscore == subscore:
            bigscore = str(int(self.mainscore.text()[4]) + 1)
            self.mainscore.setText(self.mainscore.text()[0:4] + bigscore + self.mainscore.text()[5:])
            bigscore = str(int(self.subscore.text()[4]) + 1)
            self.subscore.setText(self.subscore.text()[0:4] + bigscore + self.subscore.text()[5:])


        if newnum == "BO6":
            self.bo_id.setText(_translate("score", "赛程已结束"))
            return
        text = _translate("score", "上半")
        self.bo_id.setText(newnum + text)

    @pyqtSlot()
    def on_clear_clicked(self):
        self.mainscore.setText(_translate("score", "W0 D0 L0"))
        self.subscore.setText(_translate("score", "W0 D0 L0"))
        self.bo_id.setText(_translate("score", "BO1上半"))
        self.radioButton.setChecked(True)
        for col in range(1, 11):
            for row in range(0, 2):
                # 获取指定单元格的项
                item = self.table_score.item(row, col)
                # 如果该单元格存在，则将其内容设为空字符串
                if item:
                    item.setText("")