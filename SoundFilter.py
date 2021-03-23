#!/usr/bin/python3.8
import speech_recognition as sr
from MemeAudioPlayer import MemeAudioPlayer


class SoundFilter:

    def __init__(self, memer: MemeAudioPlayer):
        self.__curses: list = None
        self.__initCursesList()
        self.__memer: MemeAudioPlayer = memer

    # recognizeSoundWithFilter calls recognizeSound
    # and returns true when there's a curse word!
    def recognizeSoundWithFilter(self) -> bool:
        speech: str = self.recognizeSound()
        # get list of the said sentence to check if any of the said words is a bad word or not :)
        speechList: list = speech.split(" ")
        for saidWord in speechList:
            if saidWord in self.__curses:
                # the most slavic part of the program :)))))
                self.__memer.playRandomSong()
                # you're dirty :)
                return True

        # you're an angle :)
        return False

    # recognizeSound returns a string of the said word
    def recognizeSound(self) -> str:
        # wait for it...
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # setting time limit to make it look like as if it's live or something :)
            # also also 1.5s is the perfect(not much, but does the job) time, well I tested a lot
            audio: sr.AudioData = r.listen(source, phrase_time_limit=1.5)

            try:
                # transcribe audio using Google's API
                text = r.recognize_google(audio)
                return text

            except sr.UnknownValueError:
                # such empty record :(
                return ""

    # better not see the list, I spent 10mins cleaning my eyes :)
    def __initCursesList(self):

        self.__curses = ["f***", "fuck", "fu**", "motherfucker", "m***********", "mother******", "shit", "s***", "sh**",
                         "bitch", "b****", "bit**", "ass", "a**", "as*", "dick", "di**", "d***", "dickhead", "dick****",
                         "d*******", "asshole", "ass****", "a******", "bastard", "bast***", "b******", "cunt", "cu**",
                         "c***", "gay", "ga*", "g**", "lesbian", "les****", "l******", "shitty", "shity", "fucker",
                         "f*****", "fuck**", "f******", "fuckers", "damn", "da**", "d***", "dicks", "d****", "twat",
                         "tw**", "t***", "fucking", "fuck***", "f******", "motherfuker", "mother******"]
