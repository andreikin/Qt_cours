import os
import subprocess
import sys
import re

sys.path.append("//cacheServer/Project/lib/remoteExecution/lib/setup/maya")
sys.path.append('//cacheServer/Project/lib/remoteExecution/lib/setup/maya_apps/Packages/default/win32/')

from PySide2.QtWidgets import QWidget, QComboBox, QApplication, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QGroupBox, QPushButton, QLineEdit, QScrollArea, QSpinBox
from Core.Environment import Project
from PySide2.QtCore import Qt

RIGHT_PART_WIDTH = 200


class AddEpisodes_UI(QMainWindow):
    def __init__(self):
        super(AddEpisodes_UI, self).__init__()

        self.episod_scenes_dict = dict()
        self.current_episod_list = []

        self.setWindowTitle("Add episode, series or scene ")
        self.setFixedSize(350, 530)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.mainLayout = QVBoxLayout(self.central_widget)

        # Select project part
        self.prj_frame = QGroupBox("Project")
        self.prj_frame.setLayout(QGridLayout())
        self.prj_frame.layout().setSpacing(8)

        self.proj_label = QLabel("Project name: ")
        self.prj_frame.layout().addWidget(self.proj_label, 0, 0, 1, 2, alignment=Qt.AlignRight)
        self.project_combobox = QComboBox()
        self.project_combobox.setFixedWidth(RIGHT_PART_WIDTH)
        self.prj_frame.layout().addWidget(self.project_combobox, 0, 2, 1, 2, alignment=Qt.AlignLeft)
        for i, prj in enumerate(Project):
            self.project_combobox.addItem(prj.name)
            self.project_combobox.setItemData(i, prj.path, role=Qt.UserRole)
            self.project_combobox.setItemData(i, prj.full, role=Qt.UserRole + 1)  # is project a full-length
        self.project_combobox.currentIndexChanged.connect(self.path_label_update)

        self.project = self.project_combobox.itemData(0, role=Qt.UserRole)
        self.path_label = QLabel("Path: ")
        self.prj_frame.layout().addWidget(self.path_label, 1, 0, 1, 2, alignment=Qt.AlignRight)
        self.path_picer_label = QLabel()
        self.path_picer_label.setFixedWidth(RIGHT_PART_WIDTH)
        self.prj_frame.layout().addWidget(self.path_picer_label, 1, 2, 1, 2, alignment=Qt.AlignCenter)

        self.location_bttn = QPushButton('Open project directory')
        self.location_bttn.clicked.connect(self.open_file_location)
        self.prj_frame.layout().addWidget(self.location_bttn, 2, 0, 1, 4)
        self.mainLayout.addWidget(self.prj_frame, alignment=Qt.AlignTop)

        # Add episode/seria part
        self.add_ep_group_box = QGroupBox()
        self.add_ep_group_box.setLayout(QGridLayout())
        self.add_ep_group_box.layout().setSpacing(8)

        self.seria_label = QLabel("Seria: ")
        self.add_ep_group_box.layout().addWidget(self.seria_label, 0, 0, 1, 2, alignment=Qt.AlignRight)

        self.seria_line_edit = QLineEdit("001")
        self.seria_line_edit.setFixedWidth(RIGHT_PART_WIDTH)
        self.add_ep_group_box.layout().addWidget(self.seria_line_edit, 0, 2, 1, 2, alignment=Qt.AlignLeft)
        self.seria_line_edit.editingFinished.connect(self.update_curent_episodes)

        self.episode_label = QLabel("Episodes range: ")
        self.add_ep_group_box.layout().addWidget(self.episode_label, 1, 0, 1, 2, alignment=Qt.AlignRight)
        self.episode_range_line_edit = QLineEdit()
        self.episode_range_line_edit.setPlaceholderText("Input episodes sequence (1, 2, 5-10, 12, 15, 20)")
        self.episode_range_line_edit.setFixedWidth(RIGHT_PART_WIDTH)
        self.add_ep_group_box.layout().addWidget(self.episode_range_line_edit, 1, 2, 1, 2, alignment=Qt.AlignLeft)
        self.episode_range_line_edit.editingFinished.connect(self.update_curent_episodes)

        self.mainLayout.addWidget(self.add_ep_group_box, alignment=Qt.AlignTop)

        # Add scenes part
        self.add_sc_group_box = QGroupBox("Add scenes")
        self.add_sc_group_box.setLayout(QVBoxLayout())
        self.add_sc_group_box.layout().setContentsMargins(10, 4, 10, 10)

        self.scroll = QScrollArea(self)
        self.scroll.setFixedSize(200, 280)  # outside area size
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFrameStyle(0)

        self.scrolling_widget = QWidget()
        self.scrolling_widget.setFixedSize(190, 0)  # inside area size
        self.scrolling_widget.setLayout(QGridLayout())
        self.scroll.setWidget(self.scrolling_widget)
        self.scroll.setWidgetResizable(True)
        self.add_sc_group_box.layout().addWidget(self.scroll, alignment=Qt.AlignRight)

        self.mainLayout.addWidget(self.add_sc_group_box)

        self.add_bttn = QPushButton('Create structure')
        self.add_bttn.clicked.connect(self.create_structure)
        self.add_bttn.setStyleSheet('QPushButton {background-color: #99CC99;}'
                                    'QPushButton:hover {background-color: #66CC69;}')
        self.mainLayout.addWidget(self.add_bttn)

        self.path_label_update()

    def update_curent_episodes(self):
        """
        Convert text from self.episode_range_line_edit to episode list,
        than draw episode components in ui
        """
        pattern = r"\s?(\d+)\s?"

        # if many cases in line_edit divide it
        input_list = self.episode_range_line_edit.text().split(",")
        self.current_episod_list = []
        self.episod_scenes_dict = dict()
        for item in input_list:
            item_val = sorted(map(int, re.findall(pattern, item)))
            if len(item_val) == 1:
                self.current_episod_list += item_val
            elif len(item_val) == 2:
                self.current_episod_list += range(item_val[0], item_val[1] + 1)
        self.current_episod_list = sorted(list(set(self.current_episod_list)))

        self.clear_episod_components()
        self.add_episod_components()

    def add_episod_components(self):
        """
        Add label and spinBox  for each episod
        """
        self.scrolling_widget.setFixedSize(185, len(self.current_episod_list) * 28 + 10)

        for ep in self.current_episod_list:
            ep_label = QLabel("Episod " + str(ep))
            ep_label.setFixedWidth(60)
            self.scrolling_widget.layout().addWidget(ep_label, ep, 0, alignment=Qt.AlignRight)

            scenes_spin_box = QSpinBox()
            scenes_spin_box.setFixedWidth(80)
            self.scrolling_widget.layout().addWidget(scenes_spin_box, ep, 1, alignment=Qt.AlignRight)

            self.episod_scenes_dict[ep] = scenes_spin_box

    def clear_episod_components(self):
        """
        Clear all child of scrolling_widget
        """
        self.scrolling_widget.setFixedSize(150, 0)
        while self.scrolling_widget.layout().count():
            child = self.scrolling_widget.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.episod_scenes_dict = dict()

    def open_file_location(self):
        path = self.project_combobox.itemData(self.project_combobox.currentIndex(), role=Qt.UserRole)
        subprocess.Popen('explorer "%s"' % os.path.abspath(path))

    def path_label_update(self):
        """
        Change label for ui elements
        """
        self.clear_episod_components()
        i = self.project_combobox.currentIndex()
        self.path_picer_label.setText(self.project_combobox.itemData(i, role=Qt.UserRole))

        if self.project_combobox.itemData(i, role=Qt.UserRole + 1):  # if project full-length
            self.add_ep_group_box.setTitle("Add episode")
            self.seria_label.setVisible(False)
            self.seria_line_edit.setVisible(False)
            self.scroll.setFixedSize(200, 280)  # outside area size
        else:
            self.add_ep_group_box.setTitle("Add seria")
            self.seria_label.setVisible(True)
            self.seria_line_edit.setVisible(True)
            self.scroll.setFixedSize(200, 252)  # outside area size


