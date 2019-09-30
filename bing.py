from loguru import logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import os
import random

def search():
    x = 0
    while x < 30:
        word = random.choice(WORDS)
        search_form = driver.find_element_by_class_name('b_searchbox')
        search_form.clear()
        search_form.send_keys(word)
        search_form.submit()
        x += 1
        logger.debug(f'Searched {word} {x}/30')

path = os.getcwd() + '\\chromedriver.exe'
profile_path = 'C:\\Users\\arlan\\AppData\\Local\\Google\\Chrome\\User Data'

word_file = os.getcwd() + '\\words.txt'
WORDS = open(word_file).read().splitlines()

options = Options()
options.add_argument('user-data-dir=' + profile_path)
# options.headless = True

with Chrome(executable_path=path, options=options) as driver:
    driver.implicitly_wait(3)
    driver.get('https://bing.com')
    logger.debug('Accessed Bing')
    search()
