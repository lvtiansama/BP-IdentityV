# Form implementation generated from reading ui file 'ui/library.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from function import get_resource_path


class Ui_library(object):
    def setupUi(self, library):
        library.setObjectName("library")
        library.resize(854, 583)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(library)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label = BodyLabel(parent=library)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.team = ComboBox(parent=library)
        self.team.currentTextChanged.connect(self.on_team_changed)
        self.team.setObjectName("team")
        self.verticalLayout.addWidget(self.team)
        spacerItem2 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = BodyLabel(parent=library)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.human_list = ListWidget(parent=library)
        self.human_list.itemClicked.connect(self.on_human_list_changed)
        self.human_list.setMinimumSize(QtCore.QSize(160, 0))
        self.human_list.setObjectName("human_list")
        self.verticalLayout.addWidget(self.human_list)
        self.label_5 = BodyLabel(parent=library)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_3 = BodyLabel(parent=library)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.new_team = LineEdit(parent=library)
        self.new_team.setObjectName("new_team")
        self.verticalLayout_2.addWidget(self.new_team)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_team = ToolButton(parent=library)
        self.toolButton_team.setObjectName("toolButton_team")
        self.horizontalLayout.addWidget(self.toolButton_team)
        self.toolButton_delteam = PrimaryToolButton(parent=library)
        self.toolButton_delteam.setObjectName("toolButton_delteam")
        self.horizontalLayout.addWidget(self.toolButton_delteam)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label_4 = BodyLabel(parent=library)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.new_human = LineEdit(parent=library)
        self.new_human.setObjectName("new_human")
        self.verticalLayout_2.addWidget(self.new_human)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_human = ToolButton(parent=library)
        self.toolButton_human.setObjectName("toolButton_human")
        self.horizontalLayout_2.addWidget(self.toolButton_human)
        self.toolButton_delhuman = PrimaryToolButton(parent=library)
        self.toolButton_delhuman.setObjectName("toolButton_delhuman")
        self.horizontalLayout_2.addWidget(self.toolButton_delhuman)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.label_6 = BodyLabel(parent=library)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.teamlogo = ImageLabel(parent=library)
        self.teamlogo.setMinimumSize(QtCore.QSize(100, 100))
        self.teamlogo.setMaximumSize(QtCore.QSize(200, 200))
        self.teamlogo.setText("")
        self.teamlogo.setPixmap(QtGui.QPixmap(get_resource_path("data/空logo.png")))
        self.teamlogo.scaledToWidth(100)
        self.teamlogo.setBorderRadius(14, 14, 14, 14)
        self.teamlogo.setScaledContents(True)
        self.teamlogo.setObjectName("teamlogo")
        self.verticalLayout_2.addWidget(self.teamlogo)
        self.label_7 = BodyLabel(parent=library)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.humanlogo = ImageLabel(parent=library)
        self.humanlogo.setMinimumSize(QtCore.QSize(100, 100))
        self.humanlogo.setMaximumSize(QtCore.QSize(200, 200))
        self.humanlogo.setText("")
        self.humanlogo.setPixmap(QtGui.QPixmap(get_resource_path("data/空logo.png")))
        self.humanlogo.scaledToWidth(100)
        self.humanlogo.setBorderRadius(14, 14, 14, 14)
        self.humanlogo.setScaledContents(True)
        self.humanlogo.setObjectName("humanlogo")
        self.verticalLayout_2.addWidget(self.humanlogo)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.out_1 = PushButton(parent=library)
        self.out_1.setObjectName("out_1")
        self.verticalLayout_3.addWidget(self.out_1)
        self.out_all = PushButton(parent=library)
        self.out_all.setObjectName("out_all")
        self.verticalLayout_3.addWidget(self.out_all)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem11)
        self.on_1 = PrimaryPushButton(parent=library)
        self.on_1.setObjectName("on_1")
        self.verticalLayout_3.addWidget(self.on_1)
        self.on_all = PrimaryPushButton(parent=library)
        self.on_all.setObjectName("on_all")
        self.verticalLayout_3.addWidget(self.on_all)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)

        self.retranslateUi(library)
        QtCore.QMetaObject.connectSlotsByName(library)

    def retranslateUi(self, library):
        _translate = QtCore.QCoreApplication.translate
        library.setWindowTitle(_translate("library", "战队数据"))
        self.label.setText(_translate("library", "战队"))
        self.label_2.setText(_translate("library", "成员"))
        self.label_5.setText(_translate("library", "添加/删除成员时，请在左侧选中后再在右侧操作"))
        self.label_3.setText(_translate("library", "新战队名称"))
        self.toolButton_team.setIcon(FIF.ADD)
        self.toolButton_delteam.setIcon(FIF.DELETE)
        self.label_4.setText(_translate("library", "新成员名称"))
        self.toolButton_human.setIcon(FIF.ADD)
        self.toolButton_delhuman.setIcon(FIF.DELETE)
        self.label_6.setText(_translate("library", "当前战队LOGO"))
        self.label_7.setText(_translate("library", "当前成员头像"))
        self.out_1.setText(_translate("library", "导出当前战队数据"))
        self.out_all.setText(_translate("library", "导出所有数据"))
        self.on_1.setText(_translate("library", "导入战队数据"))
        self.on_all.setText(_translate("library", "导入所有数据"))
from qfluentwidgets import BodyLabel, ComboBox, ImageLabel, LineEdit, ListWidget, PrimaryPushButton, PrimaryToolButton, PushButton, ToolButton
from qfluentwidgets import FluentIcon as FIF