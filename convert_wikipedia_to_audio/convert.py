import wikipedia
from gtts import gTTS
import os

wikipedia.set_lang('en')
result = wikipedia.summary('samurai', sentences=4)
# print(result)
myobj = gTTS(text=result, lang='en', slow="False")
myobj.save('samurai.mp3')
os.system('start samurai.mp3')
