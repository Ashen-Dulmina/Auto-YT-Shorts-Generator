from local_tts import ListVoices, getVoiceOverLocal
from xilabs_tts import ListXIVoices, getVoiceOver
#from ai_generated_facts import convertMarkdown, ListAIModels, generateFact, casual, select_bgv_a, select_bgm_a
from cat_api import getFact, select_bgv_c, select_bgm_c


#DEFAULT WINDOWS VOICE IDS
#"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
#open_ai_api_key = 'sk-proj-dFDllbCbObixT3ve2QzfT3BlbkFJD4z0c9Sk938WPmNXVkpp'
#11_LABS_API_KEY = '97db27735cd91bdc0220fa836fb0e8eb'
#Ava's_voice_ID = 'CrW0KJwldC8NrcNHNvBL'
#LLAMA_AI_API_KEY = 'LL-WxEzIkSMxKoXGcvl2GK9kc6gamTLY5QvAkbtEImtLFbwk8YcDPHMNdTMxntjIGdK'
#google_api_key_ai = 'AIzaSyAXt4BoVJm5LIJ_9tUoSH2T8uLs888-DH4'


getVoiceOver("CrW0KJwldC8NrcNHNvBL", "Hi I'm Eva 123 Test", "out")