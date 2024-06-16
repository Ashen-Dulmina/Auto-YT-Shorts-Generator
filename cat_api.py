import requests
import os
import random

print("Cat API Wakeup Call -- OKI !")

def getFact():
	cat_api = requests.get("https://catfact.ninja/fact?max_length=100")
	json_format_cat_api = cat_api.json()
	cat_fact = json_format_cat_api['fact']
	return cat_fact

def select_bgv_c():
	x_factor= random.choice(os.listdir("cat_background_clips"))#prints the function
	return x_factor

def select_bgm_c():
	y_factor= random.choice(os.listdir("cat_bgm"))#fix this 24/6/16 done 4 the day
	return y_factor