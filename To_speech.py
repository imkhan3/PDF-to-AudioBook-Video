from gtts import gTTS
import os
from mutagen.mp3 import MP3
from To_text import pageDict

language = 'en-uk'

combinedText = ' '.join(map(str, pageDict.values()))
gTTS(text=combinedText, lang=language, slow=False).save("complete_audio.mp3")

for i in pageDict:
    mytext = pageDict[i]
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("temp.mp3")
    # Add length of mp3 to dictionary value along with text
    pageDict[i] = MP3("temp.mp3").info.length
    #delete temp
    os.remove("temp.mp3")



for x, y in pageDict.items():
  print(x, y) 