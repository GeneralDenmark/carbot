from gtts import gTTS
import hashlib
from os import system
from os.path import join


tmp_folder = "./tmp"


def do_talk(text):
    try:
        lang = "en"
        file_name = join(tmp_folder, hashlib.md5(text.encode("utf-8")).hexdigest() + ".mp3")
        gTTS(text=text, lang=lang, slow=False).save(file_name)
        system("ffplay -nodisp -autoexit " + file_name + " >/dev/null 2>&1")
    finally:
        system("rm " + file_name + ">/dev/null 2>&1")
