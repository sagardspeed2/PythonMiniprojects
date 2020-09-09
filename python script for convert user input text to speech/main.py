import pyttsx3
import win32com.client
from gtts import gTTS

input_string = input("\nEnter a String : ")

gtts_obj = gTTS(text=input_string, lang='en', slow=True)

gtts_obj.save(r"E:\test_audio.mp3")
print("\nAudio saved successfully using gTTS module")

print("\nText to audio using pyttsx3 module")

pyttsx3_obj = pyttsx3.init()

pyttsx3_obj.say(input_string)

pyttsx3_obj.runAndWait()

print("Text to audio using win32com mudule")

win32com_obj = win32com.client.Dispatch("SAPI.SpVoice")

win32com_obj.Speak(input_string)