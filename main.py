from SoundFilter import SoundFilter

if __name__ == "__main__":
    sf = SoundFilter()
    while True:
        print(f"you said: {sf.recognizeSoundWithFilter()}")

