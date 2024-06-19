import textwrap
import json
from google.generativeai import list_models, GenerativeModel, configure
from IPython.display import display
from IPython.display import Markdown

print("Google AI Wakeup Call -- OKI !")

#get all keys into one file [6/18]
#all keys are stored in json format in index.json[6/19]

def get_key(): #-------WORKS-------#
	file = open("keys.json", 'r')
	fjs = json.load(file)
	key = fjs['google_api_key']
	return key

#made the code run faster having an error with generating content FIX - THIS!!!!!!!!!!!!!!!![6/16]
#this somehow works fine no external fixes done [6/18]

configure(api_key=get_key())  

def convertMarkdown(text):
	text = text.replace('•', '  *')
	return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def ListAIModels():
	for m in list_models():
		if 'generateContent' in m.supported_generation_methods:
			print(m.name)

def generateFact(): #------------------------<THIS FUNCTION DOES NOT WORK[6/16]>--<NOPE THIS FUNCTION SOMEHOW WORKS FINE[6/18]>----------------------------#
	model = GenerativeModel('gemini-pro')
	response = model.generate_content("give me a long fact and describe it(must be above 100 characters). only give the fact and nothing else(without the Fact: text)")
	return response.text

def casual(modal, question): #------------------------<THIS FUNCTION DOES NOT WORK[6/16]>--<NOPE THIS FUNCTION SOMEHOW WORKS FINE[6/18]>----------------------------#
	model = GenerativeModel(modal)
	response = model.generate_content(question)
	return response

def select_bgv_a():
	x_factor= random.choice(os.listdir("osc_background_clips"))
	print(x_factor)

def select_bgm_a():
	x_factor= random.choice(os.listdir("lofi_bgm"))
	print(x_factor)
