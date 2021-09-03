import pytesseract
from auto_login import login
from auth_data import username, password
from selenium import webdriver
import time
import mss
import numpy as np
import datetime
import json
import cv2
from random import randint

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
browser = webdriver.Chrome(r'chromedriver.exe', options=chrome_options)
time.sleep(randint(2, 4))
login(username, password, browser)
browser.refresh()

time.sleep(randint(2, 4))

sct = mss.mss()

check_number = ''
last_time = time.time()

time_delta = datetime.datetime.now() + datetime.timedelta(minutes=10)

time.sleep(1)
with open('mouse_poss.json') as file:
	mon = json.load(file)

while True:
	if time.time() - last_time < 2:
		continue

	if time_delta < datetime.datetime.now():
		time_delta = datetime.datetime.now() + datetime.timedelta(minutes=10)
		browser.refresh()
		time.sleep(5)

	result = {}
	img = np.asarray(sct.grab(mon))
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	pars_string = pytesseract.image_to_string(hsv, lang='eng',
											  config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

	if pars_string != check_number:
		check_number = pars_string

		pars_string_clear = ''.join(filter(str.isdigit, pars_string))
		if pars_string_clear:
			print(f'найденное число - {pars_string_clear}')
			datetime_now = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
			digits = pars_string.rstrip('\f').rstrip('\n')
			result[datetime_now] = digits


			with open("data_mining.json", "a") as file:
					json.dump(result, file, indent=4)



	time.sleep(2)
