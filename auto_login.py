
from selenium.webdriver.common.keys import Keys
import time
import random

def login(username, password, browser):


	try:
		browser.get('https://www.casinonic.com/game/speed-roulette')
		time.sleep(random.randrange(3, 6))
		win_to_login = browser.find_element_by_class_name('auth__login')
		win_to_login.click()
		time.sleep(1)
		username_input = browser.find_element_by_name('email')
		username_input.clear()
		username_input.send_keys(username)

		time.sleep(2)

		password_imput = browser.find_element_by_name('password')
		password_imput.clear()
		password_imput.send_keys(password)

		password_imput.send_keys(Keys.ENTER)

		time.sleep(3)
		return browser

	except Exception as ex:
		print(ex)
		browser.close()
		browser.quit()
