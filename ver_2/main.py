import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
# 导入my_win.py中内容
from gui import *
# from videoplayer import VideoPlayer
from videoplayer import CVideoPlayer
import cv2
import sys

# 创建mainWin类并传入Ui_MainWindow
class mainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.button_stop)
        self.pushButton_2.clicked.connect(self.button_capture)
        self.pushButton_3.clicked.connect(self.button_restart)
        self.pushButton_4.clicked.connect(self.open_file)
        self.statusbar.showMessage("Welcome to PyQT5")
        
        self.actionAbout_File.triggered.connect(self.About_File)
        self.actionExit.triggered.connect(self.exit)
        self.actionHelp.triggered.connect(self.About_Help)

        self.comboBox.activated.connect(self.combo)

    def button_stop(self):
        if player.isPause:
            player.isPause = False
            self.statusbar.showMessage("Click Video Start")
        else:
            player.isPause = True
            self.statusbar.showMessage("Click Video Pause")

    def button_capture(self):
        player.SaveImg()
        self.statusbar.showMessage("Click Video Capture")

    def button_restart(self):
        player.Restart()

    def About_File(self):
        QMessageBox.information(self, 'Info', 'Hello world from PyQT5!')
        self.statusbar.showMessage("Welcome to PyQT5")

    def exit(self):
        sys.exit()

    def About_Help(self):
        QMessageBox.information(self, 'Info', 'About Hello World')

    def combo(self, index):
        self.statusbar.showMessage("Selected Method : "+str(self.comboBox.itemText(index)))

    def open_file(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files[0])
        player.CreateVideoPlayback(files[0])
    
if __name__ == '__main__':
    # 下面是使用PyQt5的固定用法
    player = CVideoPlayer()
    app = QApplication(sys.argv)
    main_win = mainWin()
    main_win.show()
    sys.exit(app.exec_())
