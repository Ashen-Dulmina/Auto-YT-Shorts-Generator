import pyttsx3

print("Local_TTS Wakeup Call -- OKI !")


def getVoiceOverLocal(voice, rate :int, volume :float, text, file_name):
	engine = pyttsx3.init()
	if voice:
		engine.setProperty('voice', voice)
	engine.setProperty('rate', rate)
	engine.setProperty('volume', volume)
	engine.save_to_file(text, f'{file_name}.mp3')
	engine.runAndWait()
	engine.stop()

def ListVoices():
	engine = pyttsx3.init()
	voices = list([engine.getProperty('voices')])
	for i,voices in enumerate(voices[0]):
		print(f'{i+1} {voices.name} {voices.age} : {voices.languages} ({voices.gender}) [{voices.id}]')

