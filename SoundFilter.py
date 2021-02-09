import speech_recognition as sr
from MemeAudioPlayer import MemeAudioPlayer


class SoundFilter:

    def __init__(self, memer: MemeAudioPlayer):
        self.__curses = None
        self.__initCursesList()
        self.__memer = memer

    def recognizeSoundWithFilter(self) -> str:
        speech: str = self.recognizeSound()
        # get list of the said sentence to check if any of the said words is a bad word or not :)
        speechList: list = speech.split(" ")
        for saidWord in speechList:
            if saidWord in self.__curses:
                print("watch your mouth!")
                # play some meme song
                self.__memer.playRandomSong()

        return speech

    def recognizeSound(self) -> str:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # setting time limit to make it look like as if it's live or something :)
            # also also 1.5s is the perfect(not much, but does the job) time, well I tested a lot
            audio = r.listen(source, phrase_time_limit=1.5)

            try:
                text = r.recognize_google(audio)
                return text

            except sr.UnknownValueError:
                return ""

    def __initCursesList(self):

        self.__curses = ["f***", "fuck", "fu**", "motherfucker", "m***********", "mother******", "shit", "s***", "sh**",
                         "bitch", "b****", "bit**", "ass", "a**", "as*", "dick", "di**", "d***", "dickhead", "dick****",
                         "d*******", "asshole", "ass****", "a******", "bastard", "bast***", "b******", "cunt", "cu**",
                         "c***", "gay", "ga*", "g**", "lesbian", "les****", "l******", "shitty", "shity", "fucker",
                         "f*****", "fuck**", "f******", "fuckers", "damn", "da**", "d***", "dicks", "d****", "twat",
                         "tw**", "t***", "fucking", "fuck***", "f******", "motherfuker", "mother******"]
