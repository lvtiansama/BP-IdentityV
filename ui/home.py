# Form implementation generated from reading ui file 'ui/home.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from function import get_resource_path


class Ui_home(object):
    def setupUi(self, home, parent=None):
        self._parent = parent
        home.setObjectName("home")
        home.resize(1000, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cover = QtWidgets.QLabel(parent=home)
        self.cover.setEnabled(True)
        self.cover.setMinimumSize(QtCore.QSize(600, 240))
        self.cover.setMaximumSize(QtCore.QSize(5000, 240))
        self.cover.setText("")
        self.cover.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.pixmap = QtGui.QPixmap(get_resource_path("data/test.png"))
        self.cover.setPixmap(self.pixmap)
        self.cover.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cover.setObjectName("cover")
        self.verticalLayout.addWidget(self.cover)
        self.updatePixmap()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bp_title = TitleLabel(parent=home)
        self.bp_title.setObjectName("bp_title")
        self.verticalLayout_2.addWidget(self.bp_title)
        self.bp_title_zh = LargeTitleLabel(parent=home)
        self.bp_title_zh.setObjectName("bp_title_zh")
        self.verticalLayout_2.addWidget(self.bp_title_zh)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.version_id = BodyLabel(parent=home)
        self.version_id.setObjectName("version_id")
        self.verticalLayout_2.addWidget(self.version_id)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.port_title = BodyLabel(parent=home)
        self.port_title.setObjectName("port_title")
        self.verticalLayout_3.addWidget(self.port_title)
        self.port_id = BodyLabel(parent=home)
        self.port_id.setObjectName("port_id")
        self.verticalLayout_3.addWidget(self.port_id)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.connection = BodyLabel(parent=home)
        self.connection.setObjectName("connection")
        self.verticalLayout_3.addWidget(self.connection)
        self.connection_status = BodyLabel(parent=home)
        self.connection_status.setObjectName("connection_status")
        self.verticalLayout_3.addWidget(self.connection_status)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.github_label = HyperlinkLabel(parent=home)
        # self.github_label.setUnderlineVisible(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.github_label.sizePolicy().hasHeightForWidth())
        self.github_label.setSizePolicy(sizePolicy)
        self.github_label.setObjectName("github_label")
        self.horizontalLayout_2.addWidget(self.github_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gnu_label = BodyLabel(parent=home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gnu_label.sizePolicy().hasHeightForWidth())
        self.gnu_label.setSizePolicy(sizePolicy)
        self.gnu_label.setObjectName("gnu_label")
        self.horizontalLayout_2.addWidget(self.gnu_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def updatePixmap(self):
        # 获取QLabel的大小
        label_size = self.cover.size()

        # 计算新的大小，并保持纵横比
        new_pixmap = self.pixmap.scaled(label_size,
                                        aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                        transformMode=QtCore.Qt.TransformationMode.SmoothTransformation)

        # 设置新的QPixmap
        self.cover.setPixmap(new_pixmap)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updatePixmap()

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "主页"))
        self.bp_title.setText(_translate("home", "BP IdentityV 3D"))
        self.bp_title_zh.setText(_translate("home", "第五人格BP控制台"))
        self.version_id.setText(_translate("home", f"控制台版本号：{self._parent.version}"))
        self.port_title.setText(_translate("home", "使用的端口号："))
        self.port_id.setText(_translate("home", "正在等待程序分配"))
        self.connection.setText(_translate("home", "连接状态："))
        self.connection_status.setText(_translate("home", "未连接"))
        self.github_label.setText(_translate("home", "项目地址"))
        self.github_label.setUrl('https://github.com/lvtiansama/BP-IdentityV')
        self.gnu_label.setText(_translate("home", "许可证：GNU General Public License v3.0"))
from qfluentwidgets import BodyLabel, HyperlinkLabel, LargeTitleLabel, TitleLabel
