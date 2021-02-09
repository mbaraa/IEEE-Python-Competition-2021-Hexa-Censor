from SoundFilter import SoundFilter
from MemeAudioPlayer import MemeAudioPlayer

if __name__ == "__main__":
    sf = SoundFilter(MemeAudioPlayer())
    while True:
        print(f"you said: {sf.recognizeSoundWithFilter()}")