class AddEpisodes(AddEpisodes_UI):

    def create_structure(self):
        """
        Create episodes and scenes list in it
        """
        # get seria if project not full-length
        i = self.project_combobox.currentIndex()
        full_length = self.project_combobox.itemData(i, role=Qt.UserRole + 1)

        seria = self.seria_line_edit.text()

        if not full_length:
            if re.match(r'^\d+$', seria):  # if all digits in name
                seria = '/seria%03d' % int(seria)
            else:
                seria = "/"+seria
        else:
            seria = ""

        output_dict = {x: int(self.episod_scenes_dict[x].text()) for x in self.episod_scenes_dict.keys()}
        self.project = self.project_combobox.itemData(i, role=Qt.UserRole)

        for episod in output_dict.keys():
            scen_num = output_dict[episod]
            episod = '/ep%02d' % int(episod)
            self.create_episode(seria, episod)

            ep = episod[1:] if not full_length else episod
            scenes_path = self.project + "/scenes" + seria + episod + seria.replace("seria", "sr") + ep
            for num in range(1, scen_num + 1):
                sc = 'sc%02d' % int(num)
                self.create_scene(scenes_path + sc)


    def create_episode(self, seria, episod):

        directory_list = [
            self.project + "/scenes" + seria + episod + "/references/animation",
            self.project + "/scenes" + seria + episod + "/references/texturing",
            self.project + "/scenes" + seria + episod + "/references/lighting",
            self.project + "/scenes" + seria + episod + "/references/dynamics",
            self.project + "/scenes" + seria + episod + "/references/paint",
            self.project + "/scenes" + seria + episod + "/shared/work",
            self.project + "/scenes" + seria + episod + "/template/work",
            self.project + "/scenes" + seria + episod + "/montage",
            self.project + "/Playblast" + seria + episod + "/work",
            self.project + "/precompose" + seria + episod + "/dyn/work",
            self.project + "/precompose" + seria + episod + "/render/work",
            self.project + "/precompose" + seria + episod + "/vfx/work",
            self.project + "/output/" + seria + episod + "/render_dpx"
        ]

        for directory in directory_list:
            if not os.path.isdir(directory):
                try:
                    os.makedirs(directory)
                except:
                    print "don`t create dir: ", directory

    @staticmethod
    def create_scene(target_path):

        target_path = target_path.rstrip("/") + "/"
        target_path_list = [target_path]
        directory_list = [
            "anm/work",
            "cache/alembic",
            "cache/vfx",
            "compose/dailies",
            "compose/final",
            "compose/final/render_dpx",
            "compose/layers",
            "compose/nk",
            "compose/nuke",
            "compose/render",
            "compose/sequence",
            "dyn/work",
            "vfx/backup",
            "vfx/import",
            "vfx/maps",
            "vfx/render",
            "images",
            "light/work",
            "paint/work",
            "renderman/ribarchives",
            "slim",
            "tmplate/work",
            "design/work",
        ]
        temp_directory_list = [
            "compose/render_tif",
        ]

        for target_path in target_path_list:
            for directory in directory_list:
                directory = target_path + directory
                if not os.path.isdir(directory):
                    try:
                        os.makedirs(directory)
                    except:
                        print "don`t create scene: ", directory

            for directory in temp_directory_list:
                directory = target_path + directory
                if os.path.isdir(directory):
                    if not os.listdir(directory):
                        try:
                            os.removedirs(directory)
                        except:
                            print "don`t remove directory: ", directory

if __name__ == '__main__':
    app = QApplication([])
    win = AddEpisodes()
    win.show()
    app.exec_()
