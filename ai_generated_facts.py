import textwrap
from google.generativeai import list_models, GenerativeModel, configure
from IPython.display import display
from IPython.display import Markdown

print("Google AI Wakeup Call -- OKI !")

def get_key(): #-------WORKS-------#
	f = open("google_api_key.txt", "r")
	key = f.read()
	return key

configure(api_key=get_key())  #made the code run faster having an error with generating content FIX - THIS!!!!!!!!!!!!!!!!

def convertMarkdown(text):
	text = text.replace('•', '  *')
	return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def ListAIModels():
	for m in list_models():
		if 'generateContent' in m.supported_generation_methods:
			print(m.name)

def generateFact(): #------------------------------------------------------THIS FUNCTION DOES NOT WORK--------------------------------------------------------------#
	model = GenerativeModel('gemini-pro')
	response = model.generate_content("give me a long fact and describe it(must be above 100 characters). only give the fact and nothing else(without the Fact: text)")
	return response.text

def casual(modal, question): #------------------------------------------------------THIS FUNCTION DOES NOT WORK--------------------------------------------------------------#
	model = GenerativeModel(modal)
	response = model.generate_content(question)
	return response

def select_bgv_a():
	x_factor= random.choice(os.listdir("osc_background_clips"))
	print(x_factor)

def select_bgm_a():
	x_factor= random.choice(os.listdir("lofi_bgm"))
	print(x_factor)
