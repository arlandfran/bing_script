from loguru import logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyautogui
import os
import random

def search(mode):
    x = 0
    if mode == 'desktop':
        while x < 30:
            word = random.choice(WORDS)
            search_form = driver.find_element_by_class_name('b_searchbox')
            search_form.clear()
            search_form.send_keys(word)
            search_form.submit()
            x += 1
            logger.debug(f'Searched {word} {x}/30')
    elif mode == 'mobile':
        while x < 20:
            word = random.choice(WORDS)
            search_form = driver.find_element_by_class_name('b_searchbox')
            search_form.clear()
            search_form.send_keys(word)
            search_form.submit()
            x += 1
            logger.debug(f'Searched {word} {x}/20')

def change_viewport():
    pyautogui.press('f12')
    pyautogui.hotkey('ctrl', 'shift', 'm')

def complete_tasks():
    pass

path = os.getcwd() + '\\chromedriver.exe'
profile_path = 'C:\\Users\\arlan\\AppData\\Local\\Google\\Chrome\\User Data'

word_file = os.getcwd() + '\\words.txt'
WORDS = open(word_file).read().splitlines()

options = Options()
options.add_argument('user-data-dir=' + profile_path)
options.add_experimental_option('excludeSwitches', ['enable-logging']) # disables chrome logging on terminal
# options.headless = True

pyautogui.PAUSE = 1.0

with Chrome(executable_path=path, options=options) as driver:
    driver.implicitly_wait(3)
    driver.get('https://bing.com')
    logger.debug('Accessed Bing')
    search('desktop')
    change_viewport()
    search('mobile')
    change_viewport()
    pass