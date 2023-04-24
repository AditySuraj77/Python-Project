import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

while True:
    time.sleep(0)

    speak.Speak('Please Enter Some Words')
    text = input('Enter a Some Word to speak : ')
    if text == 'q':
        print('Programme end')
        break





    speak.Speak(text)


