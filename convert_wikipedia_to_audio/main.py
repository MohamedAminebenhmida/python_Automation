import wikipedia
from gtts import gTTS
import os
# result = wikipedia.summary('Tunisia', sentences=2)
# print(result)
# result = wikipedia.search('syria', results=10)
# print(result)
# change the language of wikipedia page
# wikipedia.set_lang('ja')
# result = wikipedia.summary('Atari', sentences=4)
# print(result)
text = "Subscribe to amine devops channel!"
file = gTTS(text=text, lang='en', slow=False)
file.save('amine.mp3')
os.system('start amine.mp3')
