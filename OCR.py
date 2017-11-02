#version1
#Tries to load the file directly from memory. No luck, won't work.
"""

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import requests

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

def ocr(update):
    img = Image.open(update)
    img.load()
    print (pytesseract.image_to_string(img))
    #print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

ocr("C:\\Users\\Natarajan\\Desktop\\Untitled.png")          #works.

#img = requests.get("https://i.imgur.com/U5eyU8x.png")
#ocr(img)

"""

#Version2
# Should work perfectly. However, there seems to be some backward compatibility issue. Analysis required. 

"""

import telegram
import time
import pytesseract
import config
import os

try:
	import Image
except ImportError:
	from PIL import Image

def message(bot, update):
	if not update.message.photo:
		return

	photosize = bot.getFile(update.message.photo[-1].file_id)

	if update.message.chat_id > 0: # user	
		_photosize_to_parsed(bot, update, photosize)

def _photosize_to_parsed(bot, update, photosize):
    os.mkdir(config.CACHE_DIR)
    filename = config.CACHE_DIR+'/photo_'+''.join(str(time.time()).split('.'))+'.jpg'
    photosize.download(filename)
    image_text = pytesseract.image_to_string(Image.open(filename))
    return image_text
    if config.CACHE_TEMP:
        os.remove(filename)

"""

#version 3
#based on a telepot version of an OCR bot. Still no luck.

"""

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os
import time

def ocr(update):
    to_save = './downloads/' + ''.join(str(time.time()).split('.')) + '.png'
    bot.downloadFile(photo_id, to_save)
    text = pytesseract.image_to_string(Image.open(to_save), lang=self._lang)
    return text

"""