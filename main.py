import os
os.environ['QT_PLUGIN_PATH'] = r"C:/Users/Дима/AppData/Local/Programs/Python/Python312/plugins"
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
#импортує виджети 

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#импортуе класс QMainWindow 
#Widget наслідує QMainWindow
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)
        vid = QMediaContent(QUrl.fromLocalFile('video\\7.avi'))
#запускає видео

        self.media.setMedia(vid)
        self.media.play()
#класс віджет

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
#закриває календарь