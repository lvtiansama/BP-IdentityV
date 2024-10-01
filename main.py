import sys

from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, toggleTheme, setThemeColor)
from qfluentwidgets import FluentIcon as FIF

from function import get_resource_path
from home_Interface import HomeInterface
from countdown_Interface import CountdownInterface
from frame_Interface import FrameInterface
from introduce_Interface import IntroduceInterface
from score_Interface import ScoreInterface
from banpick_Interface import BanpickInterface
from afterthegame_Interface import AfterthegameInterface
from champion_Interface import ChampionInterface

from library_Interface import LibraryInterface


import appdirs
import os

Surs = ['幸运儿', '医生', '律师', '“慈善家”', '园丁', '魔术师', '冒险家', '佣兵', '空军', '机械师', '前锋', '盲女',
        '祭司', '调香师', '牛仔', '舞女', '先知', '入殓师', '勘探员', '咒术师', '野人', '杂技演员', '大副', '调酒师',
        '邮差', '守墓人', '“囚徒”', '昆虫学者', '画家', '击球手', '玩具商', '“心理学家”', '病患', '小说家', '“小女孩”',
        '哭泣小丑', '教授', '古董商', '作曲家', '记者', '飞行家', '拉拉队员', '木偶师', '火灾调查员', '“法罗女士”']

Killers = ['厂长', '小丑', '鹿头', '“杰克”', '蜘蛛', '红蝶', '黄衣之主', '宿伞之魂', '摄影师', '疯眼', '梦之女巫',
           '爱哭鬼', '孽蜥', '红夫人', '26号守卫', '“使徒”', '小提琴家', '雕刻家', '“博士”', '破轮', '渔女', '蜡像师',
           '“噩梦”', '“记录员”', '隐士', '守夜人', '歌剧演员', '“愚人金”', '时空之影', '“跛脚羊”']

Maps = ['军工厂', '红教堂', '圣心医院', '永眠镇', '唐人街',
    '湖景村', '月亮河公园', '里奥的回忆',
    '白沙街疯人院', '闪金石窟', '不归林', '克雷伯格赛马场']

Version = 'Alpha 1.0.1'

app_name = "BP_Identity_3d"
app_author = "Lvtiansama"
# 获取用户缓存目录
cache_dir = appdirs.user_data_dir(appname=app_name, appauthor=app_author)
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()

        self.surs = Surs
        self.killers = Killers
        self.maps = Maps
        self.version = Version

        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.frameInterface = FrameInterface(self)
        self.countdownInterface = CountdownInterface(self)
        self.introduceInterface = IntroduceInterface(self)
        self.scoreInterface = ScoreInterface(self)
        self.banpickInterface = BanpickInterface(self)
        self.afterthegameInterface = AfterthegameInterface(self)
        self.championInterface = ChampionInterface(self)

        self.libraryInterface = LibraryInterface(self)

        self.initNavigation()
        self.initWindow()


    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页', FIF.HOME_FILL)
        self.addSubInterface(self.frameInterface, FIF.MOVIE, '画面切换')
        self.addSubInterface(self.countdownInterface, FIF.STOP_WATCH, '倒计时')
        self.addSubInterface(self.introduceInterface, FIF.FLAG, '战队展示')
        self.addSubInterface(self.scoreInterface, FIF.APPLICATION, '比分控制')
        self.addSubInterface(self.banpickInterface, FIF.PIN, 'BP')
        self.addSubInterface(self.afterthegameInterface, FIF.VIDEO, '赛后数据')
        self.addSubInterface(self.championInterface, FIF.CERTIFICATE, '冠军')

        self.addSubInterface(self.libraryInterface, FIF.BOOK_SHELF, '战队数据', FIF.LIBRARY_FILL, NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
            routeKey='Light',
            icon=FIF.CONSTRACT,
            text='灯泡',
            onClick=self.Light_bulb,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setCurrentItem(self.homeInterface.objectName())

    def initWindow(self):
        self.resize(1000, 600)
        self.setWindowIcon(QIcon(get_resource_path('icon.jpg')))
        self.setWindowTitle('第五人格BP控制台 demo @绿天sama')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def Light_bulb(self):
        toggleTheme()


if __name__ == '__main__':
    setTheme(Theme.AUTO)
    setThemeColor('#8569BE')

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
