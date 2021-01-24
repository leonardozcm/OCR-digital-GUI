from View.ui_main import Ui_MainWindow
from test.detect import detect_video

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video_path = '/'
        self.save_dir = '/'
        self.video_name = None
        self.outputfile = None

        self.ui.video_pushButton.clicked.connect(self.get_file_name)
        self.ui.savepath_pushButton.clicked.connect(self.get_dir_name)
        self.ui.checkout_pushButton.setEnabled(False)
        self.ui.checkout_pushButton.clicked.connect(self.open_output_file)
        self.ui.run_buttom.clicked.connect(self.run)

    def run(self):
        # detect function
        self.ui.log_field.setText("working on {} ...".format(self.video_name))
        counts=0
        counts = detect_video(self.ui.videopath_browser.toPlainText(), self.ui.unit_comboBox.currentIndex() + 1,
                              self.ui.savepath_browser.toPlainText(),
                              skipped=int(self.ui.skipped_browser.toPlainText()))

        self.ui.checkout_pushButton.setEnabled(True)
        self.set_total_count(counts)
        self.set_save_path()
        self.ui.log_field.setText("working on {} ... \ndone!".format(self.video_name))

        pass

    def get_file_name(self):
        # QFileDialog.getOpenFileName()
        fileName1, filetype = QFileDialog.getOpenFileName(self, 'Open video file',
                                                          self.video_path)  # 设置文件扩展名过滤,=
        self.video_path = fileName1
        try:
            self.video_name = fileName1.split('/')[-1][:-4][0]
        except:
            self.video_name = fileName1
        print(fileName1, "=========", filetype)
        self.ui.videopath_browser.append(fileName1)
        self.ui.savepath_browser.append(fileName1[:-4] + ".csv")

    def get_dir_name(self):
        # QFileDialog.getOpenFileName()
        dirName1 = QFileDialog.getExistingDirectory(self, 'Open saving directory',
                                                    self.save_dir)  # 设置文件扩展名过滤,=
        self.save_dir = dirName1
        self.outputfile = os.path.join(dirName1, self.video_name + ".csv")
        print(dirName1, "=========")
        self.ui.savepath_browser.append(self.outputfile)

    # 更新label共提取n个数字
    def set_total_count(self, n):
        self.ui.data_count.setText("{}个数字".format(n))

    def set_save_path(self):
        self.ui.saved2path.setText("保存至{}".format(self.outputfile))

    def open_output_file(self):
        assert os.path.exists(self.outputfile) is not None, "path not initialized"
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(self.outputfile))

    # todo:I'm working on
    def update_logs(self):
        while (self):
            if os.path.exists(self.outputfile):
                output_line = 10
                with open(self.outputfile, 'r') as opfile:
                    lines = opfile.readlines()
                    log = ""
                    start = -output_line if len(lines) > output_line else 0
                    for line in lines[start:-1]:
                        log += line + "\n"
                self.ui.log_field.setText(log)
            else:
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
