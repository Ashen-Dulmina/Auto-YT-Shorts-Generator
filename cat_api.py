import requests

print("Cat API Wakeup Call -- OKI !")

def getFact():
	cat_api = requests.get("https://catfact.ninja/fact?max_length=100")
	json_format_cat_api = cat_api.json()
	cat_fact = json_format_cat_api['fact']
	return cat_fact