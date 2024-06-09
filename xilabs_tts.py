import requests
import json

#not tested

print("Eleven Labs TTS Wakeup Call -- OKI !")

XI_API_KEY = '97db27735cd91bdc0220fa836fb0e8eb'

def ListXIVoices():
	pull = 'https://api.elevenlabs.io/v1/voices'
	heads = {
	  "Accept": "application/json",
	  "xi-api-key": XI_API_KEY,
	  "Content-Type": "application/json"
	}
	response = requests.get(pull, headers=heads)
	vocs = response.json()
	for voice in vocs['voices']:
		print(f"{voice['name']}; {voice['voice_id']}")

def getVoiceOver(voice_ID, text, filename):
	CHUNK_SIZE = 1024
	url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_ID}"
	headers = {
	  "Accept": "application/json",
	  "xi-api-key": XI_API_KEY,
	  "Content-Type": "application/json"
	}
	data = {
  	"text": text,
  	"model_id": "eleven_monolingual_v1",
  	"voice_settings": {
  	  "stability": 0.5,
  	  "similarity_boost": 0.5
  	}
	}
	response = requests.post(url, json=data, headers=headers)
	with open(f"{filename}.mp3", 'wb') as f:
	  for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
	    if chunk:
	      f.write(chunk)