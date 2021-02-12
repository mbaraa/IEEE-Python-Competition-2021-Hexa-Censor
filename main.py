from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from MemeAudioPlayer import MemeAudioPlayer
from SoundFilter import SoundFilter


class App(QWidget):

    def __init__(self, parent: QApplication):
        super().__init__()
        self.__parent = parent
        self.__soundFilter = SoundFilter(MemeAudioPlayer(self.__parent))
        self.__isListening: bool = False
        self.__curseCounter: int = 0  # for some reason 0 isn't working

        # qt widgets
        self.__listenStatus: QtWidgets.QLabel = None
        self.__curseCounterText: QtWidgets.QLabel = None
        self.__startListening: QtWidgets.QPushButton = None

        # ui translator 
        self.__translate = QtCore.QCoreApplication.translate

        self.initUI()
        self.initFancyUI()

    def initUI(self):
        self.setWindowTitle("HexaCensor")
        self.setGeometry(10, 10, 720, 410)  # left, top, width, height

        self.__listenStatus = QtWidgets.QLabel("Not Listening!", self)
        self.__listenStatus.setGeometry(30, 170, 250, 50)

        self.__curseCounterText = QtWidgets.QLabel(self)
        self.__curseCounterText.setGeometry(370, 140, 300, 50)

        self.__startListening = QtWidgets.QPushButton(self)
        self.__startListening.setGeometry(370, 240, 250, 50)
        self.__startListening.clicked.connect(self.__startListeningOnClick)

        self.show()

    def initFancyUI(self):
        self.setWindowTitle(self.__translate("HexaCensor", "HexaCensor"))
        self.__listenStatus.setText(self.__translate("HexaCensor",
                                                     "<html><head/><body><p><span style=\" font-size:22pt; color:#1a5fb4;\">Not Litening!</span></p></body></html>"))
        self.__curseCounterText.setText(self.__translate("HexaCensor",
                                                         "<html><head/><body><p><span style=\" font-size:18pt;\">Curse Counter: 0</span></p></body></html>"))
        self.__startListening.setText(self.__translate("HexaCensor", "Start Listening!"))

    @pyqtSlot()
    def __startListeningOnClick(self):
        # flip listening state
        self.__isListening = not self.__isListening

        if self.__isListening:
            self.__listenStatus.setText(self.__translate("HexaCensor",
                                                         "<html><head/><body><p><span style=\" font-size:22pt; color:#c90909;\">Litening!</span></p></body></html>"))
        else:
            self.__listenStatus.setText(self.__translate("HexaCensor",
                                                         "<html><head/><body><p><span style=\" font-size:22pt; color:#1a5fb4;\">Not Litening!</span></p></body></html>"))

        self.__parent.sync()

        while self.__isListening:
            if self.__soundFilter.recognizeSoundWithFilter():
                self.__curseCounter -= -1

            self.__curseCounterText.setText(self.__translate("HexaCensor",
                                                             f"<html><head/><body><p><span style=\" font-size:18pt;\">Curse Counter: {self.__curseCounter}</span></p></body></html>"))
            self.__parent.sync()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App(app)
    sys.exit(app.exec())
