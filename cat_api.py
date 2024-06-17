import requests
import os
import random

print("Cat API Wakeup Call -- OKI !")

def getFact():
	cat_api = requests.get("https://catfact.ninja/fact?max_length=100")
	json_format_cat_api = cat_api.json()
	cat_fact = json_format_cat_api['fact']
	return cat_fact

#2024/6/16 <function select_bgm_c at 0x0000029A6EB2C4C0> eer!
#2024/6/17 fixed above err by correcting a typo and improved the code

def select_bgv_c():
	x = random.choice(os.listdir("cat_background_clips"))
	process_x = f"cat_background_clips/{x}"
	return process_x

def select_bgm_c():
	y = random.choice(os.listdir("cat_bgm"))
	process_y = f"cat_bgm/{y}" 
	return process_y

