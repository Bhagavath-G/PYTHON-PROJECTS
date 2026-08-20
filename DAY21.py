'''PROJECT 21'''
from gtts import gTTS

text = "Hello everyone, this is bhagavath"

tts = gTTS(text=text, lang = 'en')

tts.save("audio.mp3")

print("AUDIO SAVED")
