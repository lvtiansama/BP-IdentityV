# coding:utf-8
import json
import shutil

import py7zr

from PyQt6.QtCore import pyqtSlot, QCoreApplication
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QFileDialog, QTableWidgetItem
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon, MessageBox

from function import get_resource_path
from ui.library import Ui_library

import appdirs
import os
from PIL import Image

app_name = "BP_Identity_3d"
app_author = "Lvtiansama"

data_dir = os.path.join(appdirs.user_data_dir(appname=app_name, appauthor=app_author), "Team_Data")
cache_dir = os.path.join(appdirs.user_cache_dir(appname=app_name, appauthor=app_author))
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

_translate = QCoreApplication.translate

class LibraryInterface(Ui_library, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._parent = parent
        self.setupUi(self)
        self.refresh_team()

    def msg(self,title, content, yesbutton):
        w = MessageBox(title, content, self.window())
        w.yesButton.setText(yesbutton)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    def upteam(self,teamname):
        bpplayers = (self._parent.banpickInterface.player, self._parent.banpickInterface.player_2,
                     self._parent.banpickInterface.player_3, self._parent.banpickInterface.player_4)
        winplayers = (self._parent.championInterface.player, self._parent.championInterface.player_2,
                      self._parent.championInterface.player_3,
                      self._parent.championInterface.player_4, self._parent.championInterface.player_5,
                      self._parent.championInterface.player_6)
        if teamname == self._parent.introduceInterface.main_team.text():
            players = (self._parent.introduceInterface.main_player, self._parent.introduceInterface.main_player_2, self._parent.introduceInterface.main_player_3,
                       self._parent.introduceInterface.main_player_4, self._parent.introduceInterface.main_player_5, self._parent.introduceInterface.main_player_6)
            for player in players:
                player.clear()
            self._parent.introduceInterface.main_team.setText(_translate("introduce", "当前无战队上场"))
            self._parent.scoreInterface.table_score.setItem(0, 0, QTableWidgetItem(''))
            self._parent.scoreInterface.mainname.setText(_translate("score", "主场"))
            if self._parent.scoreInterface.radioButton.isChecked() == True:
                self._parent.banpickInterface.player_5.clear()
            else:
                for player in bpplayers:
                    player.clear()
        if teamname == self._parent.introduceInterface.sub_team.text():
            players = (self._parent.introduceInterface.sub_player, self._parent.introduceInterface.sub_player_2, self._parent.introduceInterface.sub_player_3,
                       self._parent.introduceInterface.sub_player_4, self._parent.introduceInterface.sub_player_5, self._parent.introduceInterface.sub_player_6)
            for player in players:
                player.clear()
            self._parent.introduceInterface.sub_team.setText(_translate("introduce", "当前无战队上场"))
            self._parent.scoreInterface.table_score.setItem(1, 0, QTableWidgetItem(''))
            self._parent.scoreInterface.mainname.setText(_translate("score", "客场"))
            if self._parent.scoreInterface.radioButton.isChecked() == True:
                for player in bpplayers:
                    player.clear()
            else:
                self._parent.banpickInterface.player_5.clear()
        if teamname == self._parent.championInterface.teamname.text():
            self._parent.championInterface.teamname.setText(_translate("champion", "当前无战队上场"))
            for player in winplayers:
                player.clear()

    # 当选手发生变更（删除新增）时调用
    def upgamer(self,teamname):
        bpplayers = (self._parent.banpickInterface.player, self._parent.banpickInterface.player_2,
                     self._parent.banpickInterface.player_3,self._parent.banpickInterface.player_4)
        winplayers = (self._parent.championInterface.player, self._parent.championInterface.player_2, self._parent.championInterface.player_3,
                   self._parent.championInterface.player_4, self._parent.championInterface.player_5, self._parent.championInterface.player_6)
        name_list = self.refresh_player(teamname,True)
        name_list.insert(0, '')

        if teamname == self._parent.introduceInterface.main_team.text():
            players = (self._parent.introduceInterface.main_player, self._parent.introduceInterface.main_player_2, self._parent.introduceInterface.main_player_3,
                       self._parent.introduceInterface.main_player_4, self._parent.introduceInterface.main_player_5, self._parent.introduceInterface.main_player_6)
            for player in players:
                player.clear()
                for name in name_list:
                    player.addItem(name)
            if self._parent.scoreInterface.radioButton.isChecked() == True:
                self._parent.banpickInterface.player_5.clear()
                for name in name_list:
                    self._parent.banpickInterface.player_5.addItem(name)
            else:
                for player in bpplayers:
                    player.clear()
                    for name in name_list:
                        player.addItem(name)
        if teamname == self._parent.introduceInterface.sub_team.text():
            players = (self._parent.introduceInterface.sub_player, self._parent.introduceInterface.sub_player_2, self._parent.introduceInterface.sub_player_3,
                       self._parent.introduceInterface.sub_player_4, self._parent.introduceInterface.sub_player_5, self._parent.introduceInterface.sub_player_6)
            for player in players:
                player.clear()
                for name in name_list:
                    player.addItem(name)
            if self._parent.scoreInterface.radioButton.isChecked() == True:
                for player in bpplayers:
                    player.clear()
                    for name in name_list:
                        player.addItem(name)
            else:
                self._parent.banpickInterface.player_5.clear()
                for name in name_list:
                    self._parent.banpickInterface.player_5.addItem(name)
        if teamname == self._parent.championInterface.teamname.text():
            for player in winplayers:
                player.clear()
                for name in name_list:
                    player.addItem(name)

    # 导出当前战队
    @pyqtSlot()
    def on_out_1_clicked(self):
        teamname = self.team.currentText()
        path = self.getsavepath('请选择导出的存档文件的目标文件夹')
        if path is None:
            self.msg(_translate("library", "不导出了嘛"), _translate("library", "用户取消了存档！"),
                     _translate("msgbox", "我知道了"))
            return
        path = os.path.join(path, f"{teamname}.lvtianbpsave1")

        # 构建源文件夹路径
        source_folder = os.path.join(data_dir, teamname)
        source_json = os.path.join(data_dir, f"{teamname}.json")

        # 构建目标压缩文件路径
        target_7z = os.path.join(cache_dir, f"{teamname}.7z")
        target_lvtianbpsave1 = os.path.join(cache_dir, f"{teamname}.lvtianbpsave1")

        try:
            # 创建 7z 文件对象
            with py7zr.SevenZipFile(target_7z, 'w') as archive:
                # 将文件夹添加到压缩文件中
                archive.writeall(source_folder, arcname=teamname)
                # 将 JSON 文件添加到压缩文件中
                archive.write(source_json, arcname=f"{teamname}.json")

            # 重命名压缩文件
            os.rename(target_7z, target_lvtianbpsave1)

            # 复制文件
            shutil.copy2(target_lvtianbpsave1, path)

            # 删除源文件
            os.remove(target_lvtianbpsave1)

            self.msg(_translate("library", "好耶"), _translate("library", f"成功导出了{teamname} 的存档文件！"),
                     _translate("msgbox", "我知道了"))

        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导出存档时发生错误"),
                     _translate("msgbox", "我知道了"))
            if os.path.exists(target_7z):
                os.remove(target_7z)
            if os.path.exists(target_lvtianbpsave1):
                os.remove(target_lvtianbpsave1)

    # 导出所有战队
    @pyqtSlot()
    def on_out_all_clicked(self):
        path = self.getsavepath('请选择导出的存档文件的目标文件夹')
        if path is None:
            self.msg(_translate("library", "不导出了嘛"), _translate("library", "用户取消了存档！"),
                     _translate("msgbox", "我知道了"))
            return
        path = os.path.join(path, "save.lvtianbpsave")

        # 构建目标压缩文件路径
        target_7z = os.path.join(cache_dir, f"save.7z")
        target_lvtianbpsave = os.path.join(cache_dir, "save.lvtianbpsave")

        try:
            # 创建 7z 文件对象
            with py7zr.SevenZipFile(target_7z, 'w') as archive:
                # 将文件夹添加到压缩文件中
                archive.writeall(data_dir, arcname='save')


            # 重命名压缩文件
            os.rename(target_7z, target_lvtianbpsave)

            # 复制文件
            shutil.copy2(target_lvtianbpsave, path)

            # 删除源文件
            os.remove(target_lvtianbpsave)

            self.msg(_translate("library", "好耶"), _translate("library", f"成功导出了包含所有数据的存档文件！"),
                     _translate("msgbox", "我知道了"))

        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导出存档时发生错误"),
                     _translate("msgbox", "我知道了"))
            if os.path.exists(target_7z):
                os.remove(target_7z)
            if os.path.exists(target_lvtianbpsave):
                os.remove(target_lvtianbpsave)

    def clear_bad_cache(self, name):
        if os.path.exists(name):
            shutil.rmtree(name)

    # 导入一个战队
    @pyqtSlot()
    def on_on_1_clicked(self):
        path = self.getsavedata1()
        # 等待导入的存档目录
        if path is None:
            self.msg(_translate("library", "不导入了嘛"), _translate("library", "用户取消了导入！"),
                     _translate("msgbox", "我知道了"))
            return
        if not path.endswith('.lvtianbpsave1'):
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "错误的后缀名 ID：0-0"),
                     _translate("msgbox", "我知道了"))
            return
        try:
            # 打开文件并读取前几个字节
            with open(path, 'rb') as file:
                signature = file.read(2)
            if signature != b'7z':
                self.msg(_translate("library", "呜~出错了~"), _translate("library", "错误的存档格式 ID：0-1"),
                         _translate("msgbox", "我知道了"))
                return
        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导入存档时发生错误 ID：1-0"),
                     _translate("msgbox", "我知道了"))
            return

        try:
            # 尝试打开并解压文件
            with py7zr.SevenZipFile(path, mode='r') as archive:

                # 获取文件名（包含后缀）
                basename = os.path.basename(path)

                # 不含后缀的纯文件名
                filename_without_ext, _ = os.path.splitext(basename)

                # 缓存文件夹地址
                cache_dir_path = os.path.join(cache_dir, filename_without_ext)

                if not os.path.exists(path):
                    os.makedirs(path)
                # 解压到指定目录
                archive.extractall(path=cache_dir_path)


        except:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导入存档时发生错误 ID：1-1"),
                     _translate("msgbox", "我知道了"))
            self.clear_bad_cache(cache_dir_path)
            return

        # 检测图片指向是否正确
        try:
            # 读取 JSON 文件
            with open(os.path.join(cache_dir_path, f"{filename_without_ext}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
                logo = data["logo"]
                if self.pic_is_ok(cache_dir_path, logo) == False:
                    self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：2"),
                             _translate("msgbox", "我知道了"))
                    self.clear_bad_cache(cache_dir_path)
                    return
                for player in data["player"]:
                    logo = player.get("logo")
                    if self.pic_is_ok(cache_dir_path, logo) == False:
                        self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：2"),
                                 _translate("msgbox", "我知道了"))
                        self.clear_bad_cache(cache_dir_path)
                        return
        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "检查导入数据时发生错误！"),
                     _translate("msgbox", "我知道了"))
            print(f"Error processing: {e}")
            self.clear_bad_cache(cache_dir_path)
            return

        # 检测是否有文件夹+json
        if self.check_folder_or_json_exists(cache_dir_path, filename_without_ext, True) == False:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：2"),
                     _translate("msgbox", "我知道了"))
            self.clear_bad_cache(cache_dir_path)
            return

        # json格式
        if self.validate_json_file(os.path.join(cache_dir_path, f"{filename_without_ext}.json")) == False:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：3"),
                     _translate("msgbox", "我知道了"))
            self.clear_bad_cache(cache_dir_path)
            return

        if self.check_folder_or_json_exists(data_dir, filename_without_ext, False) == True:
            w = MessageBox(_translate("library", f"存档导入：存在已有的同名战队"),
                           _translate("library", "继续导入会替换原有战队数据（原数据无法被恢复）"), self.window())
            w.yesButton.setText("继续")
            w.cancelButton.setText("取消")
            if w.exec():
                # 构建完整的路径
                target_json_path = os.path.join(data_dir, f"{filename_without_ext}.json")
                target_folder_path = os.path.join(data_dir, filename_without_ext)
                # 删除JSON文件
                if os.path.exists(target_json_path):
                    os.remove(target_json_path)
                # 删除文件夹及其内容
                if os.path.exists(target_folder_path) and os.path.isdir(target_folder_path):
                    shutil.rmtree(target_folder_path)
            else:
                self.msg(_translate("library", "不导入了嘛"), _translate("library", "用户取消了导入！"),
                         _translate("msgbox", "我知道了"))
                self.clear_bad_cache(cache_dir_path)
                return

        # 构建文件夹路径
        folder_path = os.path.join(cache_dir_path, filename_without_ext)
        # 构建 JSON 文件路径
        json_path = os.path.join(cache_dir_path, f"{filename_without_ext}.json")

        # 构建目标文件夹路径
        target_folder_path = os.path.join(data_dir, filename_without_ext)
        # 构建目标 JSON 文件路径
        target_json_path = os.path.join(data_dir, f"{filename_without_ext}.json")

        # 移动文件夹
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.move(folder_path, target_folder_path)

        # 移动 JSON 文件
        if os.path.exists(json_path) and os.path.isfile(json_path):
            shutil.move(json_path, target_json_path)

        self.refresh_team()     #刷新列表
        self.msg(_translate("library", "好耶"), _translate("library", f"成功导入了战队{filename_without_ext}的存档数据！"),
                 _translate("msgbox", "我知道了"))
        self.clear_bad_cache(cache_dir_path)
        return

    # 导入所有战队
    @pyqtSlot()
    def on_on_all_clicked(self):
        path = self.getsavedata()
        # 等待导入的存档目录
        if path is None:
            self.msg(_translate("library", "不导入了嘛"), _translate("library", "用户取消了导入！"),
                     _translate("msgbox", "我知道了"))
            return
        if not path.endswith('.lvtianbpsave'):
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "错误的后缀名 ID：0-0"),
                     _translate("msgbox", "我知道了"))
            return
        try:
            # 打开文件并读取前几个字节
            with open(path, 'rb') as file:
                signature = file.read(2)
            if signature != b'7z':
                self.msg(_translate("library", "呜~出错了~"), _translate("library", "错误的存档格式 ID：0-1"),
                         _translate("msgbox", "我知道了"))
                return
        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导入存档时发生错误 ID：1-0"),
                     _translate("msgbox", "我知道了"))
            return

        try:
            # 尝试打开并解压文件
            with py7zr.SevenZipFile(path, mode='r') as archive:

                # 获取文件名（包含后缀）
                basename = os.path.basename(path)

                # 缓存文件夹地址
                cache_dir_path = os.path.join(cache_dir, "save")

                if not os.path.exists(path):
                    os.makedirs(path)
                # 解压到指定目录
                archive.extractall(path=cache_dir)


        except:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "导入存档时发生错误 ID：1-1"),
                     _translate("msgbox", "我知道了"))
            self.clear_bad_cache(cache_dir_path)
            return

        # 检测是否有文件夹+json 同时检查数量 logo、队员头像
        if self.check_folders_and_json_files(cache_dir_path) == False:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：2"),
                     _translate("msgbox", "我知道了"))
            self.clear_bad_cache(cache_dir_path)
            return

        # json格式
        files = os.listdir(cache_dir_path)
        for file_name in files:
            # 检查是否为 .json 文件
            if file_name.endswith('.json'):
                if self.validate_json_file(os.path.join(cache_dir_path, file_name)) == False:
                    self.msg(_translate("library", "呜~出错了~"), _translate("library", "存档数据破损！ID：3"),
                             _translate("msgbox", "我知道了"))
                    self.clear_bad_cache(cache_dir_path)
                    return


        if os.listdir(data_dir):
            w = MessageBox(_translate("library", f"存档导入：当前计算机已有存档数据"),
                           _translate("library", "导入外来数据包会清空本地原有数据（原数据无法被恢复）"), self.window())
            w.yesButton.setText("继续")
            w.cancelButton.setText("取消")
            if w.exec():
                if os.path.exists(data_dir) and os.path.isdir(data_dir):
                    shutil.rmtree(data_dir)
                    os.makedirs(data_dir)
            else:
                self.msg(_translate("library", "不导入了嘛"), _translate("library", "用户取消了导入！"),
                         _translate("msgbox", "我知道了"))
                self.clear_bad_cache(cache_dir_path)
                return

        json_files = [f for f in os.listdir(cache_dir_path) if f.endswith('.json')]

        # 获取 cache_dir_path 下的所有文件和文件夹
        items = os.listdir(cache_dir_path)
        # 遍历所有文件和文件夹
        for item in items:
            src_path = os.path.join(cache_dir_path, item)
            dst_path = os.path.join(data_dir, item)

            try:
                # 移动文件或文件夹
                shutil.move(src_path, dst_path)
            except Exception as e:
                print(f"移动文件 {src_path} 出错：{e}")
                self.msg(_translate("library", "呜~出错了~"), _translate("library", "导入存档时发生错误 ID：1-2"),
                         _translate("msgbox", "我知道了"))
                self.clear_bad_cache(cache_dir_path)
                return

        self.refresh_team()     #刷新列表

        self.msg(_translate("library", "好耶"), _translate("library", f"成功导入了来自外部的 {len(json_files)}个战队 存档数据！"),
                 _translate("msgbox", "我知道了"))
        self.clear_bad_cache(cache_dir_path)


        self._parent.close()
        # 重新创建并显示新的窗口
        self._parent.__init__()
        self._parent.show()

        return

    def check_folders_and_json_files(self, directory):
        # 获取目录下的所有文件夹
        folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

        # 获取目录下的所有 .json 文件
        json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

        # 比较文件夹和 .json 文件的数量
        if len(folders) != len(json_files):
            return False

        # 检查文件夹名称和 .json 文件名称是否一一对应
        for folder in folders:
            json_file_name = folder + '.json'
            if json_file_name not in json_files:
                return False

        for entry in os.scandir(directory):
            # 检查条目是否为文件，并且扩展名为 .json
            if entry.is_file() and entry.name.endswith('.json'):
                try:
                    # 读取 JSON 文件
                    with open(entry.path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        logo = data["logo"]
                        if self.pic_is_ok(directory, logo) == False:
                            return False
                        for player in data["player"]:
                            logo = player.get("logo")
                            if self.pic_is_ok(directory, logo) == False:
                                return False
                except Exception as e:
                    self.msg(_translate("library", "呜~出错了~"), _translate("library", "检查导入数据时发生错误！"),
                             _translate("msgbox", "我知道了"))
                    print(f"Error processing {entry.path}: {e}")
                    return False
        return True

    def pic_is_ok(self, directory, pic):
        if pic:
            pic = os.path.join(directory, pic)
            if os.path.exists(pic):
                try:
                    img = Image.open(pic)
                    width, height = img.size

                    # 检查图片尺寸是否符合要求
                    if width != height or width < 512 or height < 512:
                        self.msg(_translate("library", "欸，奇怪的图片~"),
                                 _translate("library", "导入的数据库存在异常大小的图片\n请不要擅自修改数据文件！"),
                                 _translate("msgbox", "我知道了"))
                        return False

                except IOError:
                    self.msg(_translate("library", "呜~出错了~"),
                             _translate("library", "检查数据图片时出错"),
                             _translate("msgbox", "我知道了"))
                    return False
            else:
                self.msg(_translate("library", "呜~出错了~"),
                         _translate("library", "导入的数据库存在丢失的图片指向\n请不要擅自修改数据文件！"),
                         _translate("msgbox", "我知道了"))
                return False
        else:
            self.msg(_translate("library", "呜~出错了~"),
                     _translate("library", "导入的数据库存在空指向\n请不要擅自修改数据文件！"),
                     _translate("msgbox", "我知道了"))
            return False
        return True

    def validate_json_file(self, file_path):
        try:
            # 读取 JSON 文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # 检查根级别的键
            if "name" not in data or "logo" not in data or "player" not in data:
                return False

            # 检查根级别的值类型
            if not isinstance(data["name"], str) or not isinstance(data["logo"], str) or not isinstance(data["player"],
                                                                                                        list):
                return False

            # 检查 player 列表中的每个元素
            for player in data["player"]:
                if not isinstance(player, dict) or "name" not in player or "logo" not in player:
                    return False

                if not isinstance(player["name"], str) or not isinstance(player["logo"], str):
                    return False

            return True

        except (json.JSONDecodeError, FileNotFoundError) as e:
            # JSON 解析失败或文件不存在
            print(f"文件 {file_path} 解析失败或不存在：{e}")
            return False

    def check_folder_or_json_exists(self, data, name,cache):
        folder = False
        json = False

        # 构建文件夹路径
        folder_path = os.path.join(data, name)

        # 构建 JSON 文件路径
        json_path = os.path.join(data, f"{name}.json")

        # 检查是否存在同名文件夹
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            folder = True

        # 检查是否存在同名 JSON 文件
        if os.path.exists(json_path) and os.path.isfile(json_path):
            json = True

        if cache == True:
            if json == True and folder == True:
                return True
        elif cache == False:
            if json == True or folder == True:
                return True

        return False

    def getsavedata(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "请选择要导入的存档文件",
                "",
                "多个战队存档文件 (*.lvtianbpsave)"
            )
            if file_name:
                return file_name
            else:
                return None
        except Exception as e:
            return None

    def getsavedata1(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "请选择要导入的存档文件",
                "",
                "单个战队存档文件 (*.lvtianbpsave1)"
            )
            if file_name:
                return file_name
            else:
                return None
        except Exception as e:
            return None

    def getsavepath(self, text):
        try:
            directory = QFileDialog.getExistingDirectory(
                self,
                text,
                ""
            )
            if directory:
                return directory
            else:
                return None
        except Exception as e:
            return None


    def refresh_team(self):
        # names_list = []
        self.team.clear()
        self._parent.introduceInterface.sub_combobox.clear()
        self._parent.introduceInterface.main_combobox.clear()
        self._parent.championInterface.combobox.clear()
        # 遍历指定目录下的所有条目
        for entry in os.scandir(data_dir):
            # 检查条目是否为文件，并且扩展名为 .json
            if entry.is_file() and entry.name.endswith('.json'):
                try:
                    # 读取 JSON 文件
                    with open(entry.path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        if 'name' in data:
                            name = data['name']
                            self.team.addItem(name)
                            self._parent.introduceInterface.sub_combobox.addItem(name)
                            self._parent.introduceInterface.main_combobox.addItem(name)
                            self._parent.championInterface.combobox.addItem(name)
                except Exception as e:
                    self.msg(_translate("library", "呜~出错了~"), _translate("library", "初始化战队数据时发生错误！"),
                             _translate("msgbox", "我知道了"))
                    print(f"Error processing {entry.path}: {e}")
        self.refresh_player(self.team.currentText())

    def refresh_player(self, teamname ,Bool = False):
        # none好像是无效的，但是还是保留了
        if teamname is None or teamname == "":
            return
        try:
            with open(os.path.join(data_dir, f"{teamname}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading: {e}")
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "读取战队选手数据时发生错误！"),
                     _translate("msgbox", "我知道了"))

        if data['player'] and isinstance(data['player'], list):
            name_list = [player['name'] for player in data['player'] if 'name' in player]
        else:
            name_list = []
        if Bool == False:
            self.human_list.clear()
            self.human_list.clearSelection()
            for name in name_list:
                self.human_list.addItem(name)
        elif Bool == True:
            return name_list

    # 上传json
    def create_json_file(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def getpath(self, name):
        try:
            file_name, imgType = QFileDialog.getOpenFileName(
                self,
                f"请选择{name}的图标",
                "",
                "PNG图片 (*.png);;JPG图片 (*.jpg)"
            )
            if file_name:
                return file_name
            else:
                return None
        except Exception as e:
            return None

    # 上传图片 name是图片名，oldp是完整用户上传的图片路径， newp是新图位置不含data_dir
    def openpic(self, name ,oldp ,newp):
        if oldp is None:
            self.msg(_translate("library", "不添加了嘛"), _translate("library", "用户取消了上传！"),
                     _translate("msgbox", "我知道了"))
            return
        try:
            img = Image.open(oldp)
            width, height = img.size
        except IOError:
            self.msg(_translate("library", "呜~出错了~"),
                     _translate("library", "图片没有被正确打开！（文件不存在、路径错误、文件格式错误、权限问题等）"),
                     _translate("msgbox", "我知道了"))
            return None

        # 检查图片尺寸是否符合要求
        if width != height or width < 512 or height < 512:
            self.msg(_translate("library", "欸，奇怪的图片~"),
                     _translate("library", "图片不符合要求！\n（长宽比需要1:1，长宽像素大于512）"),
                     _translate("msgbox", "我知道了"))
            return None

        picpath = os.path.join(newp, f'{name}.png')
        try:
            if not os.path.exists(os.path.join(data_dir, newp)):
                os.makedirs(os.path.join(data_dir, newp))
            datadir_picpath = os.path.join(data_dir, picpath)
            img.save(datadir_picpath, format='PNG')
            self.msg(_translate("library", "好耶！"), _translate("library", "上传成功！"),
                     _translate("msgbox", "我知道了"))
            return picpath
        except Exception as e:
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "图片上传时出现错误！"),
                     _translate("msgbox", "我知道了"))
            return None

    # 上传选手数据
    @pyqtSlot()
    def on_toolButton_human_clicked(self):
        teamname = self.team.currentText()
        humanname = self.new_human.text()
        if humanname == "":
            self.msg(_translate("library", "欸？马冬梅？"), _translate("library", "你没有告诉我选手名欸！"), _translate("msgbox", "我知道了"))
            return
        if teamname == "":
            self.msg(_translate("library", "这个人要去哪呀？"), _translate("library", "未选中战队！"), _translate("msgbox", "我知道了"))
            return

        try:
            with open(os.path.join(data_dir, f"{teamname}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading: {e}")
            self.msg(_translate("library", "呜~出错了~"), _translate("library", "读取数据文件时发生错误！"),
                     _translate("msgbox", "我知道了"))

        # 检查是否已存在同名玩家
        if 'player' in data and isinstance(data['player'], list):
            for player in data['player']:
                if 'name' in player and player['name'] == humanname:
                    self.msg(_translate("library", "怎么放不进去"), _translate("library", "该选手已存在！"),
                             _translate("msgbox", "我知道了"))
                    return

        team_dir = os.path.join(teamname)
        path = self.getpath(humanname)
        logopath = self.openpic(humanname, path, team_dir)
        if logopath is None:
            return

        new_player = {
            "name": humanname,
            "logo": logopath,
        }
        # 确保 'players' 是一个列表
        if 'player' in data and isinstance(data['player'], list):
            # 向列表中添加新的字典条目
            data['player'].append(new_player)
        self.create_json_file(data, os.path.join(data_dir, f"{teamname}.json"))
        self.refresh_player(self.team.currentText())
        self.upgamer(teamname)

    # 上传战队数据
    @pyqtSlot()
    def on_toolButton_team_clicked(self):
        nowteamdata = self.team.currentText()
        teamname = self.new_team.text()
        if teamname == "":
            self.msg(_translate("library", "欸？马冬梅？"), _translate("library", "你没有告诉我战队名欸！"),
                     _translate("msgbox", "我知道了"))
            return
        if os.path.exists(os.path.join(data_dir, f"{teamname}.json")):
            self.msg(_translate("library", "怎么放不进去"), _translate("library", "该战队已存在！"),
                     _translate("msgbox", "我知道了"))
            return

        team_dir = os.path.join(teamname)
        path = self.getpath(teamname)
        logopath = self.openpic(teamname, path, team_dir)
        if logopath is None:
            return
        data = {
            "name": teamname,
            "logo": logopath,
            "player": []
        }
        self.create_json_file(data, os.path.join(data_dir, f"{teamname}.json"))
        self.refresh_team()
        self.team.setCurrentText(nowteamdata)

    # 删除选手数据
    @pyqtSlot()
    def on_toolButton_delhuman_clicked(self):
        if self.human_list.currentItem() is None:
            self.msg(_translate("library", "欸？马冬梅？"), _translate("library", "你没有选中要删除的选手！"),
                     _translate("msgbox", "我知道了"))
            return
        humanname = self.human_list.currentItem().text()
        teamname = self.team.currentText()
        w = MessageBox(_translate("library", f"你确定要删除 {humanname} 选手吗"), _translate("library", "删除操作不可逆！"), self.window())
        w.yesButton.setText("确认")
        w.cancelButton.setText("取消")
        if w.exec():
            file_path = os.path.join(data_dir, f"{teamname}.json")

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error reading: {e}")
                self.msg(_translate("library", "呜~出错了~"), _translate("library", "读取数据文件时发生错误！"),
                         _translate("msgbox", "我知道了"))
                return

            # 检查是否已存在同名玩家
            if 'player' in data and isinstance(data['player'], list):
                # 检查是否已存在同名玩家，并删除
                if 'player' in data and isinstance(data['player'], list):
                    # 使用列表推导式删除具有特定 name 的字典
                    data['player'] = [player for player in data['player'] if player.get('name') != humanname]
                    # 写入 JSON 文件
                    self.create_json_file(data, file_path)
                    self.refresh_player(teamname)
                    self.msg(_translate("library", "删除成功！"),
                             _translate("library", f"{humanname} 选手已被删除"),
                             _translate("msgbox", "我知道了"))
                    self.upgamer(teamname)
                    self.humanlogo.setPixmap(QPixmap(get_resource_path("data/空logo.png")))
                    self.humanlogo.scaledToWidth(100)
                else:
                    self.msg(_translate("library", "呜~出错了~"), _translate("library", "没有在数据文件中找到对应数据！\n可能数据文件被人非法修改！"),
                             _translate("msgbox", "我知道了"))
        else:
            return

    # 删除战队数据
    @pyqtSlot()
    def on_toolButton_delteam_clicked(self):
        teamname = self.team.currentText()
        if teamname is None or teamname == "":
            self.msg(_translate("library", "欸？马冬梅？"), _translate("library", "你没有选中要删除的战队！"),
                     _translate("msgbox", "我知道了"))
            return
        w = MessageBox(_translate("library", f"你确定要删除 {teamname} 战队的所有数据吗"), _translate("library", "删除操作不可逆！\n删除战队会一起删除该战队选手信息！"), self.window())
        w.yesButton.setText("确认")
        w.cancelButton.setText("取消")
        if w.exec():
            # 构建完整的路径
            json_file_path = os.path.join(data_dir, f"{teamname}.json")
            folder_path = os.path.join(data_dir, teamname)

            # 删除JSON文件
            if os.path.exists(json_file_path):
                os.remove(json_file_path)
            # 删除文件夹及其内容
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
            self.refresh_team()
            self.msg(_translate("library", "删除成功！"),
                     _translate("library", f"{teamname} 战队的所有数据已被删除"),
                     _translate("msgbox", "我知道了"))
            self.upteam(teamname)
            if self.team.currentText() == '':
                self.teamlogo.setPixmap(QPixmap(get_resource_path("data/空logo.png")))
                self.teamlogo.scaledToWidth(100)
        else:
            return


    # 当战队选项变更
    @pyqtSlot()
    def on_team_changed(self):
        team = self.team.currentText()
        self.humanlogo.setPixmap(QPixmap(get_resource_path("data/空logo.png")))
        self.humanlogo.scaledToWidth(100)
        if team == '':
            return
        self.refresh_player(team)
        with open(os.path.join(data_dir, f"{team}.json"), 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.teamlogo.setPixmap(QPixmap(os.path.join(data_dir, data['logo'])))
        self.teamlogo.scaledToWidth(100)

    # 当选手选项变更
    @pyqtSlot()
    def on_human_list_changed(self):
        team = self.team.currentText()
        player = self.human_list.currentItem().text()
        with open(os.path.join(data_dir, f"{team}.json"), 'r', encoding='utf-8') as file:
            data = json.load(file)
        member = next((m for m in data['player'] if m.get('name') == player), None)
        self.humanlogo.setPixmap(QPixmap(os.path.join(data_dir, member['logo'])))
        self.humanlogo.scaledToWidth(100)
