import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

print("Google AI Wakeup Call -- OKI !")

GOOGLE_AI_API_KEY = 'AIzaSyAXt4BoVJm5LIJ_9tUoSH2T8uLs888-DH4'

genai.configure(api_key=GOOGLE_AI_API_KEY)

def convertMarkdown(text):
	text = text.replace('•', '  *')
	return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def ListAIModels():
	for m in genai.list_models():
		if 'generateContent' in m.supported_generation_methods:
			print(m.name)

def generateFact():
	model = genai.GenerativeModel('gemini-pro')
	response = model.generate_content("give me a long fact and describe it(must be above 100 characters). only give the fact and nothing else(without the Fact: text)")
	return response.text

def casual(modal, question):
	model = genai.GenerativeModel(modal)
	response = model.generate_content(question)
	return response