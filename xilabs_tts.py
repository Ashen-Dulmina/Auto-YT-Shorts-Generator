import requests
import json

# ̶n̶o̶t̶  tested # yeah i tested it

print("Eleven Labs TTS Wakeup Call -- OKI !")

#get all keys into one file [6/18]
#all keys are stored in json format in index.json[6/19]

def get_key(): #-------WORKS-------#
	file = open("keys.json", 'r')
	fjs = json.load(file)
	key = fjs['xi_labs_api_key']
	return key

#default voice is eva can be changed at index.json : property = 'xi_voice_id'
def defaultVoice():
	filev = open("keys.json", 'r')
	fjsv = json.load(filev)
	voice = fjsv['xi_voice_id']
	return voice

XI_API_KEY = get_key()

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