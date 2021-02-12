from PyQt5 import QtCore, QtWidgets, QtMultimedia
import time
import random


class MemeAudioPlayer:
    def __init__(self, parentWindow: QtWidgets.QApplication):
        self.__memeSongsFiles = None
        self.__songIndex = 0
        self.__initMemeSongsFiles()
        self.__parent = parentWindow

    # playRandomSong calls __playSong0 and plays a random meme song
    def playRandomSong(self):
        index = random.randint(0, 18)
        random.seed(time.time_ns())
        self.__playSong0(index)

    # playSong calls __playSong0 and plays meme songs according to index(front-to-back)
    def playSong(self):
        self.__playSong0(self.__songIndex)
        # go to the next song :)
        self.__songIndex = (self.__songIndex + 1) % len(self.__memeSongsFiles)

    # __playSong0 plays a meme song of a given index
    def __playSong0(self, index: int):
        # qt player magic
        fileName = "res/" + self.__memeSongsFiles[index]
        fullPath = QtCore.QDir.current().absoluteFilePath(fileName)
        url = QtCore.QUrl.fromLocalFile(fullPath)
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)

        player.play()

        # wait 10s then exit
        time.sleep(10)
        player.stop()

        # sync to give control back to parent wiget
        self.__parent.sync()

    # __initMemeSongsFiles meme songs files names
    def __initMemeSongsFiles(self):
        self.__memeSongsFiles = ["all_stars.mp3", "astronomia01.mp3", "big_enough01.mp3", "crab_rave.mp3",
                                 "rasputin01.mp3", "rick_roll01.mp3", "smoke_weed_every_day.mp3", "sss.mp3",
                                 "ussr_anthem02.mp3", "what_does_the_fox_say.mp3", "astronomia00.mp3",
                                 "big_enough00.mp3", "blue.mp3", "rasputin00.mp3", "rick_roll00.mp3",
                                 "shooting_starts.mp3", "smooth_criminal.mp3", "ussr_anthem01.mp3", "we_R#1.mp3"]
