from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys
from MemeAudioPlayer import MemeAudioPlayer
from SoundFilter import SoundFilter


class App(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QApplication):
        super().__init__()
        self.__parent: QtWidgets.QApplication = parent
        self.__soundFilter = SoundFilter(MemeAudioPlayer(self.__parent))
        self.__isListening: bool = False
        self.__curseCounter: int = 0  # for some reason 0 isn't working

        # qt widgets
        self.__listenStatus: QtWidgets.QLabel
        self.__curseCounterText: QtWidgets.QLabel
        self.__startListening: QtWidgets.QPushButton

        # ui translator 
        self.__translate = QtCore.QCoreApplication.translate

        self.__initUI()
        self.__initFancyUI()

    # setup qt widgets
    def __initUI(self):
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

    # setup widgets' text content
    def __initFancyUI(self):
        self.setWindowTitle(self.__translate("HexaCensor", "HexaCensor"))
        self.__listenStatus.setText(self.__translate("HexaCensor",
                                                     "<html><head/><body><p><span style=\" font-size:22pt; color:#1a5fb4;\">Not Listening!</span></p></body></html>"))
        self.__curseCounterText.setText(self.__translate("HexaCensor",
                                                         "<html><head/><body><p><span style=\" font-size:18pt;\">Curse Counter: 0</span></p></body></html>"))
        self.__startListening.setText(self.__translate("HexaCensor", "Start/Stop Listening!"))

    @pyqtSlot()
    def __startListeningOnClick(self):
        # flip listening state
        self.__isListening = not self.__isListening

        # update listening status
        if self.__isListening:
            self.__listenStatus.setText(
                self.__translate("HexaCensor",
                                 "<html><head/><body><p><span style=\" font-size:22pt; color:#c90909;\">Listening!</span></p></body></html>"))
        else:
            self.__listenStatus.setText(
                self.__translate("HexaCensor",
                                 "<html><head/><body><p><span style=\" font-size:22pt; color:#1a5fb4;\">Not Listening!</span></p></body></html>"))
        # sync to update UI's content
        self.__parent.sync()

        # to know when to speak when testing :)
        counter: int = 0
        # start speech recognition with curse filter
        while self.__isListening:
            # debugging...
            print(f"speak now {counter}")
            counter -= -1

            # increase counter by 1 when a curse is found
            if self.__soundFilter.recognizeSoundWithFilter():
                self.__curseCounter -= -1

            # update curse counter text
            self.__curseCounterText.setText(self.__translate("HexaCensor",
                                                             f"<html><head/><body><p><span style=\" font-size:18pt;\">Curse Counter: {self.__curseCounter}</span></p></body></html>"))
            # sync to update UI's content
            self.__parent.sync()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App(app)
    sys.exit(app.exec())
