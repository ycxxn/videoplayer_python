import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# 导入my_win.py中内容
from gui import *
from videoplayer import VideoPlayer
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
        self.statusbar.showMessage("Welcome to PyQT5")
        
        self.actionAbout_File.triggered.connect(self.About_File)
        self.actionExit.triggered.connect(self.exit)
        self.actionHelp.triggered.connect(self.About_Help)

        self.comboBox.activated.connect(self.combo)

    def About_File(self):
        QMessageBox.information(self, 'Info', 'Hello world from PyQT5!')
        self.statusbar.showMessage("Welcome to PyQT5")

    def exit(self):
        sys.exit()

    def About_Help(self):
        QMessageBox.information(self, 'Info', 'About Hello World')

    def combo(self, index):
        self.statusbar.showMessage("Selected Method : "+str(self.comboBox.itemText(index)))
        # print(self.comboBox.itemText(index))
        # print(self.comboBox.itemData(index))

    def button_stop(self):
        if player.isStop:
            player.isStop = False
            self.statusbar.showMessage("Click Video Start")
        else:
            player.isStop = True
            self.statusbar.showMessage("Click Video Pause")

    def button_capture(self):
        player.saveImg(frame)
        self.statusbar.showMessage("Click Video Capture")
    
    def button_restart(self):
        player.restart()
        self.statusbar.showMessage("Click Video Restart")


def draw_circle(event,x,y,flags,param):
    
    global ix,iy,drawing,mode
    #Click 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        print("ix=",ix,"iy=",iy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            print("fx=",x,"fy=",y)
            cv2.rectangle(frame,(ix,iy),(x,y),(0,255,255),1)
           


player = VideoPlayer("video.mp4")


global px,py    
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',draw_circle)



if __name__ == '__main__':
    # 下面是使用PyQt5的固定用法
    app = QApplication(sys.argv)
    main_win = mainWin()
    while(1):
        if player.isStop == False:
            ret,frame = player.get_cap()
        if ret == False:
            break

        cv2.imshow('frame', frame)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break

        main_win.show()
        main_win.update()
        # sys.exit(app.exec_())
    player.cap.release()
    cv2.destroyAllWindows()