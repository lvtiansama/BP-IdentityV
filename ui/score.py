# Form implementation generated from reading ui file 'ui/score.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_score(object):
    def setupUi(self, score):
        score.setObjectName("score")
        score.resize(1000, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(score)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.table_score = TableWidget(parent=score)
        self.table_score.setMinimumSize(QtCore.QSize(900, 114))
        self.table_score.setMaximumSize(QtCore.QSize(900, 114))
        self.table_score.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_score.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_score.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.table_score.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.table_score.setObjectName("table_score")
        self.table_score.setColumnCount(11)
        self.table_score.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(10, item)
        self.table_score.horizontalHeader().setDefaultSectionSize(76)
        self.table_score.verticalHeader().setCascadingSectionResizes(False)
        self.table_score.verticalHeader().setHighlightSections(True)
        self.horizontalLayout_5.addWidget(self.table_score)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_1 = TitleLabel(parent=score)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.bo_id = TitleLabel(parent=score)
        self.bo_id.setObjectName("bo_id")
        self.horizontalLayout_2.addWidget(self.bo_id)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = RadioButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = RadioButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.radioButton)
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.mainname = SubtitleLabel(parent=score)
        self.mainname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainname.setObjectName("mainname")
        self.gridLayout.addWidget(self.mainname, 0, 0, 1, 1)
        self.subkillorsur = BodyLabel(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subkillorsur.sizePolicy().hasHeightForWidth())
        self.subkillorsur.setSizePolicy(sizePolicy)
        self.subkillorsur.setMinimumSize(QtCore.QSize(200, 0))
        self.subkillorsur.setMaximumSize(QtCore.QSize(200, 16777215))
        self.subkillorsur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subkillorsur.setObjectName("subkillorsur")
        self.gridLayout.addWidget(self.subkillorsur, 2, 2, 1, 1)
        self.subname = SubtitleLabel(parent=score)
        self.subname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subname.setObjectName("subname")
        self.gridLayout.addWidget(self.subname, 0, 2, 1, 1)
        self.mainscore = TitleLabel(parent=score)
        self.mainscore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainscore.setObjectName("mainscore")
        self.gridLayout.addWidget(self.mainscore, 1, 0, 1, 1)
        self.subscore = TitleLabel(parent=score)
        self.subscore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subscore.setObjectName("subscore")
        self.gridLayout.addWidget(self.subscore, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.kill4 = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kill4.sizePolicy().hasHeightForWidth())
        self.kill4.setSizePolicy(sizePolicy)
        self.kill4.setMinimumSize(QtCore.QSize(100, 0))
        self.kill4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.kill4.setObjectName("kill4")
        self.horizontalLayout_3.addWidget(self.kill4)
        self.kill3 = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kill3.sizePolicy().hasHeightForWidth())
        self.kill3.setSizePolicy(sizePolicy)
        self.kill3.setMinimumSize(QtCore.QSize(100, 0))
        self.kill3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.kill3.setObjectName("kill3")
        self.horizontalLayout_3.addWidget(self.kill3)
        self.kill2 = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kill2.sizePolicy().hasHeightForWidth())
        self.kill2.setSizePolicy(sizePolicy)
        self.kill2.setMinimumSize(QtCore.QSize(100, 0))
        self.kill2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.kill2.setObjectName("kill2")
        self.horizontalLayout_3.addWidget(self.kill2)
        self.go3 = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go3.sizePolicy().hasHeightForWidth())
        self.go3.setSizePolicy(sizePolicy)
        self.go3.setMinimumSize(QtCore.QSize(100, 0))
        self.go3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.go3.setObjectName("go3")
        self.horizontalLayout_3.addWidget(self.go3)
        self.go4 = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go4.sizePolicy().hasHeightForWidth())
        self.go4.setSizePolicy(sizePolicy)
        self.go4.setMinimumSize(QtCore.QSize(100, 0))
        self.go4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.go4.setObjectName("go4")
        self.horizontalLayout_3.addWidget(self.go4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 1, 2, 1, 1)
        self.label_2 = BodyLabel(parent=score)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.clear = PrimaryPushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setMinimumSize(QtCore.QSize(140, 0))
        self.clear.setMaximumSize(QtCore.QSize(140, 16777215))
        self.clear.setObjectName("clear")
        self.gridLayout_2.addWidget(self.clear, 1, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bo_switch = PushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bo_switch.sizePolicy().hasHeightForWidth())
        self.bo_switch.setSizePolicy(sizePolicy)
        self.bo_switch.setMinimumSize(QtCore.QSize(100, 0))
        self.bo_switch.setMaximumSize(QtCore.QSize(160, 16777215))
        self.bo_switch.setObjectName("bo_switch")
        self.horizontalLayout_4.addWidget(self.bo_switch)
        self.bo_over = PrimaryPushButton(parent=score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bo_over.sizePolicy().hasHeightForWidth())
        self.bo_over.setSizePolicy(sizePolicy)
        self.bo_over.setMinimumSize(QtCore.QSize(100, 0))
        self.bo_over.setMaximumSize(QtCore.QSize(160, 16777215))
        self.bo_over.setObjectName("bo_over")
        self.horizontalLayout_4.addWidget(self.bo_over)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem15)

        self.retranslateUi(score)
        QtCore.QMetaObject.connectSlotsByName(score)

    def retranslateUi(self, score):
        _translate = QtCore.QCoreApplication.translate
        score.setWindowTitle(_translate("score", "比分控制"))
        item = self.table_score.verticalHeaderItem(0)
        item.setText(_translate("score", "主场"))
        item = self.table_score.verticalHeaderItem(1)
        item.setText(_translate("score", "客场"))
        item = self.table_score.horizontalHeaderItem(0)
        item.setText(_translate("score", "战队名"))
        item = self.table_score.horizontalHeaderItem(1)
        item.setText(_translate("score", "BO1上半"))
        item = self.table_score.horizontalHeaderItem(2)
        item.setText(_translate("score", "BO1下半"))
        item = self.table_score.horizontalHeaderItem(3)
        item.setText(_translate("score", "BO2上半"))
        item = self.table_score.horizontalHeaderItem(4)
        item.setText(_translate("score", "BO2下半"))
        item = self.table_score.horizontalHeaderItem(5)
        item.setText(_translate("score", "BO3上半"))
        item = self.table_score.horizontalHeaderItem(6)
        item.setText(_translate("score", "BO3下半"))
        item = self.table_score.horizontalHeaderItem(7)
        item.setText(_translate("score", "BO4上半"))
        item = self.table_score.horizontalHeaderItem(8)
        item.setText(_translate("score", "BO4下半"))
        item = self.table_score.horizontalHeaderItem(9)
        item.setText(_translate("score", "BO5上半"))
        item = self.table_score.horizontalHeaderItem(10)
        item.setText(_translate("score", "BO5下半"))
        self.label_1.setText(_translate("score", "当前场："))
        self.bo_id.setText(_translate("score", "BO1上半"))
        self.radioButton.setText(_translate("score", "监管者方"))
        self.radioButton_2.setText(_translate("score", "求生者方"))
        self.mainname.setText(_translate("score", "主场"))
        self.subkillorsur.setText(_translate("score", "求生者方"))
        self.subname.setText(_translate("score", "客场"))
        self.mainscore.setText(_translate("score", "W0 D0 L0"))
        self.subscore.setText(_translate("score", "W0 D0 L0"))
        self.radioButton.setChecked(True)
        self.kill4.setText(_translate("score", "四抓"))
        self.kill3.setText(_translate("score", "三抓"))
        self.kill2.setText(_translate("score", "平局"))
        self.go3.setText(_translate("score", "三跑"))
        self.go4.setText(_translate("score", "四跑"))
        self.label_2.setText(_translate("score", "请确保本BO计分正确后再点击结算本BO，每一BO结算后无法修改！"))
        self.clear.setText(_translate("score", "重置本页数据"))
        self.bo_switch.setText(_translate("score", "切上/下半场"))
        self.bo_switch.setIcon(FIF.SYNC)
        self.bo_over.setText(_translate("score", "结算本BO"))
        self.bo_over.setIcon(FIF.ACCEPT)
        self.clear.setIcon(FIF.DELETE)

from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import BodyLabel, PrimaryPushButton, PushButton, RadioButton, SubtitleLabel, TableWidget, TitleLabel
