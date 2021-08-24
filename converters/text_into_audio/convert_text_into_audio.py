from gtts import gTTS
from yaml import load, FullLoader

with open("config.yaml", "r") as file:
    config = load(file, Loader=FullLoader)

sp = gTTS(text=config.get("text"), lang=config.get("language"), slow=False)
sp.save(config.get("path_to_audio_file"))
