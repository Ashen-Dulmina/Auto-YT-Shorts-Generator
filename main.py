from local_tts import ListVoices, getVoiceOverLocal
from xilabs_tts import ListXIVoices, getVoiceOver
from ai_generated_facts import convertMarkdown, ListAIModels, generateFact, casual, select_bgv_a, select_bgm_a
from cat_api import getFact, select_bgv_c, select_bgm_c
from editz import EditVid

EditVid("test.mp4", select_bgm_c(), "vo.mp3") #install image magic and try this

#DEFAULT WINDOWS VOICE IDS
#"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
